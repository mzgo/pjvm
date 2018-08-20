from classfile.constant_info import *

class ConstantPool(object):

    def __init__(self,data):
        self.data = data

    # 按索引查找常量
    def getConstantInfo(self, index):
        try:
            cpInfo = self.data[index]
            return cpInfo
        except:
            print("错误 : ConstantPool : 无效的常量池索引！")
            exit()

    # 从常量池查找字段或方法的名字和描述符
    def getNameAndType(self, index):
        ntInfo = self.getConstantInfo(index)
        name = self.getUtf8(ntInfo.nameIndex)
        type = self.getUtf8(ntInfo.descriptorIndex)
        return name, type

    def getClassName(self, index):
        classInfo = self.getConstantInfo(index)
        return self.getUtf8(classInfo.nameIndex)

    def getUtf8(self, index):
        utf8Info = self.getConstantInfo(index)
        return utf8Info.str

def readConstantPool(reader):
    cpCount = reader.readUint16()
    cp = [0 for i in range(cpCount)]
    i = 1
    while i < cpCount:
        cp[i] = readConstantInfo(reader, cp)
        if isinstance(cp[i], ConstantLongInfo) or isinstance(cp[i], ConstantDoubleInfo):
            i = i + 1
        i = i + 1
    return ConstantPool(cp)


def readConstantInfo(reader, cp):
    tag = reader.readUint8()
    c = newConstantInfo(tag, cp)
    c.readInfo(reader)
    return c


def newConstantInfo(tag, cp):
    if tag == CONSTANT_Integer:
        return ConstantIntegerInfo()
    elif tag == CONSTANT_Float:
        return ConstantFloatInfo()
    elif tag == CONSTANT_Long:
        return ConstantLongInfo()
    elif tag == CONSTANT_Double:
        return ConstantDoubleInfo()
    elif tag == CONSTANT_Utf8:
        return ConstantUtf8Info()
    elif tag == CONSTANT_String:
        return ConstantStringInfo()
    elif tag == CONSTANT_Class:
        return ConstantClassInfo()
    elif tag == CONSTANT_Fieldref:
        return ConstantFieldrefInfo(ConstantMemberrefInfo(cp))
    elif tag == CONSTANT_Methodref:
        return ConstantMethodrefInfo(ConstantMemberrefInfo(cp))
    elif tag == CONSTANT_InterfaceMethodref:
        return ConstantInterfaceMethodrefInfo(ConstantMemberrefInfo(cp))
    elif tag == CONSTANT_NameAndType:
        return ConstantNameAndTypeInfo()
    elif tag == CONSTANT_MethodType:
        return ConstantMethodTypeInfo()
    elif tag == CONSTANT_MethodHandle:
        return ConstantMethodHandleInfo()
    elif tag == CONSTANT_InvokeDynamic :
        return ConstantInvokeDynamicInfo()
    else:
        print("错误 : java.lang.ClassFormatError: constant pool tag!")
        exit()
