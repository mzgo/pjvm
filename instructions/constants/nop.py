from instructions.base.instruction import NoOperandsInstruction


class NOP(NoOperandsInstruction):
    def execute(self, frame):
        pass
