"""__author__=桃花寓酒寓美人"""

# 1.什么是匿名函数 - 没有名字的函数
"""
匿名函数还是函数，普通函数中除了声明的语法以外其它语法基本都是用于匿名函数
1) 声明匿名函数
lambda 参数列表:返回值

相当于：
def (参数列表):
    return 返回值

2) 说明：
lambda - 关键字，固定写法
参数列表 - 形参：参数名1，参数名2,...
:   - 固定写法
返回值 - 相当于普通函数中return语句
"""

# 用匿名函数实现求两个数的和
ab = lambda num1, num2: num1 + num2
# 匿名函数的调用和普通函数没有区别
print(ab(10, 20))
print(ab(num1=10,num2=20))

func2 = lambda a=1, b=2, c=3: print(a, b, c)

print(func2())
func2(b=20)


# 不定长参数
func3 = lambda *nums:sum(nums)
print(func3(10, 20, 30))
print(func3(1, 2, 3, 4))


# 注意：不支持类型说明
# func4 = lambda a: int,b: a*b

# 练习：写一个匿名函数判断指定的年是否是闰年
leap_year = lambda year: (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(leap_year(2001))

