import struct


class BytecodeReader(object):
    def __init__(self):
        self.code = None #[]byte
        self.pc = None #int

    def Reset(self,code,pc):
        self.code = code
        self.pc = pc

    def ReadUint8(self):
        i = self.code[self.pc]
        self.pc += 1
        return i

    def ReadInt8(self):
        return struct.unpack('>b', struct.pack('>B',self.ReadInt8()))[0]

    def ReadUint16(self):
        return struct.unpack('>H', struct.pack('>BB', self.ReadInt8(), self.ReadInt8()))[0]

    def ReadInt16(self):
        return struct.unpack('>h', struct.pack('>H',self.ReadUint16()))[0]

    def ReadInt32(self):
        return struct.unpack('>l', struct.pack('>BBBB',self.ReadUint8(),self.ReadUint8(),self.ReadUint8(),self.ReadUint8()))[0]

    def ReadInt32s(self):
        pass

    def SkipPadding(self):
        pass