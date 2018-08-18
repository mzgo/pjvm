class ConstantClassInfo(object):
    def __init__(self):
        self.cp = None
        self.nameIndex = None

    def readInfo(self,reader):
        self.nameIndex = reader.readUint16()

    def Name(self):
        return self.cp.getUtf8(self.nameIndex)