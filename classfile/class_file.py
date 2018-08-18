from classfile.attribute_info import readAttributes
from classfile.class_reader import ClassReader
from classfile.constant_pool import readConstantPool
from classfile.member_info import readMembers


def parse(classData):
    #try:
    cr = ClassReader(classData)
    cf = ClassFile()
    cf.read(cr)
    return cf
    #except:
    #    print("错误 : ClassFile.parse() : 解析class文件出错！")
#    exit()


class ClassFile(object):

    def __init__(self):
        self.minorVersion = None  # uint16
        self.majorVersion = None  # uint16
        self.constantPool = None  # ConstantPool
        self.accessFlags = None  # uint16
        self.thisClass = None  # uint16
        self.superClass = None  # uint16
        self.interfaces = None  # []uint16
        self.fields = None  # []*MemberInfo
        self.methods = None  # []*MemberInfo
        self.attributes = None  # []AttributeInfo


    def read(self,reader):
        self.readAndCheckMagic(reader)
        self.readAndCheckVersion(reader)
        self.constantPool = readConstantPool(reader)
        self.accessFlags = reader.readUint16()
        self.thisClass = reader.readUint16()
        self.superClass = reader.readUint16()
        self.interfaces = reader.readUint16s()
        self.fields = readMembers(reader, self.constantPool)
        self.methods = readMembers(reader, self.constantPool)
        self.attributes = readAttributes(reader, self.constantPool)

    def ClassName(self):
        return self.constantPool.getClassName(self.thisClass)

    def SuperClassName(self):
        if self.superClass > 0 :
            return self.constantPool.getClassName(self.superClass)
        return "" #Object 没有父类

    def InterfaceNames(self):
        interfaceNames = []
        for i in self.interfaces :
            interfaceNames.append(self.constantPool.getClassName(i))
        return interfaceNames

    def readAndCheckMagic(self,reader):
        magic = hex(reader.readUint32());
        if magic != "0xcafebabe" :
            print("错误 : java.lang.ClassFormatError : magic !")
            exit()

    def readAndCheckVersion(self,reader):
        self.minorVersion = reader.readUint16()
        self.majorVersion = reader.readUint16()
        if self.majorVersion == 45 :
            return
        elif self.majorVersion in [46,47,48,49,50,51,52]:
            if self.minorVersion == 0 :
                return
        print("错误 : java.lang.UnsupportedClassVersionError!")
        exit()