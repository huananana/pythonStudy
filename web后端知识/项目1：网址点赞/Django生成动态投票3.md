# 3

```python
# 登陆成功后为了记住这个登陆成功的用户
# 我们可以在服务器端保存和用户相关的信息
# 我们可以将这些信息保存在Django框架提供的session对象中


# 登录优化，使用正则判断账号密码  # \w:字母数字下划线 ^$
USRTNAME_PATTERN = re.compile(r'\w{6,2o0}')  
    
def check_username(username):
    matcher = USERNSME_PSTTERN.fullmatch(username)
    return matcher is not None

# django
make_password - 256加盐
```



-- 登录显示用户名

```python

```



-- 注销用户



HTTP协议是无连接无状态协议 ---> 两次请求之间不会保存用户的任何数据

再次请求服务器的时候 服务器无法得知 请求是来自哪个用户的请求



一般情况下服务器都需要记住用户来为用户提供更好的服务



用户跟踪 ---> 如果希望服务器记住用户可以使用以下三种辅助方式：

1.URL重写 http://www.baidu.com/?uid=xxx

2.隐藏域(隐式表单域) ---> 埋点(前端)

​	<form>

​		<input type="hidden" name="uid" value="xxxx">

​	</form>

3.浏览器本地存储(优先)

​	~ cookie - 浏览器中的临时文件可以保存键值对

​	coolie中的数据在发起HTTP请求时会自动加载请求头中

![Snipaste_2020-01-04_10-51-13](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-04_10-51-13.png)

​	~ window.localStorage / window.sessionStorage - 长久保存/临时保存(关闭浏览器) 



cookie和session的关系

request.session ---> 服务器内存中的一个对象，可以保存用户数据

cookie ---> 用户浏览器临时文件 ---> cookie中保存了session的id



-- 如果浏览器禁用cookie会怎么样？

-- 登录才能点击好评

```
if backurl:
    backurl = b64decode(backurl).decode()
else:
    backurl = '/'
```



-- 验证码判定

```python
# 存储code验证码至session中
request.session['code'] = code

```





-- csrf跨站请求伪造(如何防止：每次做表单，必须加令牌)

![Snipaste_2020-01-04_11-47-40](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-04_11-47-40.png)



-- 登录后返回原网址

base64编码处理

```
# python自带base64
b64encode(context.encode())
b64decode(字节串内容)
```

BASE64编码 ---> 用64个文字符号表示任意二进制数据

原理：将原来的三字节每6个比特一组变成四个字节

用A-Z,a-z,0-9,+,/一共64个字符来代表一个字节

Python ---> base64模块 ---> 64encode() / b64decode()

JavaScript ---> window ---> btoa() / atob()



-- url中不能出现非ASCII字符以及特殊字符都不能出现URL中，%编码处理上述的字符

```python
from urllib.parse import quote, unquote
a = quote('王大锤')  --- %编码字符
b = unquote(a)  --- 王大锤
```



| 易混淆知识点 | 类型                     |
| ------ | ---------------------- |
| 加密解密   | rsa / aes              |
| 编码解码   | base64 / 百分号编码         |
| 摘要签名   | md5 sha1 sha256 sha512 |



 ---好评后续作业:

![Snipaste_2020-01-04_15-54-53](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-04_15-54-53.png)

orm 模板 视图 接收参数 操作模型 渲染页面 异步请求Ajax(刷页面)