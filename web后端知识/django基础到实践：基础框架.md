[TOC]

## Django基础框架

### 1.开启django——Web后端之路(最最基础先成功创建一个django项目)

###### 1)第三方托管代码平台Gitee -创建数据仓库 

> 步骤一：https://gitee.com/ 注册账号
>
> 步骤二：![Snipaste_2020-01-04_16-22-02](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-04_16-22-02.png)

> 步骤三：填写仓库名称(要求：最好以python中变量命名规则{字母数字下划线,数字不能开头}来书写，不能出现中文) - 路径最好不要更改(Gitee会自动以仓库名作为路径)
>
> 步骤四：仓库介绍随意；是否开源随意(区别其它用户能否访问)；后面的不用填写；如果有勾选请取消勾选！(理由待补充)
>
> 步骤五：点击创建，仓库就建好了
>
> 在这里打开你的仓库,复制SSH()地址($\color{red}{免密待补充}$)
>
> ![Snipaste_2020-01-04_16-34-56](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-04_16-34-56.png)



######2).PyCharm(社区)连接Gitee远程仓库

> 打开PyCharm开始页面
>
> ![Snipaste_2020-01-04_16-33-20](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-04_16-33-20.png)
>
> 选择git方式(前提：Gitee账号已建立免密) --> 粘贴上面复制的SSH地址，选择clone文件位置
>
> 选择打开项目，本地和远程仓库就建立好连接了

###### 3)构建django虚拟环境

> 方法(settings/控制台构建)
>
> 控制台构建: `windows: python -m venv venv/virtualenv `
>
> $\color{red}{控制台如何选择虚拟环境?待解决}$
>
> `Linux: source venv/bin/activate/"venv/Scripts/activate"`
>
> 安装第三方库(直接在setting中下载/控制台使用pip包管理工具)：
>
> django==2.2.9
>
> django-jet==1.0.8
>
> django-redis==4.11.0
>
> mysqlclient==1.4.6
>
> 提升：
>
> 创建项目的依赖项文件：`pip freeze > requirements.txt`
>
> 重建依赖项文件：`pip install -r requirements.txt`

###### 4)创建Django项目

>`django-admin startproject 项目名称 .` - 注意后面有个点

###### 5)创建Django应用

`python manage.py startapp polls`

###### 6)基础配置

> 1.requirements.txt  -- 第三方库清单
>
> 创建方式：`pip freeze > requirements.txt`
>
> 使用方式：`pip install -r requirements.txt`
>
> 用法解释：由于第三方库可能非常的大，而平时项目的代码都需要托管到远程仓库，这时就会遇到上传(push)代码非常慢的情况；而这些第三方库可以随时从网上下载，没有必要和代码push上远程仓库上，这时可以在项目里建立一个第三方库清单;当我们需要从远程仓库上clone代码时，我们只用把代码clone下来，然后使用`pip install -r requirements.txt`就可以把所需的库装好。是不是方便多了呢。
>
> 2.创建push忽略文件.gitignore
>
> 创建方式：在项目名称下建立文件，文件名必须为 .gitignore 
>
> ![Snipaste_2020-01-06_23-14-54](D:\pythonStudy\web后端知识\image\Snipaste_2020-01-06_23-14-54.png)
>
> 用法解释：由上面我们可以知道，第三方库是没必要上传到远程仓库的，但是每次上传我们选择需要push那些文件的时候都需要自己勾选，也许粗心大意的你就不小心把虚拟环境给选上了，所以为了方便大众(给自己偷懒)pycharm设计了忽略文件，凡是写在忽略文件上的文件，在选择push文件的时候会自动忽略.gitignore文件中的文件；($\color{red}{待补充‘如何push上传远程仓库‘}$)
>
> 如何怎么自动生成忽略文件：网址`gitignore.io` 在框框内输入操作系统(window)，语言环境(python)，开发平台(pycharm)，版本控制器(git)
>
> 3.创建static静态文件
>
> 存放image/js/css/html等文件



-- 异步请求，局部刷新



### 2.Django正式使用

在前面的操作我们就创建了一个django的项目，利用django进行web应用开发，下面我们正式进入django的使用介绍

#### 1.settings.py基础配置

###### 1).settings.py -- 配置文件

```python
# 文件中存在DATABASES的变量(这里连接远程服务器数据库示例)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysel',
        'NAME': '数据库名称',
        'HOST': '',
        'PORT': 3306,
        'USER': '',
        'PASSWORD': '',
        'CHARSET': 'utg8',
        'TIME_ZONE': 'Asia/Chongqing'
    }
}
```

###### 2)DEBUG

###### 3)APP添加

打开settings.py我们可以找到INSTALLED_APPS的列表，在这里面我们就可以添加我们自己创建的app和三方库建立的app

```python
INSTALLED_APPS = [
	'polls',  # 自己创建的app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



###### 4)LANGUAGE_CODE/TIME_ZONE(语言选择/时区位置)

```python
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Chongqing'
```



STATICFILES_DIRS(配置静态资源路径和URL前缀)

```
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
```

#### models.py - 模型构建

关于模型内方法属性：

| 通用字段的类型                             | 通用字段内参数                  | 特殊字段                | 及参数                                      |
| ----------------------------------- | ------------------------ | ------------------- | ---------------------------------------- |
| CharField(字符串)                      | verbose_name=''(别名/后台显示) | AutoField(自增) -     | primary_key=True(主键)                     |
| Date(Time)Field(时间)                 | max_length=20(最大字段长度)    | Date(Time)Field(时间) |                                          |
| ImageField(图片) - upload_to='images' | min_length=10(最小字段长度)    | ImageField(图片) -    | upload_to='images'                       |
|                                     | default=False(默认值)       | ForeignKey(外键)      | `to=Subject`/`on_delete=model.DO_NOTHING(阻止删除外键)`/`db_column=''(SQL语法别名)` |

模型里的元数据：Meta

```
# 模型里可以创建一个类Meta,描述数据的数据，给模型加上额外的信息

```



```python
class Subject(models.Model):
    """学科(模型类)"""

    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='名称')
    intro = models.CharField(max_length=1000, verbose_name='介绍')
    is_hot = models.BooleanField(default=False, verbose_name='是否热门')  # 慎重

    def __str__(self):
        return self.name

    class Meta:  # 元数据：描述数据的数据，给模型加上额外的信息
        db_table = 'tb_subject'
        verbose_name = '学科'
        verbose_name_plural = '学科'
```

`alter table tb_xx modify column is_hot boolean default 0`

