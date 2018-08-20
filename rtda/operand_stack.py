class OperandStack(object):

    def __init__(self,maxStack):
        if maxStack<=0:
            print("错误 : operand_stack : maxStack必须大于零！")
            exit()
        self.data = []
        self.size = 0
        self.maxStack = maxStack


    def push(self, val):
        if self.size +1  >= self.maxStack:
            print("错误 : operand_stack : 超过最大栈约束！")
            exit()

        self.data.append(val)
        self.size = len(self.data)

    def pop(self):
        if self.size == 0 :
            print("错误 : operand_stack : 栈空！")
            exit()

        self.size -= 1
        return self.data.pop()