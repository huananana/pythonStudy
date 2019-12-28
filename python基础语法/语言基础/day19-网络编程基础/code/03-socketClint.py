"""__author__=桃花寓酒寓美人"""
from socket import socket

# 1.客户端套架子
# 1）创建套接字对象（买电话）
client = socket()

# 2）链接服务器（拨号）
client.connect(('10.7.156.66', 12345))

# 3)发送消息
client.send('服务器你好'.encode())

# 4)接收消息
re_data = client.recv(1024)
print(re_data.decode(encoding='utf-8'))

# 5)关闭连接
client.close()
