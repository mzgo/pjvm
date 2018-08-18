from classfile.attribute_info import readAttributes


class CodeAttribute(object):
    def __init__(self,cp):
        self.cp = cp
        self.maxStack = None
        self.maxLocals = None
        self.code = None
        self.exceptionTable = None
        self.attribute = None

    def readInfo(self,reader):
        self.maxStack = reader.readUint16()
        self.maxLocals = reader.readUint16()
        codeLength = reader.readUint32()
        self.code = reader.readBytes(codeLength)
        self.exceptionTable = readExceptionTable(reader)
        self.attributes = readAttributes(reader, self.cp)

class ExceptionTableEntry(object):
    def __init__(self):
        self.startPc = None
        self.endPc = None
        self.handlerPc = None
        self.catchType = None

def readExceptionTable(reader):
    exceptionTableLength = reader.readUint16()
    exceptionTable = []
    for i in range(exceptionTableLength):
        e = ExceptionTableEntry()
        e.startPc = reader.readUint16()
        e.endPc = reader.readUint16()
        e.handlerPc = reader.readUint16()
        e.catchType = reader.readUint16()
        exceptionTable.append(e)
    return exceptionTable