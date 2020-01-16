# day第一天 

### gogogo

查询多对多

`queryset = Agent.objects.all().prefetch_related('estates')`

查询

```python
# views.py
@cache_page(timeout=300)
@api_view(('GET', ))
def get_cities(request, pid):
    queryset = District.objects\
        .filter(pid=pid).only('distid', 'name')
    serializer = DistrictSimpleSerializer(queryset, many=True)
    return Response(serializer.data)

# serializers.py
class DistrictSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ('distid', 'name')
```



```python
# FBV - 基于函数的视图(昨天的内容)
# CBV - 基于类的视图(不推荐)

class EstateView(ListAPIView/APIView):
    queryset = Estate.objects.all().defer('district', 'agents')
    serializer_class = EstateSerializer
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            cls = RetrieveAPIView
        else:
            cls = ListAPIView
        return cls.get(self, request, *args, **kwargs)

# 映射URL
urlpatterns = [
    path('districts/', get_provinces),
    path('districts/<int:pid>/', get_cities),
    path('agents/', get_agents),
    path('estates/', EstateView.as_view()),
    # 注意这里的pk是约定参数，不能随意修改
    path('estates/<int:pk>/', EstateView.as_view()),  
]
```

### 根据自己不同的需求定制序列化器

### 提交表单(fetch发POST表单) - 拓展GET表单 

```js
// fetch的POST表单
addEstate(){
	fetch('/api/estates/', {
    	method: 'POST',
    	body: JSON.stringify({
        	'name': this.form.name,
        	'hot': this.form.hot,
        	'intro': this.form.intro,
        	'district': this.countyId
    	}),
      	headers: {
            'countent-type': 'application/json'
      	}
	}).then(resp => {
        if (resp.status == 201){
            this.$message({
                message: '新增楼盘成功',
                type: 'success'
            })
        } else {
            message = {
                message: '新增楼盘失败',
                type: 'error'
            }
        }
        this.$message(message)
	})
}

// 拓展fetch的GET表单

```

### postman postwoman requests(请求)

```python
# requests测试API
import json
import requests

resp = requests.get('http://localhost:8000/api/estates/')
estates = json.loads(resp.text)
for index, estate in enumerate(estates):
	print(index, estate)
```



### 更快的API创建方法

```python
# views.py
class HouseTypeViewSet(ModelViewSet):
	queryset = HouseType.objects.all()
	serializer_class = HouseTypeSerializer
	
# serializers.py
class HouseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseType
        fields = '__all__'
```

### 分页

```python
# CBF分页
# 配置全局分页和单独不分页和分页
# FBV分页

```



---

### 下午开工

- 设置游标分页

```python
# CBV 类下
pagination_class = MyCursorPagination

# serializers.py
class MyCursorPagination(CursorPagination):
	ordering = 'estateid'
```



- 缓存

  函数FBV/类CBV

  ```python
  # CBV实现缓存
  drf-extensions==0.5.0
  # 类加父类 CacheResponseMixin - mixin混入类 - 往前写
  # 添加配置
  REST_FRAMEWORK_EXTENSIONS = {
      'DEFAULT_CACHE_RESPONSE_TIMEOUT': 120,
      'DEFAULT_USE_CACHE': 'default',
      'DEFAULT_OBJECT_CACHE_KEY_FUNC': 'rest_framework_extensions.utils.default_object_cache_key_func',
      'DEFAULT_LIST_CACHE_KEY_FUNC': 'rest_framework_extensions.utils.default_list_cache_key_func',
  }
  # 类里的函数装饰器
  @cache_response(timeout=120, key_func=default_list_cache_key_func)

  --------------------
  # 方法二 - 给类装上装饰器,(name=类中的方法名) - django原生缓存
  @method_decorator(decorator=cache_page(timeout=600), name='list')
  @method_decorator(decorator=cache_page(timeout=600), name='retrive')

  # 解决不同网页缓存不一样的问题
  # settings -> CACHES
  'KEY_FUNCTION': 'common.utils.make_key',
  # utils.py
  import re
  PATTERN = re.compile(r'(\.[0-9a-f]{32})')

  def make_key(key, key_prefix, version):
      items = PATTERN.findall(key)[1:]
      for item in items:
          key = key.replace(item, '')
      return '%s:%s:%s' % (key_prefix, version, key)
  ```

- 数据筛选与排序(*)

```python
# django原生
def get_queryset(self):
    distid = self.request.GET.get('district')
    if distid:
        self.queryset = self.queryset.filter(district=distid)
    ordering = self.request.GET.get('ordering')
    if ordering:
        self.queryset = self.queryset.order_by(ordering)
    return self.queryset

# 三方库
# 自定义类
fileterset_class = EstateFileterSet

class EstateFileterSet(django_filters.FilterSet):
    intro = django_filters.CharFilter(lookup_expr='contains/startwith/endwith')
    minhot = django_filters.NumberFilter(field_name='hot', lookup_expr='gte')
    # Goods.objects.filter(price__lte=100)
    maxhot = django_filters.NumberFilter(field_name='hot', lookup_expr='lte')

# or
class EstateFileterSet(django_filters.FilterSet):
    """自定义FilterSet"""
    minhot = django_filters.NumberFilter(field_name='hot', lookup_expr='gte')
    maxhot = django_filters.NumberFilter(field_name='hot', lookup_expr='lte')
    keyword = django_filters.CharFilter(method='filter_by_keyword')
    
    @staticmethod
    def filter_by_keyword(queryset, key, value):
        queryset = queryset.filter(Q(name__contains=value) |
        							Q(intro__startswith=value))
        return queryset
```

- API限流(DRF可以限制，但不好) 

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_THROTTLE_CLASSES': (
    	'rest_framework.throttling.AnonRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/min',
        # 'user': '10000/day',
        # '1/sec',
    }
}

# or
# CBV类下
throttle_classes = ()  # 不限流
```



### 毕业任务：6篇博客，3篇视频 /-/11周

- 展示房源，搜索房源












---

### 提问：

1.serializers.py 文件的意义：序列化器

2.基于类的视图不推荐的原因：

3.序列化的字段选择：

4.关于继承的使用：

5.异步请求局部刷新(API和异步中间的联系)