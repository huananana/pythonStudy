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

