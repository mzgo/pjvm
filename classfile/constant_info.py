#定义常量池中各种数据结构

import struct
from abc import abstractmethod

#常量类型 tag
CONSTANT_Class = 7
CONSTANT_Fieldref = 9
CONSTANT_Methodref = 10
CONSTANT_InterfaceMethodref = 11
CONSTANT_String = 8
CONSTANT_Integer = 3
CONSTANT_Float = 4
CONSTANT_Long = 5
CONSTANT_Double = 6
CONSTANT_NameAndType = 12
CONSTANT_Utf8 = 1
CONSTANT_MethodHandle = 15
CONSTANT_MethodType = 16
CONSTANT_InvokeDynamic = 18

#常量池数据对象接口
class ConstantInfo(object):
    @abstractmethod
    def readInfo(self):
        pass

#Integer
"""
CONSTANT_Integer_info {
    u1 tag;
    u4 bytes;
}
"""
class ConstantIntegerInfo(ConstantInfo):
    def __init__(self):
        self.val = None

    def readInfo(self,reader):
        self.val = reader.readUint32()

#Float
"""
CONSTANT_Float_info {
    u1 tag;
    u4 bytes;
}
"""
class ConstantFloatInfo(ConstantInfo):
    def __init__(self):
        self.val = None

    def readInfo(self,reader):
        b = reader.readUint32()
        b = b.to_bytes(length=1, byteorder='big')
        self.val = struct.unpack('<f', struct.pack('4b', *b))[0]

#Long
"""
CONSTANT_Long_info {
    u1 tag;
    u4 high_bytes;
    u4 low_bytes;
}
"""
class ConstantLongInfo(ConstantInfo):
    def __init__(self):
        self.val = None

    def readInfo(self,reader):
        self.val = reader.readUint64()

#Double
"""
CONSTANT_Double_info {
    u1 tag;
    u4 high_bytes;
    u4 low_bytes;
}
"""
class ConstantDoubleInfo(ConstantInfo):
    def __init__(self):
        self.val = None

    def readInfo(self,reader):
        b = reader.readUint64()
        b = b.to_bytes(length=1, byteorder='big')
        self.val = struct.unpack('<d', struct.pack('8b', *b))[0]


"""
CONSTANT_Utf8_info {
    u1 tag;
    u2 length;
    u1 bytes[length];
}
"""
#String数据
class ConstantUtf8Info(ConstantInfo):
    def __init__(self):
        self.str = None

    def readInfo(self,reader):
        length = reader.readUint16()
        b = reader.readBytes(length)
        self.str = bytes.decode(b, encoding = "utf8")


"""
CONSTANT_String_info {
    u1 tag;
    u2 string_index;
}
"""
#String 索引
class ConstantStringInfo(ConstantInfo):
    def __init__(self):
        self.cp = None
        self.stringIndex = None

    def readInfo(self,reader):
        self.stringIndex = reader.readUint16()

    def String(self):
        return self.cp.getUtf8(self.stringIndex)


"""
CONSTANT_Class_info {
    u1 tag;
    u2 name_index;
}
"""
#类和超类 限定名
class ConstantClassInfo(ConstantInfo):
    def __init__(self):
        self.cp = None
        self.nameIndex = None

    def readInfo(self,reader):
        self.nameIndex = reader.readUint16()

    def Name(self):
        return self.cp.getUtf8(self.nameIndex)


"""
CONSTANT_Fieldref_info {
    u1 tag;
    u2 class_index;
    u2 name_and_type_index;
}
CONSTANT_Methodref_info {
    u1 tag;
    u2 class_index;
    u2 name_and_type_index;
}
CONSTANT_InterfaceMethodref_info {
    u1 tag;
    u2 class_index;
    u2 name_and_type_index;
}
"""
#字段符号、普通方法、接口方法的通用类
class ConstantMemberrefInfo(ConstantInfo):
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

#字段符号
class ConstantFieldrefInfo(ConstantMemberrefInfo):
    pass

#普通方法
class ConstantMethodrefInfo(ConstantMemberrefInfo):
    pass

#接口方法
class ConstantInterfaceMethodrefInfo(ConstantMemberrefInfo):
    pass

"""
CONSTANT_NameAndType_info {
    u1 tag;
    u2 name_index;
    u2 descriptor_index;
}
"""
#给出字段或方法的名称和描述符
class ConstantNameAndTypeInfo(object):
    def __init__(self):
        self.nameIndex = None
        self.descriptorIndex = None

    def readInfo(self,reader):
        self.nameIndex = reader.readUint16()
        self.descriptorIndex = reader.readUint16()


"""
CONSTANT_MethodHandle_info {
    u1 tag;
    u1 reference_kind;
    u2 reference_index;
}
"""
#Java SE 7添加到class文件中的，目的是支持新增的invokedynamic指令
class ConstantMethodHandleInfo(ConstantInfo):
    def __init__(self):
        self.referenceKind = None #uint8
        self.referenceIndex = None #uint16

    def readInfo(self,reader):
        self.referenceKind = reader.readUint8()
        self.referenceIndex = reader.readUint16()


"""
CONSTANT_MethodType_info {
    u1 tag;
    u2 descriptor_index;
}
"""
#Java SE 7添加到class文件中的，目的是支持新增的invokedynamic指令
class ConstantMethodTypeInfo(ConstantInfo):
    def __init__(self):
        self.descriptorIndex = None #uint16

    def readInfo(self,reader):
        self.descriptorIndex = reader.readUint16()


"""
CONSTANT_InvokeDynamic_info {
    u1 tag;
    u2 bootstrap_method_attr_index;
    u2 name_and_type_index;
}
"""
#Java SE 7添加到class文件中的，目的是支持新增的invokedynamic指令
class ConstantInvokeDynamicInfo(ConstantInfo):
    def __init__(self):
        self.bootstrapMethodAttrIndex = None #uint16
        self.nameAndTypeIndex = None #uint16

    def readInfo(self,reader):
        self.bootstrapMethodAttrIndex = reader.readUint16()
        self.nameAndTypeIndex = reader.readUint16()