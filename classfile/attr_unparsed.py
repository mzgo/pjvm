class UnparsedAttribute(object):
    def __init__(self, attrName, attrLen):
        self.name = attrName
        self.length = attrLen
        self.info = None

    def readInfo(self, reader):
        self.info = reader.readBytes(self.length)
