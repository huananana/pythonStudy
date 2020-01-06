# django笔记

[TOC]

## Django框架

### 1.开启django——Web前端之路

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
> 选择git方式(Gitee账号已建立免密) --> 粘贴上面复制的SSH地址，选择clone文件位置
>
> 打开项目，本地和远程仓库就建立好连接了

###### 3)构建虚拟环境

> 方法(settings/控制台构建)
>
> 控制台构建: `windows: python -m venv venv/virtualenv `
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
> 
>
> 创建项目的依赖项文件：`pip freeze > requirements.txt`
>
> 重建依赖项文件：`pip install -r requirements.txt`

###### 4)创建Django项目

>`django-admin startproject 项目名称 .` - 注意后面有个点

###### 5)创建Django应用

`python manage.py startapp polls`

 

-- 异步请求，局部刷新



### 2.Django内置文件和待添加文件介绍

###### 1).settings.py -- 配置文件

```python
# 文件中存在DATABASES的变量(这里连接远程服务器数据库示例)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysel',
        'NAME': '',
    }
}
```



DEBUG

APP添加

LANGUAGE_CODE(语言选择)

TIME_ZONE(时区位置)

STATICFILES_DIRS(配置静态资源路径和URL前缀)