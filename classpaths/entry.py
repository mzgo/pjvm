import os
import zipfile
from abc import abstractmethod

class Entry(object):
    pathListSeparator = os.sep

    def init(path):
        if (Entry.pathListSeparator in path):
            return CompositeEntry(path)
        if (path.endswith("*")):
            return WildcardEntry(path)
        if (path.endswith(".jar") or path.endswith(".JAR") or path.endswith(".zip") or path.endswith(".ZIP")):
            return ZipEntry(path)
        return DirEntry(path)

    @abstractmethod
    def readClass(self, className):
        pass

    @abstractmethod
    def String(self):
        pass


class CompositeEntry(Entry):

    def __init__(self, pathList):
        self.__compositeEntryList = []
        self.__pathList = pathList
        for path in str.split(pathList, Entry.pathListSeparator):
            self.__compositeEntryList.append(Entry.init(path))

    def readClass(self, className):
        for entry in self.__compositeEntryList:
            data = entry.readClass(className)
            if (data != None):
                return data

        print("CompositeEntry : class not found:" + className)
        exit()

    def String(self):
        return self.pathList

class DirEntry(Entry):
    absDir = "";

    def __init__(self, path):
        if (os.path.exists(path)):
            self.__absDir = os.path.abspath(path)
        else:
            print("DirEntry : path is not exists")
            exit()

    def readClass(self, className):
        fileName = os.path.join(self.__absDir, className)
        try:
            with open(fileName, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print("DirEntry : FileNotFoundError -> " + fileName)
            return None

    def String(self):
        return self.__absDir


class WildcardEntry(Entry):

    def __init__(self, path):
        self.__baseDir = path[:-1]
        self.__compositeEntryList = self.walk(self.__baseDir)
        self.__path = path

    def walk(self, path):
        compositeEntryList = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if (file.endswith(".jar") or file.endswith(".JAR")):
                    filePath = os.path.join(root, file)
                    compositeEntryList.append(ZipEntry(filePath))
        return compositeEntryList

    def readClass(self, className):
        for entry in self.__compositeEntryList:
            data = entry.readClass(className)
            if (data != None):
                return data

        print("WildcardEntry : class not found:" + className)
        exit()

    def String(self):
        return self.pathList

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