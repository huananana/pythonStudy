"""__author__=桃花寓酒寓美人"""

# 1.什么是生成器
"""
生成器就是迭代器中的一种 - 但它是自己生产数据(当程序需要它才会产生数据，之间是没有数据)
生成器作为容器它保存的不是数据，而是产生数据的算法
"""

# **2.怎么创建生成器
"""
调用带有yield的关键字的函数，就可以得到一个生成器(只有一种创建方式)
**注意：函数只要存在关键字yield无论yield在何方，这个函数都是一个生成器
"""


def func1():
    print('====')
    print('++++')
    yield


re = func1()    # 生成器
print(re)   # <generator object func1 at 0x000001F36244D448>

# 3.生成器怎么产生数据（怎么确定生成器中的元素）
"""
生成器能产生数据和类型，看执行完成生成器会遇到几次yield
遇到几次yield就可以产生多个数据，每次遇到，yield，yield后面的数据就是产生的元素
"""


def func2():
    yield 10
    yield 100
    yield 1000


gen1 = func2()
for x in gen1:
    print('x:', x)

# 4.生成器产生数据的规律
"""
生成器对应的函数执行条件，当生成器遇到程序

第一次索要数据的指令时，生成器会执行函数找到第一个yield
并在此函数停止并记录位置，将数据传出

第二次程序索要数据时，生成器在上一次停止位置继续向下运行，
找到下一份yield停止函数，记录位置，将数据传出

...

直到程序再次索要数据，生成器函数向下再也找不到yield时，程序报错StopIteration
"""


# 例子：YYYYYYYYYYYYYYY

def func3(n):
    for _ in range(n):
        yield 100


gen3 = func3(4)
next(gen3)
for x in gen3:
    print('x:', x)


def func4(n):
    for x in range(1, n+1):
        yield x*x


gen4 = func4(4)
print(next(gen4))


# 练习：写一个生成器，能后产生一个班所有学生的学号，班级人数自己定
def student_number(pre: str, n):
    length = len(str(n))
    for x in range(1, n+1):
        yield pre + str(x).zfill(length)


gen = student_number('python1906', 100)
for x in gen:
    print('student_number:', x)
