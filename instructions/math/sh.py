import struct

from instructions.base.instruction import NoOperandsInstruction


class ISHL(NoOperandsInstruction):
    def execute(self,frame):
        stack = frame.operandStack
        v2 = stack.pop()
        v1 = stack.pop()
        s = struct.unpack('>I', struct.pack('>i',v2))[0] & 0x1f
        result = v1 << s
        stack.push(result)

class ISHR(NoOperandsInstruction):
    def execute(self,frame):
        stack = frame.operandStack
        v2 = stack.pop()
        v1 = stack.pop()
        s = struct.unpack('>I', struct.pack('>i', v2))[0] & 0x1f
        result = v1 >> s
        stack.push(result)

class IUSHR(NoOperandsInstruction):
    def execute(self,frame):
        stack = frame.operandStack
        v2 = stack.pop()
        v1 = stack.pop()
        s = struct.unpack('>I', struct.pack('>i', v2))[0] & 0x1f
        v1 = struct.unpack('>I', struct.pack('>i', v1))[0]
        result = v1 >> s
        result = struct.unpack('>i', struct.pack('>I', result))[0]
        stack.push(result)

class LSHL(NoOperandsInstruction):
    def execute(self,frame):
        stack = frame.operandStack
        v2 = stack.pop()
        v1 = stack.pop()
        s = struct.unpack('>I', struct.pack('>i',v2))[0] & 0x3f
        result = v1 << s
        stack.push(result)

class LSHR(NoOperandsInstruction):
    def execute(self,frame):
        stack = frame.operandStack
        v2 = stack.pop()
        v1 = stack.pop()
        s = struct.unpack('>I', struct.pack('>i', v2))[0] & 0x3f
        result = v1 >> s
        stack.push(result)

class LUSHR(NoOperandsInstruction):
    def execute(self,frame):
        stack = frame.operandStack
        v2 = stack.pop()
        v1 = stack.pop()
        s = struct.unpack('>I', struct.pack('>i', v2))[0] & 0x3f
        v1 = struct.unpack('>I', struct.pack('>i', v1))[0]
        result = v1 >> s
        result = struct.unpack('>i', struct.pack('>I', result))[0]
        stack.push(result)

