"""__author__=桃花寓酒寓美人"""

# 1.init方法和构造方法
"""
1) 构造函数 - python中声明类的时候，系统会自动声明一个和类同名的函数
             （这个函数就是构造函数）；用来创建当前类的对象
             当我们调用构造函数创建对象的时候，系统会自动调用类中的__init__方法来初始化对象
2）init方法 - __init__(魔法方法)是一个对象方法。声明的时候函数名必须是__init__，并且保证这个方法是对象方法
              声明后不用去调用，系统会自动调用

a.创建对象的时候系统自动调用__init__方法
b.创建对象的时候，构造函数需不需要参数，需要几个参数看__init__除了self以外有没有参数，
"""


class Person:
    def __init__(self):
        print('init方法')


Person()


class Student:
    def __init__(self, name, age):
        print('学生类的init', name, age)


stu1 = Student('name', 18)
