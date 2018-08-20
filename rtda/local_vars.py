class LocalVars(object):

    def __init__(self,maxLocals):
        if maxLocals <=0 :
            print("错误 : local_vars : maxLocals必须大于零！")
            exit()
        self.data = [0 for i in range(maxLocals)]

    def setIndex(self,index,val):
        self.data[index] = val

    def getIndex(self,index):
        return self.data[index]