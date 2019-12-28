"""__author__=桃花寓酒寓美人"""
from socket import socket

# 服务端----------
# 1.创建套接字对象
server = socket()
# 2.绑定IP和端口
server.bind(('10.7.156.66', 12345))
# 3.准备监听
server.listen(520)
# 4.让服务一直运行
while True:
    print('开始监听...')
    # 1.接受请求
    connection, address = server.accept()

    # 2.持续交流
    while True:
        # 接受消息
        re_data = connection.recv(1024)
        re_message = re_data.decode('utf-8')
        print('%s:%s' % (address, re_message))
        if re_message == "拜拜" or re_message == "ByeBye":
            connection.close()
            break

        # 发送消息
        message = input('server:')
        connection.send(message.encode())
        if message == "拜拜" or message == "ByeBye":
            connection.close()
            break
