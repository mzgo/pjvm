import struct

class ConstantIntegerInfo(object):
    def __init__(self):
        self.val = None

    def readInfo(self,reader):
        self.val = reader.readUint32()

class ConstantFloatInfo(object):
    def __init__(self):
        self.val = None

    def readInfo(self,reader):
        b = reader.readUint32()
        b = b.to_bytes(length=1, byteorder='big')
        self.val = struct.unpack('<f', struct.pack('4b', *b))[0]

class ConstantLongInfo(object):
    def __init__(self):
        self.val = None

    def readInfo(self,reader):
        self.val = reader.readUint64()

class ConstantDoubleInfo(object):
    def __init__(self):
        self.val = None

    def readInfo(self,reader):
        b = reader.readUint64()
        b = b.to_bytes(length=1, byteorder='big')
        self.val = struct.unpack('<d', struct.pack('8b', *b))[0]