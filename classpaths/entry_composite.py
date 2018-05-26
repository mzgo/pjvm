import os
import sys


# 打印对象所有属性
def prn_obj(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


from classpaths.entry import Entry, newEntry


class CompositeEntry(Entry):

    def __init__(self, pathList):
        self.__compositeEntryList = []
        self.__pathList = pathList
        for path in str.split(pathList, Entry.pathListSeparator):
            self.__compositeEntryList.append(newEntry(path))

    def readClass(self, className):
        for entry in self.__compositeEntryList:
            data = entry.readClass(className)
            if (data != None):
                return data

        print("CompositeEntry : class not found:" + className)
        exit()

    def String(self):
        return self.pathList

# cm = CompositeEntry("a\\b\c").getCompositeEntrys()
