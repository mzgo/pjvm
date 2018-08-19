from classpaths.classpath import Parse
from cmd import parseCMD, printUsage
from classfile.class_file import *


def startJVM(cmd):
    cp = Parse(cmd.XjreOption, cmd.cpOption)
    className = cmd.Class.replace(".", "/", -1)
    classData = cp.ReadClass(className)
    if (classData == None):
        print("错误 : startJVM : 找不到或无法加载主类 %s\n" % cmd.Class)

    cf = parse(classData)
    printClassInfo(cf)


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
