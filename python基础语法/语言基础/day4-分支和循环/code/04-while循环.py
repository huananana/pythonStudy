import random
from random import randint

# 1.while循环
""
"""
1)语法：
while 条件语句 :
    循环体
#--细节：和if语句类似

2)说明
while ---- 关键字，固定写法
条件语句 - 任何有结果的表达式，数据、已经声明过的变量、运算符表达式(不能是赋值语句等)
: -------- 关键字，固定写法
循环体 --- 和while保持一个缩进的一条或者多条语句；(需要重复指定的语句)

3)执行过程:
先判断条件语句是否为True,如果为True就执行循环体；执行完循环体在判断条件语句是否为True，
为True又执行循环体，以此类推，知道条件语句的结果是False循环就结束
"""

# for循环和while的选择

"""
1)什么时候使用for循环
a.循环次数确定的时候
b.遍历序列

2)什么时候使用while循环
a.死循环
b.循环次数不确定
"""

# 不断输入数字，直到输入0为止
button = 1
while button != 0:
    button = int(input(">>>"))

# 练习:猜数字
# 游戏开始随机产生100以内一个数字，猜对游戏结束
# 给出提示，太大或太小
# 方法1：
number = randint(0, 100)
value = -1
while value != number:
    value = int(input(">>>"))
    if value < number:
        print("小了")
    elif value > number:
        print("大了")
print("游戏结束！", number, value)

# 方法2：
button = 0
lucky = randint(0, 100)  # 产生0，100的随机数，并且保存在lucky
while True:
    print(lucky)
    value = int(input(">>>"))
    if lucky > value:
        print("太小")
    elif lucky < value:
        print("太大")
    else:
        print("正确")
        break
