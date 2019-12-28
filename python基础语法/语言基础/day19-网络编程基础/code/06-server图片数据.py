"""__author__=桃花寓酒寓美人"""
from socket import socket

server = socket()
server.bind(('10.7.156.66', 11111))
server.listen(520)
while True:
    connection, address = server.accept()

    # 发送图片 - send()
    with open('../c_top/xiaoniao.jpg', 'rb') as f:
        data = f.read()

    # connection.send(str(len(data).encode()))
    length = len(data)
    connection.send(str(length).encode())
    connection.send(data)














