"""__author__=桃花寓酒寓美人"""
import time
# 1.什么是装饰器
"""
装饰器本质是一个函数 = 返回值高阶函数+实参高阶函数+糖语法
装饰器是python的三大神器之一：装饰器、迭代器、生成器
作用：给已经写好的函数添加新的功能
"""


# 给函数添加一个功能：统计函数的执行时间
# 方法一：在每个需要添加功能的函数中加入相应代码
def yt_sum(x, y):
    start = time.time()  # 获取当前时间
    sum1 = x + y
    print(sum1)
    end = time.time()
    print('函数执行时间：%fs' % (end - start))


yt_sum(100, 200)


def factoeial(n):
    start = time.time()
    sum1 = 1
    for num in range(1, n+1):
        sum1 *= num
    print('%d的阶乘是：%d' % (n, sum1))


# 方法二：注意：这个add_time只能给没有参数的函数添加统计执行时间的功能
def add_time(fn):
    start = time.time()
    fn()
    end = time.time()
    print('函数执行时间：%fs' % (end - start))


def add_time2(fn, *args, **kwargs):
    start = time.time()
    fn(*args, **kwargs)
    end = time.time()
    print('函数执行时间：%fs' % (end - start))


def func1():
    print('===========')
    print('+++++++++++')


def func2():
    print('asdfasdf!')
    print('asdaafasdfsadfasdfasdfasdf')


add_time(func1)
add_time(func2)

print('============装饰器============')
# 2.装饰器
"""
无参装饰器的函数：
def 函数名1(参数1):
    def函数名2(*args, **kwargs):
        参数1(*args, **kwargs)
        新功能对应的代码段
    return 函数名2

说明：
函数名1 - 装饰器的名字；一般根据需要添加的功能命名
参数1 - 需要添加功能的函数， 一般为fn
函数名2 - 随便命名，可以用test
"""


# 添加统计函数执行时间的装饰器对应的函数
def add_time3(fn):
    def test(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print('函数执行时间：%fs' % (end - start))
    return test


@add_time3
def func5(x, y):
    print('start %d')
    print(x+y)


func5(19, 129)


# 练习：给所有的返回值是整数的函数添加功能：返回值以16进制形式的数据返回
def add_hex(fn):
    def test(*args, **kwargs):
        re = fn(*args, **kwargs)
        # if type(re) == int:
        # 判断re是否是整型
        if isinstance(re, int):
            return hex(re)
        return re
    return test


@add_hex
def yt_sum(x, y):
    return x+y


print(yt_sum(1, 2))
