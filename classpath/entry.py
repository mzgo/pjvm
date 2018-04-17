import os
from abc import abstractmethod


class Entry(object):
    os.sep

    def __init__(self,pathListSeparator):
        self.pathListSeparator = ""

    @abstractmethod
    def readClass(self, className):
        pass

    @abstractmethod
    def String(self):
        pass

    def newEntry(self,path):
        pass

print(os.sep)