from cmd import parseCMD, printUsage


def startJVM(cmd):
    print("classpath:%s class:%s args:%s\n" % (cmd.cpOption, cmd.Class, cmd.args))


def main():
    cmd = parseCMD()
    if cmd.versionFlag:
        print("version 0.0.1")
    elif cmd.helpFlag or cmd.Class == "":
        printUsage()
    else:
        startJVM(cmd)

main()
