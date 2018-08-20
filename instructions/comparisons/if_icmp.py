from instructions.base.branch_logic import branch
from instructions.base.instruction import BranchInstruction


def _icmpPop(frame):
    stack = frame.operandStack
    val2 = stack.pop()
    val1 = stack.pop()
    return val1, val2


class IF_ICMPEQ(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 == val2:
            branch(frame, self.offset)


class IF_ICMPNE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 != val2:
            branch(frame, self.offset)


class IF_ICMPLT(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 < val2:
            branch(frame, self.offset)


class IF_ICMPLE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 <= val2:
            branch(frame, self.offset)


class IF_ICMPGT(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 > val2:
            branch(frame, self.offset)


class IF_ICMPGE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 >= val2:
            branch(frame, self.offset)
