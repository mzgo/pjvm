class ConstantMemberrefInfo(object):
    def __init__(self,cp):
        self.cp = cp
        self.classIndex = None
        self.nameAndTypeIndex = None

    def readInfo(self,reader):
        self.classIndex = reader.readUint16()
        self.nameAndTypeIndex = reader.readUint16()

    def ClassName(self):
        return self.cp.getClassName(self.classIndex)

    def NameAndDescriptor(self):
        return self.cp.getNameAndType(self.nameAndTypeIndex)

class ConstantFieldrefInfo(ConstantMemberrefInfo):
    pass

class ConstantMethodrefInfo(ConstantMemberrefInfo):
    pass

class ConstantInterfaceMethodrefInfo(ConstantMemberrefInfo):
    pass