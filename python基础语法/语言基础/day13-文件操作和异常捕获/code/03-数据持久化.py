"""__author__=桃花寓酒寓美人"""

# 1.数据持久化
"""
1）需要持久化的数据要保存在文件
2）需要数据的时候不是在程序中直接给初始值，而是从本地文件中读数据
3）如果这个数据的值发生改变，要将组新的数据更新到文件中
"""

# 练习：在程序中用一个变量来记录当前程序启动次数
# 需要数据的时候读取数据
# f = open('test.txt', 'r', encoding='utf-8')
# count = int(f.read())
# print(count)
# f.read()

# 数据发生改变后更新文件
# count += 1
# f = open('test.txt', 'w', encoding='utf-8')
# f.write(str(count))
# f.close()

# 2.文件域
"""
打开指定文件，在文件作用域结束后会自动关闭文件
with open(文件路径，打开方式，编码方式) as 文件对象：
    文件作用域
"""
# with open('test.txt', 'r', encoding='utf-8') as f:
#     re = f.read()
#     print(re)

# 每次运行程序添加一个学生，要求之前添加的学生要一直存在
"""
张三
[张三]

李四
[张三, 李四]

小明
[张三, 李四, 小明]
"""
# with open('files/students.txt', 'r', encoding='utf-8') as f1:
#     students = f1.read()

# name = input('学生姓名:')
# if students == '[]':
#     # [张三]
#     students = '{}{}]'.format(students[:-1], name)
# else:
#     # [张三,李四]
#     students = '{},{}]'.format(students[:-1], name)

# print(students)

# with open('files/students.txt', 'w', encoding='utf-8') as f:
#     f.write(students)

# 3.容器字符串的转换： eval
# 怎么将字符串：'[1, 2, 3]' 转换成列表：[1, 2, 3]
re1 = eval('[1, 2, 3]')
print(re1, type(re1))

