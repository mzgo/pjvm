import os

class Classpath(object):

    def __init__(self):
        from classpaths.entry import Entry
        self.bootClasspath = Entry()
        self.extClasspath = Entry()
        self.userClasspath = Entry()

    def parseBootAndExtClasspath(self, jreOption):
        jreDir = self.getJreDir(jreOption)
        jreLibPath = os.path.join(jreDir, "lib", "*")
        from classpaths.entry_wildcard import WildcardEntry
        self.bootClasspath = WildcardEntry(jreLibPath)
        jreExtPath = os.path.join(jreDir, "lib", "ext", "*")
        self.extClasspath = WildcardEntry(jreExtPath)

    def getJreDir(self, jreOption):
        if (jreOption != "" and jreOption != None and os.path.exists(jreOption)):
            return jreOption
        if (os.path.exists("./jre")):
            return "./jre"
        if (os.environ.get("JAVA_HOME") != None):
            return os.path.join(os.environ.get("JAVA_HOME"), "jre")
        print("Classpath : Can not find jre folder!")
        exit()

    def parseUserClasspath(self, cpOption):
        if (cpOption == "" or cpOption == None):
            cpOption = "."
        from classpaths.entry import newEntry
        self.userClasspath = newEntry(cpOption)

    def ReadClass(self, className):
        className = className + ".class"
        data = self.bootClasspath.readClass(className)
        if data != None:
            return data

        data = self.extClasspath.readClass(className)
        if data != None:
            return data

        return self.userClasspath.readClass(className)

    def String(self):
        return self.userClasspath.String()


def Parse(jreOption, cpOption):
    cp = Classpath()
    cp.parseBootAndExtClasspath(jreOption)
    cp.parseUserClasspath(cpOption)
    return cp