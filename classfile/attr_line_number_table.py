class LineNumberTableAttribute(object):
    def __init__(self):
        self.lineNumberTable = None

    def readInfo(self,reader):
        lineNumberTableLength = reader.readUint16()
        self.lineNumberTable = []
        for i in range(lineNumberTableLength):
            l = LineNumberTableEntry()
            l.startPc = reader.readUint16()
            l.lineNumber = reader.readUint16()
            self.lineNumberTable.append(l)

class LineNumberTableEntry(object):
    def __init__(self):
        self.startPc = None
        self.lineNumber = None

class LocalVariableTableAttribute(object):
    def __init__(self):
        self.localVariableTable = None

    def readInfo(self,reader):
        LocalVariableTableLength = reader.readUint16()
        self.localVariableTable = []
        for i in range(LocalVariableTableLength):
            l = LocalVariableTable()
            l.startPc = reader.readUint16()
            l.localVariable = reader.readUint16()
            self.localVariableTable.append(l)

class LocalVariableTable(object):
    def __init__(self):
        self.startPc = None
        self.localVariable = None