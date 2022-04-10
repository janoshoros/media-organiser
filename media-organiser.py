import sys
import os
import time
from pathlib import Path
from PIL import Image
from ExifTags import TAGS
from ExifTags import GPSTAGS
import hashlib
from collections import defaultdict
import pprint
import shutil
from datetime import datetime
import requests
import json


def main():
    errs = []
    dst = sys.argv[2]
    bkp_dir = os.path.join(dst, "duplicates")
    repository = mediaItemRepository()
    filter = [".jpg", ".png", ".gif", ".webp", ".tiff", ".psd", ".raw", ".bmp", ".heif", ".indd", ".jpeg", ".svg", ".ai", ".eps", ".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd", ".avi", ".heic", ".m4a", ".3gp"]
    if len(sys.argv)>3 and sys.argv[3] !=None:
        filter = sys.argv[3]

    print("--------------------------------------------------------------")
    print(f"looking for {filter}")
    print(f"source: {sys.argv[1]} dst: {sys.argv[2]}")

    print("performing file analysis\n")
    subfolders, files = run_fast_scandir(sys.argv[1], filter)
    i = 1
    total_count = len(files)
    for file in files:
        repository.registerItem(file)
        printProgressBar(i, total_count)
        i +=1
        
    ri = repository.registeredItems()
    print("performing metadata analysis\n")
    
    i=1
    total_count = len(ri)
    for item in ri:
        try:
            mi = ri[item]
            exif = get_exif(mi.path)

            originalDate = get_original_date(exif)
            if originalDate != None:
                mi.originalDate = get_original_date(exif)
                if mi.originalDate == "0000:00:00 00:00:00":
                    mi.originalDate = datetime.fromtimestamp(os.path.getmtime(mi.path)).strftime(f"%Y:%m:%d %H:%M:%S")
                #print(f"Original date from exif: {mi.originalDate}")
            else:
                mi.originalDate = datetime.fromtimestamp(os.path.getmtime(mi.path)).strftime(f"%Y:%m:%d %H:%M:%S")
                #print(f"Original date from file: {mi.originalDate}") #move out of exif analysis to make sure this will work for files with empty exif
            
            try:
                geotags = get_geotagging(exif)
                mi.coordinates = get_coordinates(geotags)
                mi.location = get_location(geotags)
            except BaseException as err:
                errs.append(err)

        except BaseException as err:
            #print(f"Err: {err}")
                errs.append(err)
        
        printProgressBar(i, total_count)
        i +=1

    print(f"checking dst directory {dst}")
    if not os.path.exists(dst):
        print("not found")
        try:
            print("creating dst directory")
            os.makedirs(dst)
        except OSError as e:
            #if e.errno != errno.EEXIST:
            raise e

    print("moving files\n")
    i=1
    total_count = len(ri)

    for item in ri:
        mi = ri[item]
        #print(vars(mi))

        dv = mi.originalDate
        #print(dv)


        if dv == None:
            dv = datetime.now().strftime(f"%Y:%m:%d %H:%M:%S")
        try:
            d = datetime.strptime(dv,f"%Y:%m:%d %H:%M:%S")
        except BaseException as ex:
            d = datetime.strptime(datetime.now().strftime(f"%Y:%m:%d %H:%M:%S"),f"%Y:%m:%d %H:%M:%S")

        dest_dir = os.path.join(dst, str(d.year))

        if mi.location != None  and len(mi.location)>0:
            dest_dir = os.path.join(dest_dir, mi.location[0])
        else:
            dest_dir = os.path.join(dest_dir, "unknown location")

        dest_path = os.path.join(dest_dir, os.path.basename(mi.path))
        
        #print(f"dest dir: {dest_dir} dest_file: {dest_path}")

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        try:
            #print(f"copy {mi.path} to {dest_path}")
            u_dp = get_unique_filename_with_path(dest_path)
            shutil.copy2(mi.path, u_dp)
            os.remove(mi.path)
        except BaseException as e:
            print(e)
        
        for dp_key in mi.duplicates:
            dp_list = mi.duplicates[dp_key]
            for dp in dp_list:
                #print(f"duplicate: {vars(mi)}")
                if not os.path.exists(bkp_dir):
                    os.makedirs(bkp_dir)
                dp_dest = os.path.join(bkp_dir, os.path.basename(dp.path))
                u_dp = get_unique_filename_with_path(dp_dest)
                try:
                    #print(f"copy {mi.path} to {u_dp}")
                    shutil.copy2(dp.path, u_dp)
                    os.remove(dp.path)
                except BaseException as e:
                    print(e)
    
        printProgressBar(i, total_count)
        i +=1

    print("Errors during execution:")
    for err in errs:
        print(err)    
    
    print("\nDone!\n")

def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)


    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files


def get_unique_filename_with_path(dst):

    if os.path.exists(dst):
        i = 0
        o_dst = dst
        while os.path.exists(dst):
            file_name = os.path.splitext(os.path.basename(o_dst))
            #print(file_name)
            new_file_name = file_name[0] + f"_{i}" + file_name[1]
            #print(new_file_name)
            dst = os.path.join(os.path.dirname(o_dst), new_file_name)
            #print(dst)
            i+=1
            
    return dst
   
def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]
                    #print(f"val: {val} idx: {idx} key: {key} value: {exif[idx][key]}")

    return geotagging

def get_decimal_from_dms(dms, ref):
    #print(f"dms:{dms} ref: {ref}")

    degrees = float(dms[0])#dms[0][0] / dms[0][1]
    minutes = float(dms[1]) / 60.0 #dms[1][0] / dms[1][1] / 60.0
    seconds = float(dms[2]) / 3600.0#dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    retValue = round(degrees + minutes + seconds, 5)
    #print(f"retValue: {float(retValue)}")
    return retValue

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat,lon)



def get_location(geotags):
    coords = get_coordinates(geotags)

    #print(f"calling bigdatacloud api with values:{coords}")
    uri = f"https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={coords[0]}&longitude={coords[1]}&localityLanguage=en"
    #print(uri)

    response = requests.get(uri)
    #print(response)
    try:
        response.raise_for_status()
        #print(response.json)

        geo_info = json.loads(response.text)
        ret_value = []
        
        for adm_info_element in geo_info["localityInfo"]["administrative"]:
            ret_value.append(adm_info_element["name"])
            
        #print(ret_value)
        return ret_value

    except requests.exceptions.HTTPError as e:
        print(str(e))
        return {}

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()


def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

def get_original_date(exif):
    for (key, val) in exif.items():
        #print(f"{key} [{TAGS.get(key)}]: {val}")
        if key == 36867:
            return val

class mediaItem:
    
    def __init__(self):
        self.__init__(None)

    def __init__(self, path):
        self.path = path
        self.duplicates = defaultdict(list)#dict()#[str, mediaItem] #defaultdict(<class 'mediaitem.mediaItem'>, {})
        self.coordinates = None
        self.originalDate = None
        self.MD5 = None
        self.location = None

    def path(self):
        return self.path

    def MD5(self):
        return self.MD5

    def duplicates(self):
        return self.duplicates

    def location(self):
        return self.location
    
    def coordinates(self):
        return self.coordinates

    def originalDate(self):
        return self.originalDate

class mediaItemRepository:

    def __init__(self):
        self.itemsCollection = dict()#[str, mediaItem]
    

    def registeredItems(self):
        return self.itemsCollection

    def registerItem(self, fname):
        #print(f"New item registration")
        m = md5(fname)
        #print(f"File: {fname} MD5: {m}")
        if m in self.itemsCollection:
            #print("Looks like duplicate")
            mi = self.itemsCollection.get(m)
            mi.duplicates[m].append(mediaItem(fname))
            #print("Added to duplicates")
            #print(vars(mi))
        else:
            self.itemsCollection[m] = mediaItem(fname)



# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


if __name__=="__main__":
    main()