"""__author__=桃花寓酒寓美人"""


class Person:

    def __init__(self, name, age=18, gender='女'):
        self.name = name
        self.age = age
        self.gender = gender


p1 = Person('小明', gender='男')
p2 = Person('小红', 20)

# 1.获取属性值
"""
1) 对象.属性 - 获取对象指定属性的值
2）getattr(对象，属性名：str) - 获取对象指定属性的值，特点获取的属性名不确定时，可以使用
    getattr(对象，属性名:str, 默认值) - 获取对象指定属性的值，属性不存在用默认值代替
"""

print(p1.name)

# 使用情景
# attr = input('请输入获取de属性：')
# print(getattr(p1, attr))

print(getattr(p1, 'name1', '无'))

# 2.修改属性和增加属性
"""
1) 对象.属性 = 值  当属性存在的时候就是修改；属性不存在的时候是增加
2) setattr(对象，属性名，值) 当属性存在的时候就是修改；属性不存在的时候是增加
"""
# 改
p1.age = 28
print(p1.age)

setattr(p1, 'age', 30)
print(p1.age)

# 增
p1.height = 180
print(p1.height, getattr(p1, 'height'))
setattr(p1, 'weight', 70)
print(p1.weight)

# 3.删除对象属性
"""
1) del 对象.属性 - 删除对象中指定的属性
2）delattr(对象，属性名) - 删除对象中指定的属性
"""
del p1.name
# print(p1.name)  # AttributeError: 'Person' object has no attribute 'name'

delattr(p1, 'age')
# print(p1.age)  # AttributeError: 'Person' object has no attribute 'age'

# 注意：属性的增删改查值针对指定对象有效，不会影响别的对象
print(p2.name)
