from instructions.base.instruction import NoOperandsInstruction

# push null
class ACONST_NULL(NoOperandsInstruction):
    pass

# Push double
class DCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(0.0)

class DCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(1.0)

# Push float
class FCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(0.0)

class FCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(1.0)

class FCONST_2(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(2.0)

# Push int constant
class ICONST_M1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(-1)


class ICONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(0)


class ICONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(1)


class ICONST_2(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(2)


class ICONST_3(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(3)

class ICONST_4(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(4)

class ICONST_5(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(5)

# Push long constant
class LCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(0)

class LCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push(1)
