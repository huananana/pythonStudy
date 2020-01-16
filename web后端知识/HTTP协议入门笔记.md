###HTTP协议入门笔记

HTTP协议的意思演变和设计思路

HTTP是基于TCP/IP协议的应用层协议：他不涉及数据包传输，主要规定了客户端和服务器之间的通信格式，默认使用80端口

GET 命令

91年 0.9版只有一个GET命令

```python
GET /index.html
```



TCP连接建立后，客户端向服务器进行GET请求，协议规定服务器只能回应HTML格式的字符串，服务器发送完毕就关闭TCP连接



96年 HTTP请求和回应的格式改变，每次通信都必须包括头信息(HTTP header)，用来描述一些元数据，

下面是一个1.0版的HTTP请求的例子

```python
GET / HTTP/1.0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)
Accept: */*
```

第一行是请求命令，必须在尾部添加协议版本（HTTP/1.0).后面就是多行头信息，描述客户端的情况。

服务器回应格式

```python
HTTP / 1.0 200 OK
Content-Type: text/plain
Content-Length: 137582
Expires: Thu, 05 Dec 1997 15:55:28 GMT
Last-Modified: Wed, 5 August 1996 15:55:28 GMT
Server : Apache 0.84

<html>
	<body>Hello World</body>
</html>
```

回应的格式是头信息+一个空行（\r\n) +数据。其中，第一行是协议版本+状态码(status code) + 状态描述



Content-Type 字段

关于字符的编码，1.0版规定，头信息必须是ASCII码，后面的数据可以是任何格式。因此服务器回应的时候，必须告诉客户端，数据是什么格式，这就是Content-Type字段的作用。

常见的Content-Type字段

```python
text/plain
text/html
text/css
image/jpeg
image/pg
image/svg+xml
audio/mp4
video/mp4
application/javascript
application/pdf
application/zip
application/atom+xml
```

这些数据类型总称为MIME type , 除了预定义的类型，厂商也可以自定义类型。



### 理解RESTful架构





