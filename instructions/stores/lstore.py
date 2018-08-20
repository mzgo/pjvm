from instructions.base.instruction import Index8Instruction, NoOperandsInstruction


class LSTORE(Index8Instruction):
    def execute(self, frame):
        _lstore(frame, self.index)


class LSTORE_0(NoOperandsInstruction):
    def execute(self, frame):
        _lstore(frame, 0)


class LSTORE_1(NoOperandsInstruction):
    def execute(self, frame):
        _lstore(frame, 1)


class LSTORE_2(NoOperandsInstruction):
    def execute(self, frame):
        _lstore(frame, 2)


class LSTORE_3(NoOperandsInstruction):
    def execute(self, frame):
        _lstore(frame, 3)


def _lstore(frame, index):
    val = frame.operandStack.pop()
    frame.localVars.setIndex(index, val)
