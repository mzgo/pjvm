class Stack(object):

    def __init__(self, maxSize):
        self.maxSize = maxSize  # uint
        self.SIZE = None  # uint
        self._top = None  # * Frame

    def push(self, frame):
        if self.SIZE >= self.maxSize:
            print("错误 : jvm_stack : java.lang.StackOverflowError")
            exit()

        if self._top != None:
            frame.lower = self._top

        self._top = frame
        self.SIZE += 1

    def pop(self):
        if self._top == None :
            print("错误 : jvm_stack : 栈空！")
            exit()

        top = self._top
        self._top = top.lower
        top.lower = None
        self.SIZE -= 1
        return top

    def top(self):
        if self._top == None:
            print("错误 : jvm_stack : 栈空！")
            exit()
        return self._top