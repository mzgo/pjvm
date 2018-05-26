import os
import zipfile

from classpaths.entry import Entry


class ZipEntry(Entry):

    def __init__(self, path):
        if (os.path.exists(path)):
            self.__absPath = os.path.abspath(path)
            print(self.__absPath)
        else:
            print("ZipEntry : path is not exists")
            exit()

    def readClass(self, className):
        if not (zipfile.is_zipfile(self.__absPath)):
            print("ZipEntry : file is not zipfile:" + self.__absPath)
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
                print("ZipEntry : cannot found className:" + className + " in zipfile " + self.__absPath)
                exit()
        except FileNotFoundError:
            print("ZipEntry : className:" + className + " is not found")
            exit()

    def String(self):
        return self.__absPath