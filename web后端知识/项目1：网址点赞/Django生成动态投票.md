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