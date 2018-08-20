from rtda.local_vars import LocalVars
from rtda.operand_stack import OperandStack


class Frame(object):

    def __init__(self,maxLocals,maxStack):
        self.localVars = LocalVars(maxLocals) # LocalVars
        self.operandStack = OperandStack(maxStack) # * OperandStack


