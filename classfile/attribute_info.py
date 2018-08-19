from abc import abstractmethod

def readAttributes(reader,cp):
    attributesCount = reader.readUint16()
    attributes = []
    for i in range(attributesCount):
        attributes.append(readAttribute(reader,cp))
    return attributes

def readAttribute(reader,cp):
    attrNameIndex = reader.readUint16()
    attrName = cp.getUtf8(attrNameIndex)
    attrLen = reader.readUint32()
    attrInfo = newAttributeInfo(attrName, attrLen, cp)
    attrInfo.readInfo(reader)
    return attrInfo

def newAttributeInfo(attrName,attrLen,cp):
    if attrName == "Code":
        return CodeAttribute(cp)
    elif attrName == "ConstantValue":
        return ConstantValueAttribute()
    elif attrName == "Deprecated":
        return DeprecatedAttribute()
    elif attrName == "Exceptions":
        return ExceptionsAttribute()
    elif attrName == "LineNumberTable":
        return LineNumberTableAttribute()
    elif attrName == "LocalVariableTable":
        return LocalVariableTableAttribute()
    elif attrName == "SourceFile":
        return SourceFileAttribute(cp)
    elif attrName == "Synthetic":
        return SyntheticAttribute()
    else:
        return UnparsedAttribute(attrName, attrLen)

#属性池通用接口
"""
attribute_info {
    u2 attribute_name_index;
    u4 attribute_length;
    u1 info[attribute_length];
}
"""
class AttributeInfo(object):
    @abstractmethod
    def readInfo(self,reader,cp):
        pass

"""
Code_attribute {
    u2 attribute_name_index;
    u4 attribute_length;
    u2 max_stack;
    u2 max_locals;
    u4 code_length;
    u1 code[code_length];
    u2 exception_table_length;
    {   u2 start_pc;
        u2 end_pc;
        u2 handler_pc;
        u2 catch_type;
    } exception_table[exception_table_length];
    u2 attributes_count;
    attribute_info attributes[attributes_count];
}
"""
#Code是变长属性，只存在于method_info结构中。Code属性中存放字节码等方法相关信息
class CodeAttribute(AttributeInfo):
    def __init__(self,cp):
        self.cp = cp
        self.maxStack = None
        self.maxLocals = None
        self.code = None
        self.exceptionTable = None
        self.attribute = None

    def readInfo(self,reader):
        self.maxStack = reader.readUint16()
        self.maxLocals = reader.readUint16()
        codeLength = reader.readUint32()
        self.code = reader.readBytes(codeLength)
        self.exceptionTable = self.readExceptionTable(reader)
        self.attributes = readAttributes(reader, self.cp)

    class ExceptionTableEntry(object):
        def __init__(self):
            self.startPc = None
            self.endPc = None
            self.handlerPc = None
            self.catchType = None

    def readExceptionTable(self,reader):
        exceptionTableLength = reader.readUint16()
        exceptionTable = []
        for i in range(exceptionTableLength):
            e = self.ExceptionTableEntry()
            e.startPc = reader.readUint16()
            e.endPc = reader.readUint16()
            e.handlerPc = reader.readUint16()
            e.catchType = reader.readUint16()
            exceptionTable.append(e)
        return exceptionTable

"""
ConstantValue_attribute {
    u2 attribute_name_index;
    u4 attribute_length;
    u2 constantvalue_index;
}
"""
#ConstantValue是定长属性，只会出现在field_info结构中，用于表示常量表达式的值
class ConstantValueAttribute(AttributeInfo):
    def __init__(self):
        self.constantValueIndex = None

    def readInfo(self, reader):
        self.constantValueIndex = reader.readUint16()

    def ConstantValueIndex(self):
        return self.constantValueIndex

"""
Deprecated_attribute {
    u2 attribute_name_index;
    u4 attribute_length;
}
"""
#Deprecated属性用于指出类、接口、字段或方法已经不建议使用，编译器等工具可以根据Deprecated属性输出警告信息
class DeprecatedAttribute(AttributeInfo):
    def __init__(self):
        self.MarkerAttribute = None

    def readInfo(self,reader):
        pass

"""
Synthetic_attribute {
    u2 attribute_name_index;
    u4 attribute_length;
}
"""
#Synthetic属性用来标记源文件中不存在、由编译器生成的类成员，引入Synthetic属性主要是为了支持嵌套类和嵌套接口
class SyntheticAttribute(AttributeInfo):
    def __init__(self):
        self.MarkerAttribute = None

    def readInfo(self,reader):
        pass


"""
Exceptions_attribute {
    u2 attribute_name_index;
    u4 attribute_length;
    u2 number_of_exceptions;
    u2 exception_index_table[number_of_exceptions];
}
"""
#Exceptions是变长属性，记录方法抛出的异常表
class ExceptionsAttribute(AttributeInfo):
    def __init__(self):
        self.exceptionIndexTable = None

    def readInfo(self,reader):
        self.exceptionIndexTable = reader.readUint16s()

    def ExceptionIndexTable(self):
        return self.exceptionIndexTable

"""
LocalVariableTable_attribute {
    u2 attribute_name_index;
    u4 attribute_length;
    u2 local_variable_table_length;
    {   u2 start_pc;
        u2 length;
        u2 name_index;
        u2 descriptor_index;
        u2 index;
    } local_variable_table[local_variable_table_length];
}
"""
#LocalVariableTable属性表中存放方法的局部变量信息
class LocalVariableTableAttribute(AttributeInfo):
    def __init__(self):
        self.localVariableTable = None

    def readInfo(self,reader):
        LocalVariableTableLength = reader.readUint16()
        self.localVariableTable = []
        for i in range(LocalVariableTableLength):
            l = self.LocalVariableTable()
            l.startPc = reader.readUint16()
            l.localVariable = reader.readUint16()
            self.localVariableTable.append(l)

    class LocalVariableTable(object):
        def __init__(self):
            self.startPc = None
            self.localVariable = None

"""
LineNumberTable_attribute {
    u2 attribute_name_index;
    u4 attribute_length;
    u2 line_number_table_length;
    {   u2 start_pc;
        u2 line_number;
    } line_number_table[line_number_table_length];
}
"""
#LineNumberTable属性表存放方法的行号信息
class LineNumberTableAttribute(AttributeInfo):
    def __init__(self):
        self.lineNumberTable = None

    def readInfo(self,reader):
        lineNumberTableLength = reader.readUint16()
        self.lineNumberTable = []
        for i in range(lineNumberTableLength):
            l = self.LineNumberTableEntry()
            l.startPc = reader.readUint16()
            l.lineNumber = reader.readUint16()
            self.lineNumberTable.append(l)

    class LineNumberTableEntry(object):
        def __init__(self):
            self.startPc = None
            self.lineNumber = None

"""
SourceFile_attribute {
    u2 attribute_name_index;
    u4 attribute_length;
    u2 sourcefile_index;
}
"""
#SourceFile是可选定长属性，只会出现在ClassFile结构中，用于指出源文件名
class SourceFileAttribute(AttributeInfo):
    def __init__(self,cp):
        self.cp = cp
        self.sourceFileIndex = None

    def readInfo(self, reader):
        self.sourceFileIndex = reader.readUint16()

    def FileName(self):
        return self.cp.getUtf8(self.sourceFileIndex)

"""
attribute_info {
    u2 attribute_name_index;
    u4 attribute_length;
    u1 info[attribute_length];
}
"""
class UnparsedAttribute(AttributeInfo):
    def __init__(self, attrName, attrLen):
        self.name = attrName
        self.length = attrLen
        self.info = None

    def readInfo(self, reader):
        self.info = reader.readBytes(self.length)