from instructions.base.instruction import NoOperandsInstruction


class DUP(NoOperandsInstruction):
    def execute(self,frame):
        stack = frame.operandStack
        slot = stack.pop()
        stack.push(slot)
        stack.push(slot)

class DUP_X1(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.pop()
        slot2 = stack.pop()
        stack.push(slot1)
        stack.push(slot2)
        stack.push(slot1)

class DUP_X2(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.pop()
        slot2 = stack.pop()
        slot3 = stack.pop()
        stack.push(slot1)
        stack.push(slot3)
        stack.push(slot2)
        stack.push(slot1)

class DUP2(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.pop()
        slot2 = stack.pop()
        stack.push(slot2)
        stack.push(slot1)
        stack.push(slot2)
        stack.push(slot1)

class DUP2_X1(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.pop()
        slot2 = stack.pop()
        slot3 = stack.pop()
        stack.push(slot2)
        stack.push(slot1)
        stack.push(slot3)
        stack.push(slot2)
        stack.push(slot1)

class DUP2_X2(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.pop()
        slot2 = stack.pop()
        slot3 = stack.pop()
        slot4 = stack.pop()
        stack.push(slot2)
        stack.push(slot1)
        stack.push(slot4)
        stack.push(slot3)
        stack.push(slot2)
        stack.push(slot1)

