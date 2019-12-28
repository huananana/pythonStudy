
# 1. if-elif-else结构

"""
if结构：
if 条件语句1：
    代码段1
elif 条件语句2：
    代码段2
...
else：
    代码段3
解释：条件语句为Ture，则运行代码段,(条件语句1和条件语句2...自己理解为类似地位相等，当然中止的条件是一个条件满足及结束)；如果都不满足则执行代码段3

2) 执行过程：
先判断条件语句1是否为True，为True就执行代码段1，然后整个if-elif-else结构结束；
如果为False，就判断条件语句3是否为True，为True就执行代码段3，然后整个if-elif-else结构结束
以此类推
如果所有的条件语句都不成立，就执行else后面的代码段
"""

# 示例：根据年龄范围打印：少年14-，青年15-25，壮年26-35，中年36-50，老年50-

import random
age = random.randint(0,100)
print(age)
if age < 14:
    print("少年")
elif age <= 25:   #----- 微操： 本来根据题意此处条件应该为 14 < age <= 25; 但由于if语句有承上启下的作用；说人话，就是执行到这句条件语句之前，已经包含了age>14这个条件；所以此处可以省略，以下类似
    print("青年")
elif age <= 35:
    print("壮年")
elif age <= 50:
    print("中年")
else:
    print("老年")

# 2.if嵌套
"""
if结构中的代码块中可以再出现其它的if语句
"""
#判断一个数是否是偶数，并且在判断这个数是否是4的倍数；并打印出结论
num = 16
if num & 1 == 0:
    if num % 4 == 0:
        print("偶数,且是4的倍数")
    else:
        print("偶数")
else:
    print("奇数")


num = 16
if num & 1 == 0:
    print("偶数",end=",")
    if num % 4 == 0:
        print("且是4的倍数")
else:
    print("奇数")





