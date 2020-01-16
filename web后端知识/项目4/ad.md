# ad

网络API - 通过HTTP(S)请求请求一个UTL获得(JSON)数据

> API - Application Programming Interface
>
> Application definition
>
> djangorestframework - rest风格的数据接口



### 反向工程将表变成模型

`python manage.py inspectdb > common/models.py`

1.模型如果要迁移

```python
class Model(model.Model):

	class Meta:
		managed = False
```

2.改名字需要重构重命名

refactor -> rename

3.多对多字段

estates = models.ManyToManyField(to='其他表', through='中间表')



4.CRUD - Create Read Update Delete



### 目标数据接口

实体 --->  数据 ---> 数据接口 ---> 网络API (HTTP/HTTPS)

REST架构 ---> RESTful API ---> 无状态、幂等性 ---> 风格

`幂等性：一个幂等操作的特点`

REpresentational State Transfer ---> 表述性状态转移

最适合互联网应用的架构



水平扩展 ---> 单机结构 ---> 多机结构(分布式集群)

(用户流量扩增，进行水平扩展)



HTTP ---> 无连接无状态

URL ---> Universal Resource Locator ---> 资源

HTTP协议 请求行 GET / POST / DELETE / PUT / PATCH

新建 - POST - 不需要幂等性

查看 - GET

更新 - PUT / PATCH

删除 - DELETE



face_recognition - 人脸识别-表情包



设计URL ---> 名词



连表操作：

        sno = request.GET['sno']
        subject = Subject.objects.get(no=sno)
        queryset = Teacher.objects\
            .filter(subject__no=sno).defer('subject')