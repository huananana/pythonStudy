# Redis

[TOC]

### a

CVS / VSS ---> 锁定模式
Subversion (SVN) ---> 合并模式 + 中央服务器
BitKeeper / Git ---> 合并模式 + 分布式版本控制



Multics ---> Unics ---> Unix
Unix ---> MINIX ---> Linux ---> Android
Unix ---> BAS ---> FreeBSD ---> macOS ---> ios
Unix ---> AIX / Hp-Unix / Solaris
ken thompson ---> B
dennis ritchie ---> C 



lloogg.com ---> LAMP = Linux + Apache +  MySQL + PHP

LNMP = Linux + Nginx +  MySQL + PHP

Remote Dictionary Server ---> KV存储系统

GitHub ---> 3.x ---> 5.x



缓存系统缓解关系型数据库的访问压力

命令 & ---> 将命令放到后台运行

jobs 查看后台运行的命令

fg %编号 将后台命令放到前台运行

Ctrl + z ---> 将前台命令暂停并放到后台

bg %编号 ---> 将暂停的命令在后台运行



Linux 系统启停服务
yum install -y nginx

​	~ 启动：systemctl start nginx
​		service nginx start
​	~ 停止：systemctl stop nginx
​		service nginx stop
​	~ 重启：systemctl restart nginx
​	~ 查看状态：systemctl status nginx
​	~ 开机自启：systemctl enable nginx
​	~ 禁用自启：systemctl disable nginx



加密技术：
 	~ 对称加密：加密和解密使用相同的密钥 - AES
​	~ 非对称加密：加密和解密使用不同的密钥(公钥和私钥) - RSA
​	PyCrypto



生成密钥
ssh-keygen -t rsa -b 2048 -C “940665932@qq.com”

项目的依赖项文件:

​	~ pip freeze > requirements.txt
​	~ pip install -r requirement.txt 



上传版本的忽略文件处理

在项目下新建文件.gitignore
在文件里输入要忽略的文件名



端口 0-65535 

2^16-1



### 1.Linux安装软件

###### 1.包管理工具

```
- yum CentOS
    ~ yum search nginx	查询
    ~ yum install nginx	安装
    ~ yun erase nginx / yum remove nginx 卸载
    ~ yum info nginx  包信息
    ~ yum list installed|grep nginx   

- rpm Redhat
	~ rpm -ivh 下载的rpm包文件名
	~ rpm -e
	~ rpm -qa
	
- apt Ubuntu
```

###### 2.源代码构建

```
# 安装redis-5.0.7
wget http://download.redis.io/releases/redis-5.0.7.tar.gz
gunzip redis-5.0.7.tar.gz
tar -xvf redis-5.0.7.tar
cd redis-5.0.7
make && make install

# 安装git-2.24.1
wget http://mirrors.edge.kernel.org/pub/software/scm/git/git-2.24.1.tar.xz
xz -d git-2.24.1.tar.xz
tar -xf git-2.24.1.tar
cd git-2.24.1
yum install -y libcurl-devel
./configure --prefix=/usr/local
make && make install
# 以上为手写，可能有误差，仅作参考
```



### 2.redis的启动与关闭

###### 1.启动redis服务

`redis-server --requirepass 口令 >> redis.log &`

###### 2.进入redis

`redis-cli -p 端口 -h 主机`

###### 3.关闭redis

`pkill redis-server` or `killall redis-server`



### 3.redis常见指令

```
set key value ex 120 		---> 添加键值对
get username 				---> 通过键查找值
ttl username 				---> 查看键过期时间
expire username 300 		---> 设置键过期时间
keys *						---> 查看所有键
dbsize 						---> 查看数据库大小(键值对数量)
select id 					---> 切换数据库
save 						---> 保存数据
bgsave 						---> 后台保存数据
flushdb 					---> 清空当前数据库的数据
flushall 					---> 清空所有数据库的数据
exists 						---> 判断指定的键是否存在
type 						---> 查看键对应的值得数据类型
```

### 4.redis数据类型

###### 1.命令大全

[redis命令](redisdoc.com)

###### 2.redis的核心数据类型-字符串

```
set key value 					---> 添加键值对
get key 						---> 通过键查看值
strlen key 						---> 获取字符串长度
append key value2 				---> 给字符串追加内容
mset key1 value1 key2 value2 	---> 获取字符串长度
mget key1 key2 					---> 查看多个键对应的值
incr key 						---> 值加1
incrby key value 				---> 值加上value
decr key 						---> 值减1
decrby key value 				---> 值减去value
getrange key start end 			---> 获取字符串指定范围的字串
setrange key offset  value 		---> 修改字符串指定位置的内容 
```

###### 3.redis的核心数据类型-哈希(字典)

```
hset key field value 					---> 添加hash类型键值对
hmset key field1 value1 field2 value2 	---> 添加多组hash类型键值对
hget key field 							---> 获取hash类型字段对应的值
hmget key field1 field2 				---> 获取hash类型多个字段对应的值
hgetall key 							---> 获取hash类型所有的字段和对应的值
hkeys key		 						---> 获取hash类类型所有的字段
hvals key 								---> 获取hash类型所有字段的值
hexists key field 						---> 判断hash类型某个字段是否存在
```

###### 4.redis的核心数据类型-列表

```
lpush key value1 value2 value3 			---> 在左边添加元素
rpush key value1 value2 value3 			---> 在右边添加元素
lpop key 								---> 从左边移除一个元素
rpop key 								---> 从右边移除一个元素
lrange key start end 					---> 查看泪飙指定范围的元素
llen key  								---> 查看列表元素个数
lindex key index 						---> 查看列表指定位置元素
lrem key count value	 				---> 删除列表中指定元素
```

###### 5.集合

```
sadd key value1 value2 value3 			---> 添加元素
srem key value							---> 删除元素
spop 									---> 获取随机元素
scard key 								---> 查看元素个数
smembers key 							---> 查看所有元素
sismember key value 					---> 查看集合中是否有指定值
sinter key1 key2 						---> 交集
sunion key1 key2 						---> 并集
sdiff key1 key2 						---> 差集
```

###### 6.有序集合

```
zadd key score1 mem1 score2 mem2 		---> 添加元素
zrem key mem 							---> 删除元素
zrange key start end 					---> 按score的升序查看元素
zrevrange key start end 				---> 按score的降序查看元素
zscore key mem 							---> 查看元素对应的score
zincrby key count value 				---> 修改元素的score值
```

###### 7.地理位置

LBS应用 - Location-Based Service - 基于位置的服务

`geoadd key longitude(经) latitude(纬) member(地点)`