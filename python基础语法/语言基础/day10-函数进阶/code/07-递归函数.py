"""__author__=桃花寓酒寓美人"""

# 1.什么是递归函数
"""
声明函数的时候调用函数本身，这样的函数就是递归函数(自己调用自己)
递归可以实现循环效果，原则上除了死循环，其它的循环递归都可以实现(占内存)
递归思路：从后往前思考
    1.列出开头的终止语句
    2.列出f(n)与f(n-1)...之间的函数关系
    3.递归就完成了
缺点：占内存
优点：对一些复杂循环，可以实现缩减代码量
建议：一般不用，高手
"""


# 无限循环
def func1():
    print('=')
    func1()


# 2.递归怎么用
"""
使用递归的套路：
a.设置临界值 - 循环结束的条件(保证函数结束)
b.找关系 - 找f(n) 和 f(n-1)的关系
c.假设函数的功能已经实现，通过f(n-1)去实现f(n)的功能

"""


# 递归：计算1+2+3+4+...+100
def func(n):
    # 找临界值
    if n == 1:
        return 1
    # 判断关系
    return n + func(n-1)


print(func(100))


# 斐波那契
def fibonacci(n):
    """

    :param n:
    :return:
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))


# 练习：
"""
n = 4
*
**
***
****
"""


def xx(n):
    if n == 1:
        print('*')
        return
    # 关系：实现f(n-1)的功能后，在打印一行n个*
    xx(n-1)
    print(n*'*')


xx(4)
n = 5
print(n*'*')
