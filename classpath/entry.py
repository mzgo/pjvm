from abc import abstractmethod


class Entry(object):
    pathListSeparator = ""

    def __init__(self):
        string = ""

    @abstractmethod
    def readClass(self, className):
        pass

    @abstractmethod
    def String(self):
        pass

    def newEntry(self,path):
        pass