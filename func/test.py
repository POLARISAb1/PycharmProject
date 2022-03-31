# coding=utf-8

def A():
    print(12345)


def B(obj):
    print(obj, type(obj))


if __name__ == '__main__':
    B(A)  # A是一个函数，传入B
    print('--'*50)
    B(A())  # A()是一个调用，传入B中
