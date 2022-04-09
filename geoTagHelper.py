import os
import requests
from ExifTags import TAGS, GPSTAGS
import json

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

    #dms:(27.0, 54.0, 55.86) ref: N
    #print("bla")
    #print(dms[0])
    #print(dms[1])
    #print(dms[2])

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


