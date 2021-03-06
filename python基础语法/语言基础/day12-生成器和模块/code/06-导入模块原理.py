"""__author__=桃花寓酒寓美人"""

# 1.导入模块的原理
"""
导入模块时，会将目标模块执行一遍
"""
import test1

# 2.阻止导入
"""
如果将模块中的代码写入if __name__ == '__main__'这个if语句中，那么这个if语句代码在被导入的
时候不会执行。直接运行当前模块的时候会执行

阻止的原理：
在创建模块的时候，系统会自动给这个模块添加属性：__name__,用来保存当前模块的名字
__name__属性的值默认是当前文件的文件名；当直接运行当前模块的时候，这个模块的__name__属性值
会变成'__main__'，运算完成后又变回文件名。
"""

