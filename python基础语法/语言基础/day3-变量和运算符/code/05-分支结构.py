# python代码默认情况下是从第一行开始从上往下依次执行，每一条语句都会执行
# 分支结构：某段代码是否执行看条件（if语句）

# 1.if结构 - 满足条件就执行某个操作，不满足就不执行
""""""
"""
1）语法：
if 条件语句：
    代码段
其它代码

2）说明：
if----------关键字，固定写法
条件语句----任何有结果的表达式都可以，例如：数据，已经声明过的变量，运算表达式（不能是赋值语句）等
:-----------固定写法；（一般出现：的位置，后面都会换成产生缩进）
代码段------和if保持一个缩进的一条或者多条语句；需要满足条件才执行的代码

3）执行过程
先判断条件语句的结果是否为True（如果条件语句的结果不是布尔值，就下转换成布尔再看）
如果为True就执行代码段，否则代码段不执行
"""

num = 12
if num & 1 == 0:
    print('ou s')

# 2.if-else结构 -- 满足条件执行某个操作，不满足条件的时候执行另外一个操作
"""
1）语法：
if 条件语句：
    代码段1（满足条件要执行的代码）
else：
    代码段2（不满足条件要执行的代码）

2）执行过程：
先判断条件语句是否为True，如果为True就执行代码段1，否则执行代码段2
"""

import random
age = random.randint(0,100)
# 根据年龄值的范围打印“成年”或者“未成年”
print(age)
if age >= 18:
    print('成年')
else:
    print('未成年')

a = int('123')
print(type(a))

import random
num = random.randint(0,100)
num = 21
if num % 3 == 0 and num % 7 == 0:
    print('%d 能同时被3和7整除'%num)
else:
    print('%d 不能能同时被3和7整除'%num)

num = 60
if num % 3 != 0 or num % 7 != 0:
    print("%d能够被3或者7整除且不能同时被3或者7整除"%num)
else:
    print("%d不满足：能够被3或者7整除且不能同时被3或者7整除"%num)



# value  = input('请输入年：')
# year = int(value)
# if year % 4 == 0 and year % 100 != 0:
#     print('闰年')
# else:
#     print('不是闰年')


time = 15000
h = time//60//60
min = time%3600//60
second = time%3600%60
print('%d时'%h+'%d分'%min+'%d秒'%second)

print(bin(54))

weight = float(input('体重>>>'))
height = float(input('身高>>>'))
standard = weight/height**2
if 18.5<standard<24.9 :
    print('正常%f'%standard)
else:
    print('bu正常%f'%standard)
