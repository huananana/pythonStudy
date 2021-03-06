"""__author__=桃花寓酒寓美人"""
from datetime import datetime
import time
from threading import *
from random import randint

# 1.join
"""
线程对象.join()
代码A

代码A会在线程对象执行完成后才执行
"""


def download(film_name: str):
    print('%s开始下载：%s' % (film_name, datetime.now()))
    time.sleep(randint(3, 7))
    print('%s下载结束：%s' % (film_name, datetime.now()))


t1 = Thread(target=download, args=('暮光之城',))
t2 = Thread(target=download, args=('两只老虎',))
t3 = Thread(target=download, args=('海上钢琴师',))

# 需求1：所有电影都下载结束之后打印'所有电影下载完成'
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
# print('所有电影下载完成')

# 需求2：要求暮光之城和两只老虎下载完成后才下载海上钢琴师
t1.start()
t2.start()
t1.join()
t2.join()
t3.start()
