import os
import sys
import zipfile

from classpath.entry import Entry


class ZipEntry(Entry):
    def __init__(self, path):
        if (os.path.exists(path)):
            self.__absPath = os.path.abspath(path)
        else:
            print("path is not exists")
            exit()

    def readClass(self, className):
        if not (zipfile.is_zipfile(self.__absPath)):
            print("file is not zipfile:" + self.__absPath)
            return None

        try:
            azip = zipfile.ZipFile(self.__absPath)
            nameList = azip.namelist()
            try:
                for i in nameList:
                    if (i == className):
                        with azip.open(i, 'r') as file:
                            return file.read()
            except FileNotFoundError:
                print("cannot found className:" + className + " in zipfile " + self.__absPath)
                return None
        except FileNotFoundError:
            print("className:" + className + " is not found")
            return None

    def String(self):
        return self.__absPath
