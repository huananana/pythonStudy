# 1.增 - 添加元素
""
"""
1)列表.append(元素) - 在指定的列表的末尾添加一个元素
2)列表.insert(下标,元素) - 在列表指定下标 "前" 插入指定元素
"""
# 1)append
films = ["一人之下", "一拳超人", "不良人", "死亡笔记", "秦时明月", "海贼王"]
print(films)
films.append("柯南")
print(films)

# 2)insert
films = ["一人之下", "一拳超人", "不良人", "死亡笔记", "秦时明月", "海贼王"]
print(films)
films.insert(1, "柯南")
print(films)

# 2.删 - 删除列表元素
# 1)del 列表[下标] - 删除指定下标对应的元素
films = ['一人之下', '柯南', '一拳超人', '不良人', '死亡笔记', '秦时明月', '海贼王']
print(films)
del films[2]
print(films)

# 2) 列表.remove(元素) - 删除列表中指定元素
# 注意 a.如果元素不存在会报错！ b.如果元素在列表中有多个，只删第一个

nums = [1, 2, 3, 4, 2]
print(nums)
nums.remove(2)
print(nums)

# 3)列表.pop()      -  "取出" 列表中最后一个元素,返回被去除的元素
#   列表.pop(下标)  -  "取出" 列表中指定下标对应的元素,返回被去除的元素

nums = [10,2,45,2,9]
print(nums)
del_num = nums.pop()
print(nums)
print(del_num)

nums = [10,2,45,2,9]
print(nums)
del_num = nums.pop(-2)
print(nums)
print(del_num)

# 练习：深处下面这个列表中所有小于60的元素

# 1.del scores[]
scores = [89, 45, 56, 20, 90, 78, 60, 23, 87, 20, 50]
for x in scores[:]:
    if x < 60:
        scores.remove(x)
print(scores)

# 2.scores.remove()
scores = [89, 45, 56, 20, 90, 78, 60, 23, 87, 20, 50]
for x in scores[:]:
    if x < 60:
        scores.remove(x)
print(scores)

# 3.改 - 修改元素的值
# 列表[下标] = 值  --  将列表中指定下标对应的元素修改成指定的值
# 示例：
nums = [10,2,45,2,9,-2]
print(nums)
nums[0] = 100
print(nums)

# 练习：将scores中所有小于60的分数换成'不及格'
scores = [89,45,56,20,90,78,60,23,87,20,50]
for index in range(len(scores)):
    if scores[index] < 60:
        scores[index] = "不及格"
print(scores)









