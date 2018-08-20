from instructions.base.instruction import NoOperandsInstruction


class DREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        v2 = stack.pop()
        v1 = stack.pop()
        result = v1 % v2
        stack.push(result)


class FREM(DREM):
    pass


class IREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        v2 = stack.pop()
        v1 = stack.pop()
        if v2 == 0:
            print("java.lang.ArithmeticException: / by zero")
            exit()
        result = v1 % v2
        stack.push(result)


class LREM(IREM):
    pass
