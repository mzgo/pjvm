from classpaths.classpath import Parse

from cmd import parseCMD, printUsage


def startJVM(cmd):
    cp = Parse(cmd.XjreOption, cmd.cpOption)
    print("classpath:%s class:%s args:%s\n" % (cp.String(), cmd.Class, cmd.args))
    className = cmd.Class.replace(".", "/", -1)
    classData = cp.ReadClass(className)
    if (classData == None):
        print("Could not find or load main class %s\n" % cmd.Class)
    print("class data:%s\n" % classData)


def main():
    cmd = parseCMD()
    if cmd.versionFlag:
        print("version 0.0.1")
    elif cmd.helpFlag or cmd.Class == "":
        printUsage()
    else:
        startJVM(cmd)

main()
