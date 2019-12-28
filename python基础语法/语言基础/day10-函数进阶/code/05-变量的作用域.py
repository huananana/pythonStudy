"""__author__=桃花寓酒寓美人"""

# 1.变量的作用域 - 变量可以使用的范围
# 2.全局变量和局部变量
"""
1)全局变量
函数与类之外的地方的变量，就是全局变量(python这样定义的)；
从声明变量开始到文件结束任何地方都可以使用

2)局部变量
在函数中声明的变量，就是局部变量；
从声明开始到该函数结束可以使用(形参是声明在函数中的变量)
"""
print('================= 全局变量 ====================')
# a就是全局变量
a = 10

print('在外部：', a)

for x in range(3):
    print('循环中：', a)


def func1():
    print('在函数中', a)


for b in range(3):
    print('b也是全局变量', b)

print("================= 局部变量 ====================")


def func2(aa):
    bb = 200
    print('在函数内的局部变量', aa)

    def func3():
        cc = 300
        print('函数中的函数：', aa, bb)

    func3()
    # print('函数内部：', cc)  # NameError: name 'cc' is not defined


func2(100)
# print(aa)   # NameError: name 'aa' is not defined
# print(bb)   # NameError: name 'bb' is not defined

# 3.global和nonlocal
"""
global和nonlocal这两个关键字只能在函数体中使用

1) global
使用方法：在函数中给变量赋值前加：global 变量名
作用：在函数中声明一个全局变量

2) nonlocal
使用方法：在函数中给变量赋值前加：nonlocal 变量名
作用：在局部的局部中修改局部变量的值
"""
print("================ global的使用 =====================")
a1 = 100
b1 = 100


def func4():
    # 声明一个局部变量a1
    a1 = 200

    # 声明b1是一个全局变量
    global b1
    b1 = 200  # 修改全局变量b1的值

    # 在函数内声明一个全局变量
    global c1
    c1 = 200

    print('函数内部', a1)


func4()

# 这里使用的是全局变量a1
print('函数外部', a1, b1, c1)

print("================ nonlocal的使用 =====================")


def func5():
    a2 = 100
    b2 = 100

    def func6():
        a2 = 200
        nonlocal b2
        b2 = 200
        print('函数的函数中：', a2, b2)

    func6()
    print('函数中：', a2, b2)


func5()
