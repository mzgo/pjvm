from instructions.base.instruction import NoOperandsInstruction


class POP(NoOperandsInstruction):
    def execute(self,frame):
        frame.operandStack.pop()

class POP2(NoOperandsInstruction):
    def execute(self,frame):
        frame.operandStack.pop()
        frame.operandStack.pop()