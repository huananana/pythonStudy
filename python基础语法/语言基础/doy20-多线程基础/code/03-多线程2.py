"""__author__=桃花寓酒寓美人"""
from threading import Thread
from datetime import datetime
import time


class DownloadThread(Thread):
    def __init__(self, film_name):
        super().__init__()
        self.film_name = film_name
    # 这个run方法时会在子线程中自动调用的方法，要求除了self以外不能有其它的参数

    def run(self) -> None:
        print('%s开始下载：%s' % (self.film_name, datetime.now()))
        time.sleep(5)
        print('%s结束下载：%s' % (self.film_name, datetime.now()))


t1 = DownloadThread('T')
t2 = DownloadThread('A')
t3 = DownloadThread('V')

t1.start()
t2.start()
t3.start()
