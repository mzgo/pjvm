class ConstantStringInfo(object):
    def __init__(self):
        self.cp = None
        self.stringIndex = None

    def readInfo(self,reader):
        self.stringIndex = reader.readUint16()

    def String(self):
        return self.cp.getUtf8(self.stringIndex)