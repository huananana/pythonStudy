"""__author__=桃花寓酒寓美人"""
# 导入模块的代码应该放在文件的开头
import random
import math

# 1.什么是模块
"""
python中一个.py文件就是一个模块

"""

# 2.怎么使用其他模块中的内容(导入模块)
"""
如果想要在一个模块中使用另一个模块中的内容，需要在当前模块中取导入另外的模块

1）怎么导入模块
a.import 模块名 = 导入后可以使用被导入的模块中所有的全局变量(普通全局变量，全局函数，类)
                以'模块名.变量名'的方式去使用模块中的内容

b.from 模块名 import 变量名1，变量名2，...
                = 导入后可以使用import指定的全局变量；
                  使用的时候直接用变量名

c. from 模块名 import *
                = 导入模块中所有的全局变量
                  使用的时候直接使用变量名

d. 对模块进行重命名
import 模块名 as 新模块名 - 重命名后在当前模块中同过新名字来使用导入的模块

e. 对模块中的变量进行重命名
from 模块名 import 变量名1 as 新变量名1， 变量名2 as 新变量名2，...
"""
# =============== 1.import 模块名 ==============
# import 模块名
# import test1
#
# print(test1.test)
# print(test1.x)
# test1.func1()

# =============== 2.from = import ===============
# from test1 import func1, test
# func1()
# print(test)

# =============== 3. from = import * =============
# from test1 import *
# func1()
# print(test)
# print(x)

# =============== 4. 对模块进行重命名 ============
# import test1 as test
# test.func1()


