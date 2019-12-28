# 3.用三个列表表示三门学科的选课学生姓名(一个学生可以同时选多门课)
discipline1 = ['1', '2', '5', '8', '11', '15', '12', '3', '7', '17']
discipline2 = ['11', '7', '9', '14', '6', '8', '4', '1', '34', '17']
discipline3 = ['2', '8', '24', '1', '4', '9', '14', '18', '3', '19']

# a. 求选课学生总共有多少人
num = len(set(discipline1 + discipline2 + discipline3))
print(num)

# b. 求只选了第一个学科的人的数量和对应的名字
num2 = set()
for x in discipline1:
    for y in discipline2:
        if x == y:
            num2.add(x)
    for y in discipline3:
        if x == y:
            num2.add(x)
print(set(discipline1) - num2, '数量:', len(set(discipline1) - num2))

# c. 求只选了一门学科的学生的数量和对应的名字
num2 = set()
for x in range(len(discipline1)):
    for y in range(len(discipline1)):
        if discipline1[x] == discipline2[y]:
            num2.add(discipline1[x])
    for y in range(len(discipline1)):
        if discipline1[x] == discipline3[y]:
            num2.add(discipline1[x])
    for y in range(len(discipline1)):
        if discipline2[x] == discipline3[y]:
            num2.add(discipline2[x])
num1 = set(discipline1 + discipline2 + discipline3)
print(num1 - num2, '数量:', len(num1 - num2))

# d. 求只选了两门学科的学生的数量和对应的名字
num = set(discipline1 + discipline2 + discipline3)
dict1 = dict.fromkeys(num, 1)
for x in range(len(discipline1)):
    for y in range(len(discipline1)):
        if discipline1[x] == discipline2[y]:
            dict1[discipline1[x]] += 1
    for y in range(len(discipline1)):
        if discipline1[x] == discipline3[y]:
            dict1[discipline1[x]] += 1
    for y in range(len(discipline1)):
        if dict1[discipline1[x]] == 3:
            print(dict1[discipline1[x]])
            continue
        if discipline2[x] == discipline3[y]:
            dict1[discipline2[x]] += 1
num = []
for x in dict1:
    if dict1[x] == 2:
       num.append(x)
print(num, '数量:', len(num))

# e. 求选了三门学生的学生的数量和对应的名字
num = []
for x in dict1:
    if dict1[x] == 4:
       num.append(x)
print(num, '数量:', len(num))
