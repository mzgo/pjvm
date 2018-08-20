from instructions.base.instruction import NoOperandsInstruction


class FCMPG(NoOperandsInstruction):
    def execute(self, frame):
        _fcmp(frame, True)


class FCMPL(NoOperandsInstruction):
    def execute(self, frame):
        _fcmp(frame, False)


class DCMPG(FCMPG):
    pass


class DCMPL(FCMPL):
    pass


def _fcmp(frame, gFlag):
    stack = frame.operandStack
    v2 = stack.pop()
    v1 = stack.pop()
    if v1 > v2:
        stack.push(1)
    elif v1 == v2:
        stack.push(0)
    elif v1 < v2:
        stack.push(-1)
    elif gFlag:
        stack.push(1)
    else:
        stack.push(-1)
