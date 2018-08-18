class ConstantUtf8Info(object):
    def __init__(self):
        self.str = None

    def readInfo(self,reader):
        length = reader.readUint16()
        b = reader.readBytes(length)
        self.str = bytes.decode(b, encoding = "utf8")