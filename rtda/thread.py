from rtda.jvm_stack import Stack


class Thread(object):

    def __init__(self):
        self.pc = None #int
        self.stack = Stack(1024) # *Stack

    def PushFrame(self,frame):
        self.stack.push(frame)

    def PopFrame(self):
        return self.stack.pop()

    def CurrentFrame(self):
        return self.stack.top()