from instructions.base.instruction import NoOperandsInstruction


class D2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        d = stack.pop()
        stack.push(float(d))


class D2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        d = stack.pop()
        stack.push(int(d))


class D2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        d = stack.pop()
        stack.push(int(d))

