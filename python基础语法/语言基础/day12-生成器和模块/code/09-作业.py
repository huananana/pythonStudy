"""__author__=桃花寓酒寓美人"""

from math import pi
# 1. 写一个生成式能够产生的数据为: 1, 2, 27, 256, 3125,…, 9**9
generate = (x**x for x in range(1, 10))
for x in generate:
    print(x)
# 2. 写一个生成式能够产生1-10中所有半径是偶数的圆的面积
generate = (pi*x*x for x in range(1, 11) if not x & 1)
for x in generate:
    print(x)
# 3. 写一个生成式交换字典的键和值，产生一个新的字典
dict1 = {'name': 1, 'age': 25}
generate = ({x, dict1[x]} for x in dict1)
for x in generate:
    print(x)
