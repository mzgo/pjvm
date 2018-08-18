
from classfile.attr_constant_value import ConstantValueAttribute
from classfile.attr_exceptions import ExceptionsAttribute
from classfile.attr_line_number_table import LineNumberTableAttribute, LocalVariableTableAttribute
from classfile.attr_markers import DeprecatedAttribute, SyntheticAttribute
from classfile.attr_source_file import SourceFileAttribute
from classfile.attr_unparsed import UnparsedAttribute


class AttributeInfo(object):

    def readInfo(self,reader,cp):
        attributesCount = reader.readUint16()
        attributes = []
        for i in range(attributesCount):
            attributes.append(readAttribute(reader,cp))
        return attributes

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
        from classfile.attr_code import CodeAttribute
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