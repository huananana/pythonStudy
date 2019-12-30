"""__author__=桃花寓酒寓美人"""
"""
使用redis做高速缓存
1.what: 使用MySQL存储数据最大的问题再于查询与提取数据慢，为了解决MySQL提取数据慢的问题，我们可以使用redis做高速缓存操作
2.why：为什么使用redis做高速缓存(redis提取速度快的原因有很多，下面介绍主要几点(后补充，数据与内存硬盘的存储关系))
      1)绝大部分请求是纯粹的内存操作，不用访问硬盘
      2)非关系性数据库，数据结构简单，对数据的操作也简单，数据结构是专门设计的
3.how(简单使用):
    思路：要访问一个数据，先从redis中查询，
        有，直接提取返回
        无，再从MySQL中取出来，存入redis缓存中，返回

序列化(dumps - 倾倒)：把一个对象变成字符串（str）或者字节串（bytes）
反序列化(loads - 装载)：把字符串或者字节串还原成对象
json - dumps / loads - 字符串
pickle -dumps / loads - 字节串
"""


import pickle
import time
import pymysql
import redis


# 无，MySQL提取数据
def load_depts_from_db():
    conn = pymysql.connect(host='114.55.106.77', port=3306,
                           user='root', password='alymysql&272727',
                           charset='utf8', db='hrs')

    depts = ()
    try:
        with conn.cursor() as cursor:
            cursor.execute('select dno, dname, dloc from tb_dept')
            depts = cursor.fetchall()
    except pymysql.MySQLError as err:
        print(err)
    finally:
        conn.close()
    return depts


def main():
    # 从redis提取数据
    client = redis.Redis(host='114.55.106.77', port=6379, password='1qaz2wsx')
    start = time.time()
    data = client.get('depts')
    # 有，输出；无，从MySQL提取
    if data:
        depts = pickle.loads(data)
    else:
        depts = load_depts_from_db()
        client.set('depts', pickle.dumps(depts))

    end = time.time()
    # 提取结果
    print(depts)
    # 提取时间
    print(f'执行时间：{end - start}秒')


if __name__ == '__main__':
    main()
