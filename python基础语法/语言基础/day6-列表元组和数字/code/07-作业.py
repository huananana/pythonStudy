"""__author__=蒋志颖"""

# 1. list.count():统计某个元素在列表中出现的次数
list1 = [1, 11, 22, 22, 11]
num = 22
count = 0
for index in list1:
    if num == index:
        count += 1
print(count)

# 2. list.extend():在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list1 = [1, 11, 22, 22, 11]
new_list = ["a", "b", "c"]
for x in new_list:
    list1 += x
print(list1)
# 序列：列表、数组、字符串、元组统称序列

# 3. list.index(obj):从列表中找出某个值第一个匹配项的索引位置
list1 = [1, 11, 22, 22, 11]
num = 22
for x in range(len(list1)):
    if num == list1[x]:
        print(x)
        break
list1 = [1, 11, 22, 22, 11, 2]

# 4. list.reverse():反向列表中的元素(不能新建列表)
if len(list1) & 1:
    for x in range(int((len(list1)-1)/2)):
        list1[x], list1[len(list1)-x-1] = list1[len(list1)-x-1], list1[x]
    print(list1)
else:
    for x in range(int(len(list1)/2)):
        list1[x], list1[len(list1)-x-1] = list1[len(list1)-x-1], list1[x]
    print(list1)