# 1.注释
# 代码中参与编译执行的文字（不影响程序功能的文字）就叫注释；专门用来对代码进行注解和说明的
# python中单行注释就是再一行文字前加#
# python中的多行注释是：'''注释'''
'''
多行注释1
多行注释2
多行注释3
...

'''

# 2.语句（一行一行的代码）
# 一条语句占一行，一条语句借宿后可以不写分号
# 如果一行中需要些多条语句，语句之间必须加分号

# 3.缩进
# Python中一条语句的开头不能随便加缩进（tab）或者空格

# 4.标识符
# 标识符是专门用来给变量，函数或者类等命名的
# 标识符的要求：由字母、数字或_组成；数字不能开头（汉字、日语、汉语等也可以作为标识符）

# 5.关键字
# 在Python中有特殊功能或意义的标识符就是关键字，又叫保留字
# 33个关键字：['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

import keyword
print(keyword.kwlist)

# 6.常用数据
# 1）数字数据：用来表示大小的数据就是数字数据，在程序中直接写，
#                   例如：2e3 = 2*10**3； j**2 = -1 ;
# 2）文本数据：文本信息对应的数据，在程序中需要用单引号或者双引号引起来
# 3）布尔数据：肯定-True否定-Flash
print(True)

# 7.常用的数字类型 - 通过不同的数据类型对数据进行分类
# 整形（int） - 包含所有的整数
# 浮点型（float）- 包含所有的小数
# 负数（）
# 字符串（str） - 文本数据类型
# 布尔类型（bool） - True和Flash对应的数据类型
# 其他：列表（list）、字典（dict）、元组（tuple）、集合（set)、字节（bytes)、迭代器（iter)、函数（function）等
# type（数据） - 获取数据对应的类型

# 8.输入和输出函数
# 1)输出函数：print（）
# print(数据) - 在控制台中打印指定数据
# print（表达式） - 打印表达式的结果
# print（表达式1表达式2表达式3...） - 在一行同时打印多个表达式的结果

# a.定制换行
# 默认情况下，一份print中的内容会在一行打印。
print('hello world',end=';')
print('你好世界！')

# b.定制分割
# 默认情况下，一个print打印多分内容的时候，多和内容之间用空格隔开
print(1,2,3,4)
print(1,2,3,4,sep='')

# 2）输入函数：input（）
# input(输入提示信息)
age = input('请输入你的年龄：')
print('age的值是%s'%age)




