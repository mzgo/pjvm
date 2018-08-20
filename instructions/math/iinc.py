class IINC(object):

    def __init__(self):
        self.index = None  # uint
        self.const = None  # int32

    def FetchOperands(self, reader):
        self.index = reader.ReadUint8()
        self.const = reader.ReadInt8()

    def execute(self, frame):
        localVars = frame.localVars
        val = localVars.getIndex(self.index)
        val += self.const
        localVars.setIndex(self.index, val)
