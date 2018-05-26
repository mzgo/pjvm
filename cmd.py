import argparse
import os
import sys

parser = argparse.ArgumentParser()


class CMD(object):
    def __init__(self):
        self.helpFlag = False
        self.versionFlag = False
        self.cpOption = ""
        self.XjreOption = ""
        self.Class = ""
        self.args = []


def printUsage():
    print("Usage: %s [-options] class [args...]\n" % sys.argv[0])


def parseCMD():
    cmd = CMD()

    # 添加命令行参数解析规则
    parser.add_argument('-help', default=False, help='print help message', action="store_true")
    parser.add_argument('-version', default=False, help='print version and exit', action="store_true")
    parser.add_argument('-classpath', default="", help='classpath')
    parser.add_argument('-Xjre', default="", help='path to jre')

    # 解析参数 argv是未定义的不定参数
    args, argv = parser.parse_known_args(None, None)

    if len(argv) > 0:
        cmd.Class = argv[0]
        cmd.args = argv[1:]

    cmd.helpFlag = args.help
    cmd.versionFlag = args.version
    cmd.cpOption = args.classpath
    return cmd


# 打印对象所有属性
def prn_obj(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))