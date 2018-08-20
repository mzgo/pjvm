from instructions.base.instruction import NoOperandsInstruction


class IAND(NoOperandsInstruction):
    def execute(self,frame):
        stack = frame.operandStack
        v2 = stack.pop()
        v1 = stack.pop()
        result = v1 and v2
        stack.push(result)

class LAND(IAND):
    pass

