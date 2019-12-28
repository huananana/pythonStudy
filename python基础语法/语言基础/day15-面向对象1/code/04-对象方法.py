"""__author__=桃花寓酒寓美人"""

# 1.类中的方法 - 类中共同的功能
"""
方法 - 声明在类中的函数

类中的方法分为三种：对象方法、类方法、静态方法
"""
# 2.对象方法
"""
1）怎么声明：直接声明在类中的函数就是对象方法
2）怎么调用：需要对象来调用；以“对象.对象方法（）”的形式来调用
3）特点：自带参数self，参数self在通过对象电泳的时候不用传参；系统会自动将当前对象传给self传参
         当前对象 - 当前调用这个方法的对象
         当前类的对象能做的事情，self都可以做
"""


class Dog:
    """狗"""
    # eat就是对象方法

    def eat(self, food='骨头'):
        print('self:', self)
        print('狗吃'+food)

        # self 就是调用时的对象，对象能做的事情self都能做
        self.run()

    def run(self):
        print('狗跑步')


dog1 = Dog()  # dog1就是Dog的对象
print('dog1:', dog1)
dog1.eat('狗粮')
dog1.run()

dog2 = Dog()
print('dog2:', dog2)
dog2.eat('肉')
