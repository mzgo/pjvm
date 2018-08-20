from abc import ABCMeta, abstractmethod

#通用指令接口
class Instruction(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def FetchOperands(self,reader):
        pass

    @abstractmethod
    def execute(self,frame):
        pass

#无操作数指令
class NoOperandsInstruction(object):

    def FetchOperands(self,reader):
        pass

#跳转指令
class BranchInstruction(object):
    def __init__(self):
        self.offset = None #int

    def FetchOperands(self,reader):
        self.offset = reader.ReadInt16()

class Index8Instruction(object):
    def __init__(self):
        self.index = None #uint

    def FetchOperands(self,reader):
        self.index = reader.ReadUint8()

class Index16Instruction(object):
    def __init__(self):
        self.index = None #uint

    def FetchOperands(self,reader):
        self.index = reader.ReadUint16()