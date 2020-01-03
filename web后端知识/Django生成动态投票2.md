# 2

### 更改后台样式

-- 下载jet三方库

`pip install django-jet -i https://pypi.doubanio.com/simple`

-- 迁移数据

`python manage.py migrate jet`

-- settings.py 添加应用jet

```python
# 这里'jet'必须要放第一位
INSTALLED_APPS = [
    'jet',
	...
]
```

-- urls.py 

```python
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
	...
]
```





生成哈希摘要 - 两个不同的对象(有限时间)找不到相同的哈希摘要

一个哈希摘要 - 一个字符串

给对象生成唯一的标识符

```python
# 给压缩包对象生成哈希摘要
# 同一个文件生成的哈希摘要是相同的
# 数字指纹, 数字签名, 哈希摘要
from hashlib import md5, sha1, sha256, sha512

hasher = md5()
with open('xxx', 'rb')as file:
	data = file.read(4096)
	while data:
		hasher.update(data)
        data = file.read(4096)
    print(hasher.hexdigest())
```



异构(系统(windows/),语言(python/java)...不同)

-- Ajax - Asynchronous JavaScript and XML

-- JSON - JavaScript Object Notation

-- YAML 



-- 视图异步请求

```html
# $()函数中的箭头函数是页面加载完成后要执行的回调函数
	<script>
        $(()=> {
          // 通过$(选择器)获取页面元素绑定点击事件
          // on方法的第一个参数是事件名第二个参数是事件回调函数
          // 时间回调函数的参数evt是代表事件的对象
            $('.comment>a').on('click', (evt)=>{
                // 阻止事件默认行为(避免直接刷新页面)
                evt.preventDefault()
                // 通过事件对象获取事件源并由$函数转成jQuery对象
                let anchor = $(evt.target)
                // 通过jQuery对象的getJSON方法发起Ajax请求
                // 第一个参数是请求的URL
                // 第二个参数是请求完成之后要执行的回调函数
                $.getJSON(anchor.attr('href'), (json)=>{
                    if (json.code == 520){// 如果投票成功
                        // 获取与a标签相邻的span标签
                        let span = anchor.next()
                        // 将span标签的值加1再写回span标签
                        span.text(parseInt(span.text())+1)
                        // 实现函数节流
                        // flag = false
                        // setTimeout(()=>{ flag = true }, 2000)
                    }else{// 投票失败
                        alert(json.message)
                    }
                })
            })
        })
    </script>
```



### 页面登录

-- 写html网页代码

```
知识点：
```

-- 视图添加功能函数

-- 网址后缀绑定功能函数



### 添加验证码

-- 导入验证码封装库

fonts/captcha.py  (资源在仓库,简单验证码)

-- 随机验证码

-- 绑定视图函数

-- 网址后缀绑定功能函数

```

```



### 用户模型

-- 创建用户模型

```

```



