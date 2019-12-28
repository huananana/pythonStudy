"""__author__=桃花寓酒寓美人"""
# json模块是python提供的专门用来支持json数据
import json


# 1.什么是json
"""
json是一种数据格式：一个json只有一个数据；唯一的这个数据必须是json支持的数据类型的数据
json支持的数据类型：
1）数字类型（number） - 包含所有的数字（整数和小数），并且支持科学计数法；数字直接写
                        1000 12.5 3e4 -3.14
2）字符串（string）   - 文本数据，只能使用双引号,并且支持转义字符
                        "abc", "hello"，"\nand"
3）布尔（boolean）    - 只有true和false

4）空值               - null

5）数组（array）      - [元素1， 元素2， 元素3，...]元素是json支持的任何类型的数据

6）字典（dict）       - {key1：value1，key2：value2...} key必须是字符串
"""
# 2.json转python
"""
1)转换规律
json            python
数字            int/float
字符串          字符串；双引号可能变成单引号
布尔            布尔；true -> True; false -> False
null            None
数组            列表
字典            字典

2)转换方法
json.loads(字符串) - 将json合适的字符串转换成python对应的数据
                   - 注意：要求这个字符串的内容必须是json格式的数据
"""
result = json.loads('100')
print(result, type(result))

result = json.loads('"abc"')
print(result, type(result))

result = json.loads('[12, "abc", null, true]')
print(result, type(result))

# 3.python转json
"""
python              json
int/float           数字
字符串              字符串；单引号会变成双引号
布尔值              布尔；True -> true；False -> false
None                null
列表/元组           数组
字典                字典

2）方法
json.dumps(数据) - 将python数据转换接送格式的字符串
"""
result = json.dumps('100')
print([result], type(result))

result = json.dumps([100, 'abc', None, True])
print([result], type(result))

result = json.dumps(('hello', 234, False))
print([result], type(result))

result = json.dumps({1: 1, 'name': 2})
print([result], type(result))

str1 = ''
print(len(str1))
