import sys
import os
import time
from pathlib import Path
from mediaitem import mediaItem
from mediaitem import mediaItemRepository
import metadataHelper
import geoTagHelper
import pprint
import shutil
from datetime import datetime
import file_helper
import progress_helper


def main():
    errs = []
    dst = sys.argv[2]
    bkp_dir = os.path.join(dst, "duplicates")
    repository = mediaItemRepository()
    filter = [".jpg", ".png", ".gif", ".webp", ".tiff", ".psd", ".raw", ".bmp", ".heif", ".indd", ".jpeg", ".svg", ".ai", ".eps", ".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd", ".avi", ".heic", ".m4a", ".3gp"]
    #[".jpg",".jpeg", ".png", ".mov", ".avi", ".mp4", ".heic", ".m4a"]
    if len(sys.argv)>3 and sys.argv[3] !=None:
        filter = sys.argv[3]
    subfolders, files = run_fast_scandir(sys.argv[1], filter)
    print("--------------------------------------------------------------")
    print(f"looking for {filter}")
    print(f"source: {sys.argv[1]} dst: {sys.argv[2]}")

    print("performing file analysis\n")
    i = 1
    total_count = len(files)
    for file in files:
        repository.registerItem(file)
        progress_helper.printProgressBar(i, total_count)
        i +=1
        
    ri = repository.registeredItems()
    print("performing metadata analysis\n")
    
    i=1
    total_count = len(ri)
    for item in ri:
        try:
            mi = ri[item]
            exif = metadataHelper.get_exif(mi.path)

            originalDate = metadataHelper.get_original_date(exif)
            if originalDate != None:
                mi.originalDate = metadataHelper.get_original_date(exif)
                if mi.originalDate == "0000:00:00 00:00:00":
                    mi.originalDate = datetime.fromtimestamp(os.path.getmtime(mi.path)).strftime(f"%Y:%m:%d %H:%M:%S")
                #print(f"Original date from exif: {mi.originalDate}")
            else:
                mi.originalDate = datetime.fromtimestamp(os.path.getmtime(mi.path)).strftime(f"%Y:%m:%d %H:%M:%S")
                #print(f"Original date from file: {mi.originalDate}") #move out of exif analysis to make sure this will work for files with empty exif
            
            try:
                geotags = geoTagHelper.get_geotagging(exif)
                mi.coordinates = geoTagHelper.get_coordinates(geotags)
                mi.location = geoTagHelper.get_location(geotags)
            except BaseException as err:
                errs.append(err)

        except BaseException as err:
            #print(f"Err: {err}")
                errs.append(err)
        
        progress_helper.printProgressBar(i, total_count)
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
        
        d = datetime.strptime(dv,f"%Y:%m:%d %H:%M:%S")

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
            u_dp = file_helper.get_unique_filename_with_path(dest_path)
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
                u_dp = file_helper.get_unique_filename_with_path(dp_dest)
                try:
                    #print(f"copy {mi.path} to {u_dp}")
                    shutil.copy2(dp.path, u_dp)
                    os.remove(dp.path)
                except BaseException as e:
                    print(e)
    
        progress_helper.printProgressBar(i, total_count)
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

   

if __name__=="__main__":
    main()
