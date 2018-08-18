import struct

class ClassReader(object):

    def __init__(self,data):
        self.data = data

    def readUint8(self):
        value = self.data[0]
        self.data = self.data[1:]
        return value

    def readUint16(self):
        value = struct.unpack('>H',self.data[0:2])[0]
        self.data = self.data[2:]
        return value

    def readUint32(self):
        value = struct.unpack('>I',self.data[0:4])[0]
        self.data = self.data[4:]
        return value

    def readUint64(self):
        value = struct.unpack('>Q',self.data[0:8])[0]
        self.data = self.data[8:]
        return value

    def readUint16s(self):
        n = self.readUint16()
        s = []
        for i in range(n):
            s.append(self.readUint16())
        return s

    def readBytes(self,n):
        value = self.data[:n]
        self.data = self.data[n:]
        return value