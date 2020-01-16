-- 前后端分离



-- 删除模版页配置



-- json返回列表需要加参数sava?



-- objects查询时+

only('字段...') - 指定查询那些列

defer('字段') - 指定不查询那些列



-- 比较两文件不一样

vim -d 文件1 文件2

-- 比较两版本

git diff 版本1 版本2

beyond compare  专业作比较工具



-- 前后端渲染区别在哪儿



-- 提升数据库性能：redis

数据体谅不大，访问次数多 - 缓存



--配置缓存数据库(配置文件不会配找官方文档)



-- django中的settion会话信息默认放在数据库中(非常不好)

会话

读写性能好，不用手动管理，可以水平拓展

```python
# 配置缓存数据库
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [
            'redis://114.55.106.77:6379/0',
            #  可以书写多个redis，下面的redis都是读数据
            #  一个主人/多个奴隶
        ],
        'KEY_PREFIX': 'djang19062',  # 前缀
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 512,
                # 最多允许512个连接，不释放连接
                # TCP协议建立连接3次握手，释放连接4次挥手
                # redis (10/8)w/s读取速度
            },
            'PASSWORD': 'jzyi.default',
        }
    },
}

# 配置使用缓存来支持用户会话
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# 会话数据放在那一组缓存中
SESSION_CACHE_ALIAS = 'default'
# 缓存过期时间为1天
SESSION_COOKIE_AGE = 86400
```

```python
# 复习启动redis
redis-server --requirepass jzyi.qaz >> redis.log &
# 查看后台进程 - 只能查看当前终端开启的进程 ps -a
jobs
# 查看端口信息
netstat -ntlp

# 进入redis
redis-cli
auth pass
```

```python
# 添加缓存数据
# 1.编程式缓存
def show_subjects(request):
    """获取所有学科"""
    if caches['default'].get('subjects'):
    queryset = Subject.objects.all()
    subjects = [SubjectMapper(subject).as_dict()
                for subject in queryset]
    resp = JsonResponse(subjects, safe=False)
    caches['default'].set('subjects', resp)
    return resp
# 2.django框架封装的方法(views.py)
@cache_page(timeout=3600, cache='default')
```

# Django生成动态投票
### Django框架

```python
""" 
[TOC]
1.urls.py -- 项目下对应网址的视图函数
2.settings.py -- 配置文件
3.models.py -- 模型
4.admin.py -- 后台管理
5.views.py -- 视图
6.static -- 静态文件存放位置
7.templates -- html文件存放位置位置
9.补充知识点
-----------------------------------------------------------------------------------------------
1.urls.py -- 项目下对应网址和所调用的视图函数
关键字：urls.py,项目网址功能
框架:
urlpatterns = [
  path('admin/', admin.site.urls), 
  path('', index),
  ...
]
--参数介绍
'网址后缀',网址功能函数
-----------------------------------------------------------------------------------------------
2.settings.py -- 配置文件
TEMPLATES			--数据库绑定,
DEBUG,
INSTALLED_APPS		-- 应用添加,
LANGUAGE_CODE		-- (语言选择),
TIME_ZONE			-- (时区位置),
STATICFILES_DIRS	-- (配置静态资源路径和URL前缀)
TEMPLATES['DIRS']	-- 配置html文件位置 
-----------------------------------------------------------------------------------------------
3.models.py -- 模型
用途：创建所需类
效果：自动构建数据库表，编辑后台别名，元数据
mx框架：
class lei(models.Model):
	no = models....(...)
	...(AutoField(自增),IntegerField(整型),CharField(字符串),BooleanField(布尔),DateField(时间))
	...(primary_key,verbose_name,max_length,default)
	# 当数据为对象时
	models.ForeignKey(to=类名, on_delete=models.DO_NOTHING, db_column='sno')
	
	class Meta:  # 元数据
		db_table = '表名'
		...(verbose_name/verbose_name_plural,设置后台管理类别名(默认类名+s)/设置类展开别名 )
--迁移数据(终端)：
python manage.py makemigrations polls
python manage.py migrate
-----------------------------------------------------------------------------------------------
4.admin.py -- 后台管理
用途：可以增删查改后台数据
admin框架：
class lei(admin.ModelAdmin):
	list_display = ('no, name, ...')
	...(以及其它方法：
					list_display_links(...) - 链接属性
					search_fields(...) - 搜索框
					ordering(...) - 升序)

admin.site.register(mx, lei)
-----------------------------------------------------------------------------------------------
5.views.py -- 视图
关键字：页面的数据处理，异常处理， html地址
views框架：
def func(request):
	context = {
      'datas': data
	}
	return render(request, 'html地址', context)
--模型数据提取
context = lei.objects.all() - 模型所有数据
context = lei.objects.get(select) - 一条数据
context = lei.objects.filter(select) - 满足条件的数据
--返回值介绍：
1.render(request, 'html地址', 数据) --渲染新网页
2.redirect('url') --渲染到指定已存在的网页
--方法介绍：
context.save() --保存数据修改至数据库中
-----------------------------------------------------------------------------------------------
6.static -- 静态文件存放位置
关键字:图片,css/js文件存放地点
框架：
在项目下建立文件夹static/css, static/image, static/js
-----------------------------------------------------------------------------------------------
7.templates -- html文件存放位置位置
关键字：html文件存放位置
框架：
项目下建立文件夹templates/APP(应用名)
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
8.补充知识点
-- 创建数据库
create database django1906 default charset utf8;
-- 创建用户
create user 'jackfrued'@'%' identified by '123456';
-- 给用户授权
grant all privileges on django1906.* to 'jackfrued'@'%';

-- 关于表格内内容太长格式错乱的问题：注意不加分号，末尾效果图查看
select * from table\G   
"""
```

### 实例：

###### 1.urls.py

在项目django1906的urls.py下关联首页,及功能页

```python
urlpatterns = [
    path('admin/', admin.site.urls),  # 后台管理页面
    path('', index),  # 首页
    path('teachers/', show_teacher),  # 教师页面
    path('good/', praise),  # 好评添加功能
    path('bad/', bad),  # 差评添加功能
]
```

######2.settings.py 

配置应用文件polls

```python
# 在settings.py 文件中找到
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',  # 添加应用
]
```

语言时区设置

```python
LANGUAGE_CODE = 'zh-hans'  # 语言
TIME_ZONE = 'Asia/Chongqing'  # 时区
```

配置静态资源路径和URL前缀

```
# 配置静态资源路径和URL前缀
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
```

数据库绑定

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django1906',  # 仓库名
        'HOST': '114.55.106.77',  # ip地址
        'PORT': 3306,  # 端口号
        'USER': 'Jzyi',  # 用户名
        'PASSWORD': '1qaz2wsx',  # 密码
        'CHARSET': 'utf8',  # 编码方式
        'TIME_ZONE': 'Asia/Chongqing',  # 时区
    }
}
```

######3.models.py -- 模型

在应用下models.py文件下创建模型：

```python
class Subject(models.Model):
    """学科模型类"""
    
    # 魔法方法介绍
    def __str__(self):  # 魔法方法：显示类数据时，显示self.name
        return self.name
    
	...
    class Meta:  # 给模型加上特殊的信息
        ...


class Teacher(model.Model):
	"""讲师模型类"""
	...
	class Meta:
		...


...
```

数据迁移：将类转换为数据库表

`(终端输入)python manage.py makemigrations polls `

![Snipaste_2020-01-02_20-15-25](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-02_20-15-25.png)

polls/migrations文件下自动生成0001_initial.py

![Snipaste_2020-01-02_20-17-39](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-02_20-17-39.png)

`(终端输入)python manage.py migrate` 

![Snipaste_2020-01-02_20-20-57](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-02_20-20-57.png)

在绑定的数据库中可以看到迁移过来的数据表

![Snipaste_2020-01-02_20-22-11](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-02_20-22-11.png)

![Snipaste_2020-01-02_20-27-24](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-02_20-27-24.png)



######4.admin.py -- 后台管理

创建Django后台超级管理员账号

`python manage.py createsuperuser` - 输入用户名/邮件地址/密码(8位)

![Snipaste_2020-01-02_20-34-59](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-02_20-34-59.png)

`home_page/admin/` - 后台管理平台/登录 - 输入我们刚刚创建的username/password



######5.views.py -- 视图

在应用的views.py中创建index函数

```python
def func(request):
    ...
    return ...


...
```



######8.补充知识点

###### 末尾效果图

表格因内容过长而产生的内容错乱：

![Snipaste_2020-01-02_11-53-20](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-02_11-53-20.png)

解决方案

![表和](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-02_11-46-53.png)


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



django环境

`python manage.py shell`

```
django时间
from django.utils import tiomezone
user.laset_visit = timezone.now()
user.save()
```

-- 密码md5摘要自动生成操作



```python
# 重写save方法
def save(self):
	# 商业代码中需要对用户口令进行加盐操作
	self.password = to_md5_hex(self.password)
	super().save()
```

```
# 
```



-- CSRF -->跨站请求伪造 ---> {% csrf_token %}

Cross Site Request Forge

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

### 数据没拿时显示花括号

```html
# CSS
[v-cloak]{
	display:none;
}

# 加上v-cloak 遮蔽 
<div id='app' v-cloak>

```

### 添加加载提示(三方库)

element ui

使用：放在Vue-#app下面

`<link rel="stylesheet" href="![img](file:///C:\Users\Administrator\AppData\Roaming\Tencent\QQTempSys\%W@GJ$ACOF(TYDYECOKVDYB.png)https://unpkg.com/element-ui@2.13.0/lib/theme-chalk/index.css">`



### 请求数据失败

```html
created(){
	fetch('/teachers/' + location.search)
		.thenI(resp => resp.json())
		.then(json => {
            this.loading = false
            if(json.code == 20000){
                this.subject = json.subject
                this.teachers = json.teachers
            } else {
                this.$message.error(json.message)  # 添加的代码
            }
		})
}
```



### 关于save保存

.save() -- 保存的时候会锁定数据，当访问量上来后，会崩溃，会成为性能瓶颈

解决办法：使用redis缓存

```python
# caches['default'].set/get
# redis_cli = Redis(host='', port='', password='', )
redis_cli = get_redis_connection()  # 默认default
key = f'django19062:polls:{tno}'
if not redis_cli.exists(key):
    redis_cli.hmset(key, {'good': 0, 'bad': 0})
if request.path.startswith('/praise'):
    redis_cli.hincrby(key, 'good', 1)
else:
    redis_cli.hincrby(key, 'bad', 1)
data = {'code': 10000, 'message': '操作成功'}

# 通过定时任务和异步任务每隔一段时间就将Redis中投票的数据
# 合并到数据库的表中，这样的话最终投票的票数是正确的
# 要实现定时任务可以使用APScheduler或Celery三方库
```



