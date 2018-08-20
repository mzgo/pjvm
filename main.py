from classpaths.classpath import Parse
from cmd import parseCMD, printUsage
from classfile.class_file import *
from rtda.frame import Frame


def startJVM(cmd):
    # cp = Parse(cmd.XjreOption, cmd.cpOption)
    # className = cmd.Class.replace(".", "/", -1)
    # classData = cp.ReadClass(className)
    # if (classData == None):
    #     print("错误 : startJVM : 找不到或无法加载主类 %s\n" % cmd.Class)
    #
    # cf = parse(classData)
    # printClassInfo(cf)

    frame = Frame(100,100)
    testLocalVars(frame.localVars)
    testOperandStack(frame.operandStack)

def testLocalVars(vars):
    vars.setIndex(0, 100)
    vars.setIndex(1, -100)
    vars.setIndex(2, 2997924580)
    vars.setIndex(4, -2997924580)
    vars.setIndex(6, 3.1415926)
    vars.setIndex(7, 2.71828182845)
    vars.setIndex(9, None)

    print(vars.getIndex(0))
    print(vars.getIndex(1))
    print(vars.getIndex(2))
    print(vars.getIndex(4))
    print(vars.getIndex(6))
    print(vars.getIndex(7))
    print(vars.getIndex(9))

def testOperandStack(ops):
    ops.push(100)
    ops.push(-100)
    ops.push(2997924580)
    ops.push(-2997924580)
    ops.push(3.1415926)
    ops.push(2.71828182845)
    ops.push(None)

    print(ops.pop())
    print(ops.pop())
    print(ops.pop())
    print(ops.pop())
    print(ops.pop())
    print(ops.pop())
    print(ops.pop())



def printClassInfo(cf):
    print("version: %s %s" % (cf.majorVersion, cf.minorVersion))
    print("constants count: %s" % len(cf.constantPool.data))
    print("access flags: 0x%x" % cf.accessFlags)
    print("this class: %s" % cf.ClassName())
    print("super class: %s" % cf.SuperClassName())
    print("interfaces: %s" % cf.InterfaceNames())
    print("fields count: %s" % len(cf.fields))

    for i in cf.fields:
        print(" %s " % i.Name())

    for i in cf.methods:
        print(" %s " % i.Name())


def main():
    cmd = parseCMD()
    if cmd.versionFlag:
        print("版本号 ： 0.0.1")
    elif cmd.helpFlag or cmd.Class == "":
        printUsage()
    else:
        startJVM(cmd)

main()
