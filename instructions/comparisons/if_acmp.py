from instructions.base.branch_logic import branch
from instructions.base.instruction import BranchInstruction


def _acmp(frame):
    stack = frame.operandStack
    ref2 = stack.pop()
    ref1 = stack.pop()
    return ref1 == ref2


class IF_ACMPEQ(BranchInstruction):
    def execute(self,frame):
        if _acmp(frame):
            branch(frame,self.offset)

class IF_ACMPNE(BranchInstruction):
    def execute(self,frame):
        if not _acmp(frame):
            branch(frame,self.offset)

