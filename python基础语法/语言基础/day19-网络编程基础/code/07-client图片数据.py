"""__author__=桃花寓酒寓美人"""
from socket import socket

client = socket()
client.connect(('10.7.156.66', 11111))

# 接收图片长度
total_length = int(client.recv(1024).decode())
print('第一次:', total_length)


# sum_length = 0   # 保存接收到的图片的总长度
sum_data = bytes()   # 保存接收到的图片的总数据

while True:
    re_data = client.recv(1024)
    sum_data += re_data
    print(len(sum_data))
    if len(sum_data) == total_length:
        with open('../client/test.jpeg', 'wb') as f:
            f.write(sum_data)
        break

