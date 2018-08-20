from instructions.base.instruction import NoOperandsInstruction


class LCMP(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        v2 = stack.pop()
        v1 = stack.pop()
        if v1 > v2:
            stack.push(1)
        elif v1 == v2:
            stack.push(0)
        else:
            stack.push(-1)

