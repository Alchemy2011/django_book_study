# -*- coding: utf-8 -*-
# __author__ = 'liqirong'


# 第九步：装饰器带类参数，并分拆公共类到其他py文件中，
# 同时演示了对一个函数应用多个装饰器
# 示例9: 装饰器带类参数，并分拆公共类到其他py文件中
# 同时演示了对一个函数应用多个装饰器
# 多个装饰器有点复杂，但是本质上还是装饰器。还没悟透
class Locker:
    def __init__(self):
        print("Locker.__init__() called.")

    @staticmethod
    def acquire():
        print("Locker.acquire() called.")

    @staticmethod
    def unlock():
        print("    Locker.unlock() called.")


class LockerEx(Locker):
    @staticmethod
    def acquire():
        print("LockerEx.acquire() called.")

    @staticmethod
    def unlock():
        print("    LockerEx.unlock() called.")


def lock_helper(cls):
    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()

        return __deco

    return _deco
# 如果分拆公共类到其他的py文件中，那么需要以下代码引入
# from my_locker import *


class Example:
    @lock_helper(Locker)
    def my_func(self):
        print("my_func() called.")

    @lock_helper(Locker)
    @lock_helper(LockerEx)
    def my_func2(self, a, b):
        print("my_fuc2() called.")
        return a + b


if __name__ == '__main__':
    egg = Example()
    egg.my_func()
    print(egg.my_func())
    print(egg.my_func2(1, 2))
    print(egg.my_func2(3, 4))

'''
# 第八步：让装饰器带 类 参数
# 示例8: 装饰器带类参数
# Python中一切皆对象，所以类名可以直接当参数
# 为了不调用初始化方法，所以需要使用staticmethod
# 其实使用@classmethod也可以，只不过需要修改方法中的参数
class Locker:
    def __init__(self):
        print("Locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        print("Locker.require() called. (这是静态方法)")

    @staticmethod
    def release():
        print("    Locker.release() called. (不需要对象实例)")


def deco(cls):
    """cls 必须实现acquire和release静态方法"""
    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                ret = func(*args, **kwargs)
                print("    after %s classed [%s]." % (func.__name__, cls))
                return ret
            finally:
                cls.release()
        return __deco
    return _deco


@deco(Locker)
def my_func(a, b):
    print("my_func() called.")
    return a + b


@deco(Locker)
def my_func2(a, b, c):
    print("my_func2() called.")
    return a + b + c

if __name__ == '__main__':
    my_func(1, 2)
    my_func(3, 4)
    my_func2(1, 2, 3)
    my_func2(3, 4, 5)
'''

"""
# 第七步：让装饰器带参数
# 示例7: 在示例4的基础上，让装饰器带参数，
# 和上一示例相比在外层多了一层包装。
# 装饰函数名实际上应更有意义些
# 让装饰器带参数，需要再增加一层包装，最外层传装饰器的参数，
# 中间层传被装饰函数名，最里层传被装饰函数的参数。
def deco(arg):
    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called [%s]." % (func.__name__, arg))
            ret = func(*args, **kwargs)
            print("    after %s called [%s]." % (func.__name__, arg))
            return ret
        return __deco
    return _deco


@deco("my_module")
def my_func(a, b):
    print("my_func() called.")
    return a + b


@deco("module2")
def my_func2(a, b, c):
    print("my_func2() called.")
    return a + b + c


if __name__ == '__main__':
    my_func(1, 2)
    my_func(3, 4)
    my_func2(1, 2, 3)
    my_func2(3, 4, 5)
"""

"""
# 第六步：对参数数量不确定的函数进行装饰
# 示例6: 对参数数量不确定的函数进行装饰，
# 参数用(*args, **kwargs)，自动适应变参和命名参数
# 所谓的参数不确定，是因为装饰的函数的参数不确定引起的
# 但是被装饰的函数，参数是确定的
def deco(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("    after %s called." % func.__name__)
        return ret

    return _deco


@deco
def my_func(a, b):
    print("my_func(%s,%s) called." % (a, b))
    return a + b


@deco
def my_func2(a, b, c):
    print("my_func2(%s,%s,%s) called." % (a, b, c))
    return a + b + c


if __name__ == '__main__':
    my_func(1, 2)
    my_func(3, 4)
    my_func2(1, 2, 3)
    my_func2(3, 4, 5)
"""

"""
# 第五步：对带参数的函数进行装饰
# 示例5: 对带参数的函数进行装饰，
# 内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
# 带参数的函数，参数必须往内嵌的包装函数中传，否则找不到
def deco(func):
    def _deco(a, b):
        print("before my_func() called.")
        ret = func(a, b)
        print("    after my_func() called.")
        return ret

    return _deco


@deco
def my_func(a, b):
    print("my_func(%s,%s) called." % (a, b))
    return a + b


if __name__ == '__main__':
    my_func(1, 2)
    my_func(3, 4)
"""

"""
# 第四步：使用内嵌包装函数来确保每次新函数都被调用
# 示例4: 使用内嵌包装函数来确保每次新函数都被调用，
# 内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
def deco(func):
    def _deco():
        print("before my_func() called.")
        func()
        print("    after my_func() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco


@deco
def my_func():
    print("my_func() called.")
    return 'ok'


if __name__ == '__main__':
    my_func()
    my_func()
"""

"""
# 使用语法糖@来装饰函数
# 示例3: 使用语法糖@来装饰函数，相当于“my_func = deco(my_func)”
# 但发现新函数只在第一次被调用，且原函数多调用了一次
# 返回原函数不对，应该返回被装饰后的结果。
# 如何确保新增的功能每次都被调用，就需要将执行的状态保存下来
# 如何保存？理论上，应该通过封装实现，所以需要再引入一个函数
# 解决方案，嵌套函数
def deco(func):
    print("before my_func() called.")
    func()
    print("    after my_func() called.")
    return func


@deco
def my_func():
    print("my_func called.")


if __name__ == '__main__':
    my_func()
    my_func()
"""

"""
# 第二步：使用装饰函数在函数执行前和执行后分别附加额外功能
# 示例2: 替换函数(装饰)
# 装饰函数的参数是被装饰的函数对象，返回原函数对象
# 装饰的实质语句: my_func = deco(my_func)
def deco(func):
    print("before my_func() called.")
    func()
    print("    after my_func() called.")
    return func


def my_func():
    print("my_func() called.")


if __name__ == '__main__':
    # 调用deco函数后，又将返回值传给了变量my_func
    my_func = deco(my_func)
    my_func()
    my_func()
"""

"""
# 第一步：最简单的函数，准备附加额外功能
# 示例1: 最简单的函数,表示调用了两次
# 调用两次的目的，一致性测试
def my_func():
    print("my_func() called.")


if __name__ == '__main__':
    my_func()
    my_func()
"""
