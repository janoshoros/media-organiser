import md5helper
from collections import defaultdict


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
        m = md5helper.md5(fname)
        #print(f"File: {fname} MD5: {m}")
        if m in self.itemsCollection:
            #print("Looks like duplicate")
            mi = self.itemsCollection.get(m)
            mi.duplicates[m].append(mediaItem(fname))
            #print("Added to duplicates")
            #print(vars(mi))
        else:
            self.itemsCollection[m] = mediaItem(fname)


