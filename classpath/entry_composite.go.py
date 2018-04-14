import os
import sys

from classpath.entry import Entry


class  CompositeEntry (Entry):
    def __init__(self, pathList):
        self.__pathList = pathList

    def  newCompositeEntry(self):
        compositeEntry = []
        for path in str.split(self.__pathList,":") :
            compositeEntry.append(Entry().newEntry(path))
        return compositeEntry

    def readClass(self, className):
        pass


    def String(self):
        return self.__absDir

cm = CompositeEntry("1:2:3")
cm.newCompositeEntry()