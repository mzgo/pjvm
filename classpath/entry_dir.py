import os
import sys

from classpath.entry import Entry


class DirEntry(Entry):
    def __init__(self, path):
        if (os.path.exists(path)):
            self.__absDir = os.path.abspath(path)
        else:
            print("path is not exists")
            exit()

    def readClass(self, className):
        fileName = os.path.join(self.__absDir, className)
        try:
            with open('fileName', 'r') as file:
                return file.read()
        except FileNotFoundError:
            print("className:" + className + " is not found")
            return None

    def String(self):
        return self.__absDir