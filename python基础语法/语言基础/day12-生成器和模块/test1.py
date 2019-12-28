"""__author__=桃花寓酒寓美人"""

if __name__ == '__main__':

    print('开始')
    # 全局变量
    test = 100

    # x是全局变量
    for x in range(4):
        print('=============')


    # func1是全局变量
    def func1():
        b = 100
        print('test1中的函数1')


    print('结束')

