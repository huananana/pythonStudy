"""__author__=蒋志颖"""

# 1.什么是字典（dict）
"""
a.字典定义：
字典是容器行数据类型，将{}作为容器的标志，里面多个元素用逗号隔开；但是字典中的元素是键值对：{键1：值1，键2：值2,...}
可变的（支持增删改），无序（不支持下标操作）

b.键值对
字典中的所有元素都必须是键值对，键和值必须成对出现；字典存数据存的是值，键是用来区分和说明不同的值的
键 - 任何不可变的数据都可以作为见，实际开发的时候一般将字符串作为key;键是唯一的
值 - 任何类型的数据都可以作为字典的value
"""
student1 = {'abc': 19, "a": True, "b": [1, 2], "c": {"name": "小明"}}
print(student1)

# 键是不可变,且唯一
student2 = {10: 100, "a": 200, (1, 2): 300}
print(student2)
student4 = {"a":10, "a":100, "b": 20}
print(student4)


# 2.字典的增删改查
# 1)查 - 获取字典的值
"""
a.获取单个值
字典[key] - 获取字典中指定key对应的值
字典.get(key, 默认值) - 获取字典中指定key对应得值,不存在，返回默认值(默认值为None)


"""
person = {"name": "小明", "age": 20, "tel": "1530002273"}
print(person["tel"])
# print(person["height"])     # KeyError: 'height'

print(person.get("age"))
print(person.get("height", "Nones"))

"""
b.遍历
for key in 字典:  # 取的为key
    循环体
"""
# 正确遍历方式：
for x in person:
    print('key: ', x, "value: ", person[x])

# 其它(复杂)的遍历方式
# 不能这么写，效率低、占空间
print(person.items())
for key, value in person.items():
    print(key, value)

# 2).增/改
"""
字典[key] = 值 - 当key存在的时候，秀发i字典指定key对应得值；当key不存在的时候,添加"key:值"的键值对
"""
person = {"name": "小花", "age": 20, "tel": "1530002273"}

person["name"] = "小明"
print(person)
person["score"] = 90
print(person)

# 3)删 - 删除键值对
"""
1)del 字典[key] - 删除字典中指定key对应的键值对
2)字典.pop(key)  - 取出字典中指定key对应的值（key对应的键值对会从字典中删除）
"""
del person['age']
print(person)

name = person.pop('name')
print(person, name)


# 练习：保存一个班所有的学生的信息（姓名、学号、年龄、成绩、电话，假设一个班50个人）
all_student = [
    {"name": '小明', 'age': 11, 'score': 4, 'tel': '13468742354'},
    {"name": '小1', 'age': 28, 'score': 77, 'tel': '13468742354'},
    {"name": '小2', 'age': 33, 'score': 56, 'tel': '13468742354'},
    {"name": '小3', 'age': 55, 'score': 99, 'tel': '13468742354'},
    {"name": '小4', 'age': 1, 'score': 2, 'tel': '13468742354'},
    {'nnn': '123'}
]

# 1)统计以上学生中不及格学生的人数
num = 0
for student in all_student:
    if not student.get('score'):
        continue
    if student.get('score') < 60:
        num += 1
print(num)
# 2）打印所有未成年人学生的姓名
for student in all_student:
    if not student.get('score'):
        continue
    if student.get('age') < 18:
        print(student['name'])
# 3）将年龄为25岁以上的学生的电话号码设置为"保密"
for student in all_student:
    if not student.get('score'):
        continue
    if student.get('age') > 25:
        student['tel'] = "保密"
print(all_student)
