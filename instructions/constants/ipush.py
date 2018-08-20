import struct


class BIPUSH(object):
    def __init__(self):
        self.val = None #int8

    def FetchOperands(self,reader):
        self.val = reader.ReadInt8()

    def execute(self,frame):
        frame.operandStack.push(struct.unpack('>l', struct.pack('>b', self.val))[0])

class SIPUSH(object):
    def __init__(self):
        self.val = None #int16

    def FetchOperands(self,reader):
        self.val = reader.ReadInt16()

    def execute(self,frame):
        frame.operandStack.push(struct.unpack('>l', struct.pack('>h', self.val))[0])
