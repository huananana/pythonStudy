"""__author__=桃花寓酒寓美人"""


# 1.变量可以作为函数的返回值
def yt_sum(x, y):
    t = x+y
    return t


yt_sum(10, 20)


# 函数可以作为函数的返回值 - 返回值高阶函数
# func1就是一个返回值高阶函数
def func1():
    def func2():
        print('function2')
    return func2


print(func1())
print('=====================')
print(func1()())


# 2.闭包 - 函数1中声明了一个函数2，并且在函数2中使用了函数1的数据，那么这个函数1就是一个闭包
# 作用(特点)：闭包函数中的数据不会因为函数调用结束而销毁
def func3():
    a = 10

    def func4():
        print(a)

    return func4


print(' ====================================================bi bao')
t = func3()
print(' ====================================================bi bao')
t()  # a 没有销毁


# 练习1：python中声明函数不会执行函数体
list1 = []
for i in range(5):
    list1.append(lambda x: x*i)

print(list1[1](2), list1[2](2), list1[3](2))


# 练习2：
def func2(seq=[]):
    seq.append(10)
    return seq


func2()
print(func2())
print(func2([1, 2]))
print(func2())




















