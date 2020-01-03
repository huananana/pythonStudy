# jQuery

### 1.jQuery介绍

> jQuery本质就是一个用js封装的库，里面更装了很多方法和对象让网页开发更简单
>
> jQuery是通过jQuery对象来提供功能



### 2.怎么导入jQuery

1)本地导入 - 下载jQuery导入

2)远传导入 - `<script type="text/javascript" src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>`



### 3.使用jQuery

```html
1.获取节点
1)元素/id/后代/群组选择器
	$('div')
	$('#div1')
	$('#div1>p')
2)特殊选择器
	$('p+a') - a标签(紧跟在p后面的a标签)
	$('#p1~*') - p1后面(所有)的兄弟标签
	$('p:first') - 第一个p标签(last最后一个p标签)
	$('div *:forst-child') - 所有div的第一个子标签(last-child最后一个子标签)
```
	2.节点操作
	1)创建节点
		$('<p>段落内容</p>') - HTML代码
	
	2)添加节点
		$().append() - 在jQuery对象中的最后添加
		$().prepend() - 在jQuery对象中的最前添加
		$().before() - 在jQuery对象的前面添加
		$().after() - 在jQuery对象的后面添加
	
	3)删除节点
		$().remove() - 删除jQuery对象
		$().empty() - 删除jQuery对象的所有子节点
	
	4.拷贝节点
		$().clone(true/false) - 深浅拷贝(区别是jQuery中的事件)
	1.特殊属性
		$().text() - 获取标签内容(添加参数:'修改值')
		$().html() - 获取标签内容(添加参数:'修改值')
		$().val() - 获取value值(添加参数:'修改值')
	
		$().addClass('class') - 添加class属性
		$().removeClass('class') - 删除class属性
	
	2.样式属性(CSS)
		$().css() - 获取/设置样式属性值(参数:'修改值')
		$().css({
			css代码 - 属性改为CSS的驼峰式命名(加引号可以正常使用)
		})
	
	3.普通属性
		$('选择器').attr('参数', '属性值') - 获取/修改属性值(参数:'属性名', '值')
		
	1.事件绑定
		$().on('事件', function(){
			# 事件中重要:this,是js类型的事件源
		})
		
		$().on('事件', '选择器下的标签类型', function(){
			# 事件可以绑定新的标签
		})
	
	2.事件捕获
		evt.stopPropagation()  # 当标签中嵌套子标签时，子标签时，点击子标签的范围，会触动父标签的点击事件
### 3.Ajax使用

1.什么是Ajax

> asynchronization - JavaScript - xml(异步js)
>
> Ajax是由jQuery封装的专门用来做http请求的相关方法，和python中的第三方库requests的功能一样

```
框架：
$.ajax({
			 	url:数据接口地址,
			 	type:请求方式(get/post),
			 	data:请求数据/参数(客户端传递给服务器的数据, 值是对象),
			 	success:请求成功的回调函数(函数),
			 	error:请求失败的回调函数
			 })
```

实例：



```html
<script type="text/javascript">
	$.ajax({
        type:"get",
        url:"http://rap2api.taobao.org/app/mock/233723/shopping",
        data:{username:'小明', password:'123456'},
        success:function(result){
            console.log('请求成功！')
            console.log(result)
            for(var goods of result.data){
                var name = goods.name
                $('#box').append($('<p>'+name+'</p>'))
                $('#box').append($('<img src="'+goods.goods_image+'" />'))

            }
        },
        error: function(){
            console.log('请求失败')
        }
    });
</script>

<--> 另一种方法？</-->
<scipt type="text/javascript">
	$.get("http://rap2api.taobao.org/app/mock/233723/shopping", {username:'小明', password:'123456'}, function(result){	
		console.log('=====:', result)
	})
</scipt>
```