class Stack(object):

    def __init__(self, maxSize):
        self.maxSize = maxSize  # uint
        self.size = 0  # uint
        self.data = []  # []Frame

    def push(self, frame):
        if self.size +1  >= self.maxSize:
            print("错误 : jvm_stack : java.lang.StackOverflowError")
            exit()

        self.data.append(frame)
        self.size = len(self.data)

    def pop(self):
        if self.size == 0 :
            print("错误 : jvm_stack : 栈空！")
            exit()

        self.size -= 1
        return self.data.pop()

    def top(self):
        if self.size == 0 :
            print("错误 : jvm_stack : 栈空！")
            exit()
        return self.data[-1]