from instructions.base.instruction import NoOperandsInstruction


class SWAP(NoOperandsInstruction):
    def execute(self,frame):
        stack = frame.operandStack
        slot1 = stack.pop()
        slot2 = stack.pop()
        stack.push(slot1)
        stack.push(slot2)