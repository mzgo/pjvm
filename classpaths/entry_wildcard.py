import os
from classpaths.entry import Entry


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
                    from classpaths.entry_zip import ZipEntry
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

