from classfile.attribute_info import readAttributes

def readMembers(reader,cp):
    memberCount = reader.readUint16()
    members = []
    for i in range(memberCount):
        members.append(readMember(reader,cp))
    return members

def readMember(reader,cp):
    memberInfo = MemberInfo()
    memberInfo.cp = cp
    memberInfo.accessFlags = reader.readUint16()
    memberInfo.nameIndex = reader.readUint16()
    memberInfo.descriptorIndex = reader.readUint16()
    memberInfo.attributes = readAttributes(reader,cp)
    return memberInfo

class MemberInfo(object):

    def __init__(self):
        self.cp = None #ConstantPool
        self.accessFlags = None #uint16
        self.nameIndex = None #uint16
        self.descriptorIndex = None #uint16
        self.attributes = None #[]AttributeInfo

    def Name(self):
        return self.cp.getUtf8(self.nameIndex)

    def Descriptor(self):
        return self.cp.getUtf8(self.descriptorIndex)