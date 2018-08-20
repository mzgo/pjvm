from instructions.base.branch_logic import branch
from instructions.base.instruction import BranchInstruction


class IFEQ(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop()
        if val == 0:
            branch(frame, self.offset)


class IFNE(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop()
        if val != 0:
            branch(frame, self.offset)


class IFLT(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop()
        if val < 0:
            branch(frame, self.offset)


class IFLE(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop()
        if val <= 0:
            branch(frame, self.offset)


class IFGT(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop()
        if val > 0:
            branch(frame, self.offset)


class IFGE(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop()
        if val >= 0:
            branch(frame, self.offset)
