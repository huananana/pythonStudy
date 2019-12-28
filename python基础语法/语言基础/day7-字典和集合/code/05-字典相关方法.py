"""__author__=蒋志颖"""
# 1.字典.clear() - 清空字典
dog = {'name': '大黄', 'age': 4, 'sex': '公', 'kind': '土狗'}
dog.clear()
print(dog)

# 2.字典.copy() - 拷贝字典，返回新的字典
dog = {'name': '大黄', 'age': 4, 'gender': '公狗', 'kond': '土狗'}
dog2 = dog.copy()
dog['name'] = '萌萌'
print(dog2)

# 3.dict.fromkeys(序列，值) - 创建新字典；将序列中的元素作为key,值作为每个key，指定的值作为每个key的value，去创建一个新的字典
dict1 = dict.fromkeys('abc', 100)
print(dict1)

# 4.字典.items()、字典.values()、字典.keys()
# 字典.keys() -> 获取字典所有的key并且返回，返回的数据类型是序列但是不是列表
# 字典.values() -> 获取字典所有的value并且返回
# 字典.items() -> 同时获取字典所有的key和value，返回一个序列，序列中元素是由两个元素的元组，这两个元素分别是key和value
dog = {'name': '大黄', 'age': 4, 'gender': '公狗', 'kond': '土狗'}
print(dog.keys())
print(dog.values())
print(list(dog.keys()))
print(dog.items())

# 5.字典.setdefault(key,value) -> 字典中添加键值对（key存在的时候不会修改）
dog = {'name': '大黄', 'age': 4, 'gender': '公狗', 'kond': '土狗'}
dog.setdefault('color', '黄色')
print(dog)

dog.setdefault('name', "财财")
print(dog)

# 6.字典1.update(字典2)  - 将字典2中的键值对添加到字典1中
dog = {'name': '大黄', 'age': 4, 'gender': '公狗', 'kond': '土狗'}
dict2 = {'name': '小明', 'height': 170}
dog.update(dict2)
print(dog)

# 练习2:
# 设置数据保存一个班级的信息：
# 班级名字、位置、所有的老师(name,sex,QQ,职位)、
# 所有的学生(name,universe,tell,sex,age,
# 紧急联系人(name,关系，tell))、

data = {'ClassName': 'python1906',
        'Location': '力宝大厦',
        'Teacher': [
            {'name': '余婷', 'sex': '女', "QQ": 123456789, '职位': '讲师'},
            {'name': '张瑞燕', 'sex': '女', "QQ": 223456789, '职位': '班主任'}
        ],
        'Student': [
            {
                'name': '蒋志颖',
                'university': '成都大学',
                'tell': 13698745632,
                'sex': '男',
                'age': 22,
                'EmergencyContact': {
                    'name': '她她她',
                    'sex': 'xx',
                    'tell': 13131313131
                }
            }
        ]
        }
print(data)
