# coding=utf-8
import types


def getName():
    return "FanBingyang"


def printName(obj):
    print("输出参数类型：", type(obj))
    instance = isinstance(obj, types.FunctionType)
    print("参数是否是函数：", instance)
    strl = ""
    if instance:
        print("参数是函数，调用函数")
        strl = obj()
        print("调用参数函数结果：", strl)
    else:
        print("参数不是函数，取当前参数值——函数返回值")
        strl = obj
        print("取参数值结果：", strl)


if __name__ == "__main__":
    # 函数作为参数
    print('函数作为参数：getName')
    printName(getName)
    print("----------")
    # 函数返回值作为参数
    print('函数返回值作为参数：getName()')
    printName(getName())
