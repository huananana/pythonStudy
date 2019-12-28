"""__author__=桃花寓酒寓美人"""

# 1.类中的属性 - 就是类中保存数据的变量
"""
类中的属性分为两种：字段、对象属性
"""

# 2.字段
"""
1）怎么声明：直接声明在类中函数外的变量就是字段
2）怎么使用：通过类使用；以“类.字段”
3）什么时候用：不会因为对象不同而不一样的属性就声明成对象属性
"""


# 2.对象属性
"""
1）怎么声明：
声明在__init__方法中；以“self.属性名=值”的形式来声明

2）怎么使用：通过对象来使用；以’对象.属性‘的形式来使用

3）什么时候用：会因为对象不同而不一样的属性就声明成对象属性
               例如：人类，每个对象的名字就是对象属性
"""


class Person:
    # a就是字段
    a = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('诸葛卧龙', 1800)
print(p1.name, p1.age)


class Student:
    def __init__(self, name, s=0):
        self.name = name
        self.age = 18
        self.score = s


s1 = Student('周郎')
print(s1.name)

# 声明一个狗类，拥有属性：品种、名字、颜色、年龄、性别；功能吃(XXX吃XXX)


class Dog:
    def __init__(self, name, color='黄色', gender="公", breed='土狗'):
        self.breed = breed
        self.name = name
        self.color = color
        self.gender = gender

    def eat(self, food: str):

        print('%s在吃%s' % (self.name, food))


dog1 = Dog('大黄')
dog2 = Dog('财财', color='黑色')

dog1.eat('肉')
dog2.eat('骨头')
