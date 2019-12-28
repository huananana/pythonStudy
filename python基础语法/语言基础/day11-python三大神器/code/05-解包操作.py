"""__author__=桃花寓酒寓美人"""

# 1.解包：在容器型类型前加*或者**可以容器进行解包
# 注意：**只能放在字典的前面
#

list1 = [10, 20, 30]
print(*list1)  # list1 = [10, 20, 30]  -> *list1 == 10, 20, 30


def func1(x, y, z):
    print('x:{}, y:{}, z:{}'.format(x, y, z))


func1(10, 20, 30)
func1(*list1)


# 练习：写一个函数可以对多个数据进行不同的运算
def sum_1(*nums):
    sum1 = 0
    for x in nums:
        sum1 += x
    return sum1


def sub_1(*nums):
    sub1 = nums[0]
    for x in nums[1:]:
        sub1 -= x
    return sub1


def operation(char, *nums):
    if char == "+":
        return sum_1(*nums)
    elif char == "-":
        return sub_1(*nums)


print(operation('+', 1, 2, 3, 4))

# 2) **是将字典解包
dict1 = {'x': 1, 'y': 2}
print(dict1)
# print(**dict1)  # **dict == x=100, y=200

dict2 = {'end': '=', 'sep': 'x'}
print(10, 20, **dict2)


def func2(x, y):
    print(x, y)



