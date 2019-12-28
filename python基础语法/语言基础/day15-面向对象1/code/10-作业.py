"""__author__=桃花寓酒寓美人"""
# 4.创建⼀一个学⽣生类:
# 属性:姓名，年龄，学号
# 方法:答到，展示学⽣生信息
# 创建⼀一个班级类:
# 属性:学⽣生，班级名
# 方法:添加学⽣生，删除学生，点名, 求班上学生的平均年龄


class Student:

    def __init__(self, name, age, student_number):
        self.name = name
        self.age = age
        self.student_number = student_number

    def sign_in(self):
        print('姓名：%s 年龄：%s 学号：%s' % (self.name, self.age, self.student_number))


class Class:

    def __init__(self, student_name, class_name):
        self.student_name = student_name
        self.class_name = class_name

    def add_student(self):


