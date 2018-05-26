import os
from abc import abstractmethod


class Entry(object):
    pathListSeparator = os.sep

    @abstractmethod
    def readClass(self, className):
        pass

    @abstractmethod
    def String(self):
        pass


def newEntry(path):
    if (Entry.pathListSeparator in path):
        from classpaths.entry_composite import CompositeEntry
        return CompositeEntry(path)
    if (path.endswith("*")):
        from classpaths.entry_wildcard import WildcardEntry
        return WildcardEntry(path)
    if (path.endswith(".jar") or path.endswith(".JAR") or path.endswith(".zip") or path.endswith(".ZIP")):
        from classpaths.entry_zip import ZipEntry
        return ZipEntry(path)
    from classpaths.entry_dir import DirEntry
    return DirEntry(path)
