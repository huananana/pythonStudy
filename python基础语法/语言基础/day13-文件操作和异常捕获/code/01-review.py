"""__author__=桃花寓酒寓美人"""

"""

import ：在导入模块的时候会检查当前模块之前是否已经导入过，如果已经导入过不会重新导入
include
联系：都是导入文件
区别：import会检查是否已经导入
      include不会检查每次都会重新导入


"""


dict1 = {'name': 1, 'age': 25}
generate = ({key, dict1[key]} for key in dict1)
for key in generate:
    print(key)

dict2 = dict((dict1[key], key) for key in dict1)
print(dict2)
