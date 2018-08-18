class ConstantValueAttribute(object):
    def __init__(self):
        self.constantValueIndex = None

    def readInfo(self, reader):
        self.constantValueIndex = reader.readUint16()

    def ConstantValueIndex(self):
        return self.constantValueIndex
