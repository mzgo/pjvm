from instructions.base.instruction import Index8Instruction, NoOperandsInstruction


class ILOAD(Index8Instruction):
    def execute(self,frame):
        _iload(frame,self.index)

class ILOAD_0(NoOperandsInstruction):
    def execute(self,frame):
        _iload(frame,0)

class ILOAD_1(NoOperandsInstruction):
    def execute(self,frame):
        _iload(frame,1)

class ILOAD_2(NoOperandsInstruction):
    def execute(self,frame):
        _iload(frame,2)

class ILOAD_3(NoOperandsInstruction):
    def execute(self,frame):
        _iload(frame,3)

def _iload(frame,index):
    val = frame.localVars.getIndex(index)
    frame.operandStack.push(val)