"""__author__=桃花寓酒寓美人"""
'''关于pymysql的数据库连接和MySQL操作
1.连接MySQL数据库
语法：
连接对象 = pymysql.connect(host,port,user,password)

参数解释：
    host:主机地址(localhost表示当前设备上的数据库/服务器公网ip)
    port:mysql服务端口，3306 (默认？)
    user:MySQL用户
    password:用户密码
    database:连接后默认操作的数据库
    charset:设置连接的数据库文件的编辑方式
    autocommit:是否自动提交(提交啥？)

2.获取游标对象
语法：
with 连接对象.cursor() as 游标对象(通常用cursor):
    cursor(游标对象).execute('sql语句')
    
注意：查询返回值类型 - None:查询结果以元组得形式返回；pymysql.cursors.DictCursor:查询结果以字典的形式返回

3.关闭连接
连接对象.close()

'''

import pymysql

# 1.和mysql建立连接
'''
连接对象 = pymysql.connect(host,port,user,password)

说明：
    host - MySQL主机地址(localhost表示当前设备上的mysql，服务区公网ip)
    port - mysql服务端口，3306
    user - mysql用户
    password - 用户密码(如果创建用户的时候没有设置密码，这个参数可以不用赋值)
    database - 建立连接后默认操作的数据库
    charset - 设置连接的数据库文件的编码方式
    autocommit - 是否自动提交
'''
con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='mysql&272727',
    database='school',
    charset='utf8',
    autocommit=True
)

# 2.通过连接获取游标对象
'''
with 连接对象.cursor() as 游标对象:
    数据库操作上下文

说明：
    查询返回值类型 - None:查询结果以元组得形式返回；
                    pymysql.cursors.DictCursor:查询结果以字典的形式返回
    数据库操作上下文 - 游标对象只有在数据库操作上下文才有效
'''
with con.cursor() as cursor:
    # 数据库操作上下文
    # 3.执行sql语句：游标对象.execute('sql语句')
    cursor.execute('create database if not exists pyschool;')

# 关闭连接
con.close()
