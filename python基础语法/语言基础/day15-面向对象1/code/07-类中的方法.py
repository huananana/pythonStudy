"""__author__=桃花寓酒寓美人"""

# 1.类中的方法
"""
类中的方法有3中：对象方法、类方法、静态方法

1）对象方法
a.怎么声明：直接生命在类中的函数
b.怎么调用：通过对象来调用
c.特点：自带一个参数self；self在调用的时候不用传参，指向当前对象
        self -> 当前对象
d.什么时候用：如果实现函数的功能需要用到对象属性，这个函数就声明成对象方法

2）类方法
a.怎么声明：在函数声明前加@classmethod
b.怎么调用：通过类来调用
c.特点：自带一个参数cls；cls在调用的时候不用传参，系统会自动将当前类传给cls
        cls -> 当前类(当前类能做的事情cls都可以做
d.什么时候用：实现函数的功能不需要对象属性的前提下，需要类

3）静态方法
a.怎么声明：在声明函数前加@staticmethod
b.怎么调用：通过类来调用
c.特点：没有自带的参数
d.什么时候用：实现函数的功能不需要对象属性的前提下，也不需要类

"""


class Student:
    num = 200

    def __init__(self, name, tel, age=18):
        self.name = name
        self.age = age
        self.tel = tel

    def study(self):
        print('%s在学习' % self.name)

    @classmethod
    def func1(cls):
        print(cls)
        print('类方法func1')
        stu2 = cls('小花', '112', 20)
        print('stu2:', stu2)
        print(Student.num)
        # cls可以使用类的字段
        print(cls.num)

    @staticmethod
    def func2():
        print('静态方法func2')

    # def __repr__(self):
    #     return "<class '%s.%s'>" % (self.__module__, self.__class__.__name__)


stu = Student('小明', '110')
stu.study()
print('stu:', stu)

print('Student:', Student)
Student.func1()

Student.func2()


class Keng:
    num1 = 100

    def func1(self):
        print('坑中的对象方法', self)

    @classmethod
    def func2(cls):
        print('坑中的类方法', cls)

    @staticmethod
    def func3():
        print('坑中的静态方法')


# 注意：理论上类中的所有方法都可以通过对象过着类调用
# 类调用对象方法
Keng.func1(100)  # 用类调用对象方法self会失去意义

k = Keng()
k.func2()       # 用对象调用类方法是多次一举，cls还是当前类
Keng.func2()

k.func3()
Keng.func3()
