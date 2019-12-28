"""__author__=桃花寓酒寓美人"""


class Person:
    num = 10

    def __init__(self, sex):
        self.name = '小明'
        self.age = 18
        self.sex = sex

    @staticmethod
    def func1():
        print('我是静态方法')


class Student(Person):

    def __init__(self, name, sex):
        super().__init__(sex)
        self.name = name

    @classmethod
    def func2(cls):
        print('我是类方法')


student = Student('a', 1)
student.func1()
print(student.sex)
print(student.name)
