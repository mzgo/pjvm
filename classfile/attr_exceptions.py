class ExceptionsAttribute(object):
    def __init__(self):
        self.exceptionIndexTable = None

    def readInfo(self,reader):
        self.exceptionIndexTable = reader.readUint16s()

    def ExceptionIndexTable(self):
        return self.exceptionIndexTable