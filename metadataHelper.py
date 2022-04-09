
from PIL import Image
from ExifTags import TAGS

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
