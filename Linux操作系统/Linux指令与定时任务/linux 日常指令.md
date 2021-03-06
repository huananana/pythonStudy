# 1.日常指令

##### 1.cd指令 -  进入文件夹

cd 文件夹路径(路径可以是绝对地址也可以是相对路径) - 进入到指定路径对应的文件夹

cd .. - 返回上层目录

cd /  - 进入操作系统根目录

cd ~ - 进入电脑的文件系统根目录



##### 2.ls指令 - 显示当前目录中的内容

```
ls 直接显示当前文件夹中的内容的名字(隐藏文件和文件夹看不到)
ls -l/lh 显示当前文件夹中的内容和内容的基本信息(隐藏文件和文件夹看不到)
ls -a 显示当前文件夹中所有的内容(包括隐藏文件)
ls -R 递归显示当前目录以及当前目录下所有的子目录中的内容
ls -S/-t 显示文件夹中的内容，并且内容按大小/时间从大到小排序
-------------------------------------
ls -A 列出除.及..的其它文件
ls -r 反序排列
ls -t 以文件修改时间排序
ls -h 以易读大小显示
---------------组合显示---------------------
ls -Sr 按大小从小到大排序
ls -Srlh 按大小从小到大排序，并且显示内容的基本信息
```

##### 3.pwd指令

pwd - 查看当前目录的绝对路径(系统目录下的)

##### 4文件操作

1) touch指令 - 新建文件

touch 文件路径 - 在指定位置创建指定文件

```
touch a.txt - 在当前目录下新建一个文件a.txt
touch ../a.txt - 在当前目录的上层目录新建一个a.txt
touch /home/a/a.txt - 在根目录下home目录中的a目录里面创建
```

2) cat指令 - 查看文件内容(读文件)

cat 文件路径 - 读取指定路径对应的文件的内容



3) vim指令

vim 文件路径 - 使用vim(是一个工具)打开文件

##### 5.文件夹操作

1) mkdir指令 - 新建文件夹

mkdir 文件夹路径 - 在指定位置创建文件夹

mkdir -p 文件夹路径 - 在指定位置创建文件夹(会创建目录中所有不存在的文件夹)

```
mkdir -p a/b/c	a,b,c可以都没有，会在现在当前目录中创建a，在a中创建b，b中创建c

mkdir -p a/{b，c}		a,b,c可以都没有，会在当前目录中创建a，在a中创建b和c
```

##### 6.删除文件和文件夹

1)rm指令 - 删除文件和文件夹

rm 文件路径    -    删除指定文件(删除的时候会询问是否确定删除，y-同意，n-不同意)

rm -f 文件路径    -    删除指定文件(删除的时候不询问)

rm -r 文件夹路径	-	删除指定文件夹



2)rmdir指令	-	删除空目录

rmdir	文件夹路径	-	删除指定文件夹(这个文件夹必须是空的)



3)cp指令	-	拷贝

cp 文件路径1	文件路径2	-	将文件路径1指定的文件中的内容复制到文件路径2指定的文件中(文件路径2对应的文件本身是不存在的)

​						-	将文件1中的内容复制粘贴到文件2(如果文件2不存在，会自动创建；如果存在会询问是否覆盖)



cp 文件路径	文件夹路径	-	将指定文件复制粘贴到指定文件夹中

cp -r 文件夹路径1 文件夹路径2	-	将文件夹1复制粘贴到文件夹2中



4)mv指令	-	移动

mv 文件路径1 文件路径2	-	将文件1移动文件2所在的位置

```
mv 文件名1 文件名2	-	对文件进行重命名(将文件名1修改为文件名2)
mv a.txt b.txt	-	将当前文件夹中的a.txt重命名为b.txt
mv /home/a.txt /home/b.txt	-	将系统根目录下home文件中的a.txt重命名为b.txt
```

mv 文件路径/文件夹路径 文件夹路径	-	将文件/文件夹直接移动到指定文件夹中



##### 7.history指令	-	获取历史记录(指令的历史记录)

history	-	显示当前系统已经执行过的所有的指令

```shell
#如果想要显示历史记录的时候显示指令执行的时间需要修改~/.bashrc文件：
export HISTTIMEFORMST="[%y-%m-%d_%T] "

# 修改完成后需要通过指令：source ~/.bashrc 去执行这个配置文件，最后历史记录
```



##### 8.创建链接

1)创建软链接

ln -s 源文件路径路径 软链接文件地址	-	给源文件在指定文职创建一个软链接(软链接本质就是用来保存源文件绝对地址的一个文件，可以理解为windows中的快捷方式)

注意：源文件路径必须写绝对路径

如果删除或者移动源文件，软链接会直接无效



2)创建硬链接

ln 源文件路径 硬链接文件地址	-	给源文件在指定位置创建一个硬链接

硬链接的本质就是源文件内容的另外一个引用，所以删除或者移动源文件硬链接任然有效，只是删除硬链接会变成普通文件



##### 9.快捷键



ctr + a	-	回到行首

ctr + e	-	回到行尾	

ctr + u	-	向左删除全部

ctr + k	-	向右删除全部

ctr + y	-	粘贴上次删除的内容

ctr + l	-	清屏



##### 10.进程相关指令

1)ps 指令

ps	-	查看进程状态

ps -aux	-	查看当前所有的进程的信息

ps grep 进程名/进程ID	-	根据进程名/进程ID查看指定进程

2) top指令

top	-	实时查看当前所有的进程信息和系统信息

top -p PID1,PID2,...	-	实时检测指定的进程

3)free指令

free	-	显示当前系统的内存信息，显示的时候以kb为单位

free -单位	-	显示当前系统的内存信息，以指定单位来显示

4)kill 指令

kill 进程ID	-	杀掉指定id对应的进程

kill -1/-9/-15 进程ID	-	以指定的方式(-1表示不间断重启;-9表示强制杀死进程;-15表示正常结束进程)杀掉指定进程



pkill 进程名	-	杀死指定进程名对应的进程(中介可以加-1/-9-15)

killall 进程名	-	杀死和进程名相关的所有进程



5)uptime指令

uptime	-	获取系统信息



##### 10.用户管理

一个Linux操作系统可以有多个用户(user),也可以有多个用户组(group);用户和用户之间的关系是多对多

users - 查看当前用户

groups - 查看当前分组

groupadd - 分组名 - 创建分组(管理员才能创建;可以通过查看/etc/group文件来查看当前系统所有的分组)



useradd 用户名 - 创建指定用户(1.用户创建成功后系统会自动在/home目录下创建一个和用户名同名的文件夹；2.会自动创建和用户名同名的分组，并且将当前用户添加到这个分组中)



useradd -G 分组1,分组2,...用户名 - 创建指定用户，并且将用户添加到指定分组中

usermod - G 分组1,分组2 用户名 - 修改用户分组



passwd 用户名 - 修改用户密码(需要root权限)



su 用户名 - 切换账号(root登陆的时候切换不需要密码，其他账号需要)

exit - 退出当前帐号



sudo - 在命令前sudo是以管理员身份执行指令

注意：不是所有的用户都可以通过sudo来以管理员身份执行指令，如果想要能够使用sudo必须添加配置

​	a.Ubuntu: 将需要有管理员身份的账号添加到sudo分组中

​	b.redhat和contos：在/etc/sudoers配置文件中添加代码：

```shell
## Allow root to run any commands any where
root	ALL=(ALL)	ALL    #(默认有的)
用户名    ALL=(ALL)	ALL	   #(自己添加的，xiaoming是用户名)
```

##### 11.文件权限

文件类型 - --- --- ---

| 文件类型  | 所有者权限        | 同组用户权限 | 其他用户权限 |
| ----- | ------------ | ------ | ------ |
| d(目录) | r w x - 读写执行 | ...    | ...    |
| -(文件) | ...          | ...    | ...    |
| l(链接) | ...          | ...    | ...    |

默认情况下文件和文件夹的权限：文件所有者有读写权限，同组用户和其它用户都是只读权限。

1) chmod指令

chmod 权限值 文件路径 - 将指定文件的权限修改成指定值

```
权限：		rwx r-- rw-
权限二进制 111 100 110
权限值：    7   4   6
chmod 746 文件路径

权限：		rwx rwx rwx
权限值：	7	7	7
chmod 777 文件路径
```

chmod [a,u,g,o]/[+-]/[r.w.x] 文件地址 - 给指定文件对应指定用户添加或者删除指定权限

​			(a-所有用户，u-文件所有者，g-同组用户，o-其他用户；

​			+表示添加权限，-表示删除权限；

​			r-读，w-写，x-执行)

```shell
chmod a-x 文件地址	# 删除所有用户的执行权限
chmod u+w 文件地址  # 给文件所有者添加写的权限
```



##### 12.日志管理

###### 1)显示文件内容

1) cat指令 - 直接显示文件中所有的内容

cat文件 - 直接查看文件所有内容

2)查看部分内容

head -n N 文件地址 - 显示指定文件前N行内容

tail -n N 文件地址 - 显示指定文件后N-1行内容

3)分页显示

less文件 - 显示文件内容(通过快捷键控制内容显示过程)

less -N 文件 - 显示文件内容，每次翻页的时候翻N行

more -N 文件 - 按页显示文件内容，每次翻页的时候翻N行

快捷键：

​	-按j向下

​	-k向上

​	-f向下翻屏

​	-b向上

​	-g到全文开头

​	-G全文结尾

​	-按Q退出

more[-N]文件 - 和less差不多，这个是尽可能多，less是尽可能少的加载



总结：查看文件内容的时候可以加参数-n，让内容在显示的时候显示行号



###### 2)结果的处理

凡是有打印结果的指令，我们都可以通过相关指令对结果进行处理

a.管道 - |

如果需要对某一个指令的结果使用另外的指令进行二次处理的时候，需要用到管道(|)



b.sort - 排序

sort - 从小到大排序(将一行内容作为一个字符串，按字符串大小对应内容进行排序，默认不区分大小写)

```shell
cat a.text |sort - 对a.txt的文件内容从小到大排序显示

sort的参数：
-r - 逆序
-nk 1 - 数值大小排序
-nk 2 - 字符大小排序(默认)
```



c.uniq - 去重

uniq - 只能将紧挨着的相同行去掉重复的(如果需要去掉所有重复的行，先排序将相同的行放到一起)

```
cat a.txt|uniq - 去掉a.txt文件内容中相邻重复的行
cat a.txt|sort|uniq - 去掉a.txt文件内容中所有重复的行
```



d.awk - 获取列

awk'{print $N}' - 获取内容中第N列的数据

```
history|awk '{print $2}' - 获取历史记录第2列的内容
history|awk '{print $2,$3}' - 获取历史记录第2列和第3列的内容
```



练习：

```shell
history |awk '{print $4}' |sort |uniq -c | sort -rnk 1 | head -n 3	# 统计最常用的3个指令及其使用次数
```



###### 3) 输出重定向 - >/>>

执行有打印结果的指令 >文件地址 - 将结果保存到指定文件中(w的方式添加)

... >> ... (a的方式添加)

```shell
history > a.txt # 将当前历史记录直接保存到a.txt文件中

# 将最常用的3个指令及其使用次数保存到a.txt文件中
history |awk '{print $4}' |sort |uniq -c | sort -rnk 1 | head -n 3 > a.txt
```



###### 4)统计

wc -c/-w/-l 文件地址 - 统计指定文件中字符/单词/行的数量



###### 5)查找

grep - 找内容

a. grep 内容 文件地址 - 在指定文件中查找指定内容(返回文件中所有包含指定内容的行)

```
grep you a.txt # 获取a.txt中包含you的所有的行

grep的参数：
-n	- 显示结果的时候显示行号
-i 	- 查找内容的时侯忽略大小写
-E	- 按正则表达式进行匹配
		使用方法：grep -E '正则表达式'文件
		注意：Linux操作系统中正则表达式不支持：\d,\D,\w,\W,\s,\S,\b,\B;其它语法都支持
-v	- 忽略字段
		grep you a.txt -v # 获取a.txt中不包含you的所有的行

```

b. 执行有打印结果的指令|grep 内容 - 在指令执行结果中查找指定内容

c. grep -r 内容 文件夹地址 - 在指定文件夹中所有的文件中查找指定内容

find - 找文件

find 文件夹路径 - name 文件名 - 在指定文件夹下按文件名找指定文件

```shell
# 找指定文件名
find dir1 -name 'test1.py'	# 在文件夹dir1找名字是text1.py的文件
dind dir1 -name '*.txt'		# 在文件夹dir1找后缀是txt的所有文件
find dir1 -name 'test*.txt'
find dir1 -name 'test*'
find dir1 -name '*c.txt'
```

find 文件夹路径 -size +/-文件大小 - 在指定文件夹下找文件大小满足条件的所有的文件

```shell
find dir1 -size +4k		# 查找在文件夹dir1中所有大于4k的文件
find dir1 -size -4k 	# 查找在文件夹dir1中所有小于4k的文件
find dir1 -size +5k -size -10k	# 查找在文件夹dir1中所有大于5k并且小于10k的文件(文件大小如果是小数，算的时候向上取整)
find dir1 -size +4k -name '*.txt' 	# 查找在文件夹dir1中所有大于4k的txt文件
```



###### 查指令

whatis 指令名 - 查看该指令说明

which 指令名 - 精确查找当前指令对应的文件的路径

whereis 指令名 - 查找和指定指令相关的所有的文件的路径

`man` 指令名 - 获取指定指令的使用手册

指令名 - help - 获取指定指令的帮助文档



##### 13.网络管理

ifconfig  -  查看网卡状态

netstat -natp -查看当前系统所有的网络连接状态

netstat -natp|grep 端口号 - 查看指定端口对应的网络连接状态



ping 地址 - 该指定地址对应的服务器发送数据(主要用来检测当前网络通不通)

ping -i 时间(单位秒) 地址 - 每个指定时间ping一次(时间可以是小数)

ping -c 次数 地址 - ping指定次数

telnet ip地址 端口 - 查看远程主机网络连接状况(需要telnet环境) - 不用

** wget 地址 - 下载



##### 14.压缩和归档

压缩可以让文件变小，一般在文件需要传输前都会先对文件进行压缩，注意，压缩指令只针对文件有效，并且一次只能压缩一个文件

归档可以将一个文件夹变成一个文件(tar文件)

###### 1)归档和解归档 - tar (既可以对文件进行归档也可以对文件夹归档)

`tar -cvf` 归档文件地址 -  需要归档的源文件地址 - 将文件进行归档操作

`tar -xvf` 归档文件地址 - 将指定的归档文件解归档



###### 2) 压缩和解压：gzip,gunzip,xz

a.gzip    

----压缩----

`gzip` 文件地址 - 压缩指定文件 (压缩后会生成一个gz文件，并且会删除原文件)

gzip -c 文件地址> 压缩文件地址 - 将指定文件压缩指定文件，并且保留原文件

----解压----

gzip -d 压缩文件地址 - 解压指定文件(解文件后会删除原压缩文件)

----查看压缩文件----

gzip -l 压缩文件地址 - 列出压缩文件中的内容



b.gunzip

`gunzip` 压缩文件地址 - 解压指定文件(解压文成后会删除原压缩文件)



c.xz

xz 文件地址 - 压缩指定文件(压缩文件后缀xz)

xz -d 文件地址 - 解压缩指定文件



##### 15.软件安装和包管理工具

Linux的包管理工具是yum，



###### 1.源代码构建python3.x

```shell
[root ~]# yum install gcc (安装编译环境)
[root ~]# wget https://www.python.org/ftp/python/3.6.5/Python-3.7.5.tgz		(下载安装包)
[root ~]# gunzip Python-3.7.5.tgz	(解压)
[root ~]# tar -xvf Python-3.7.5.tar		(解归档)
[root ~]# cd Python-3.7.5	(进入安装包)
[root ~]# ./configure --prefix=/usr/local/python37 --enable-optimizations		(设置安装路径)
[root ~]# yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel	(安装相关依赖库)
[root ~]# make && make install		(编译执行安装文件)
...
[root ~]# ln -s /usr/local/python37/bin/python3.7 /usr/bin/python3		(给python指令文件创建快捷方式python3)
[root ~]# python3 --version
Python 3.7.5
[root ~]# python3 -m pip install -U pip		(安装pip)
[root ~]# ln -s /usr/local/python37/bin/pip /usr/bin/pip3		(给pip指令创建快捷方式pip3)
[root ~]# pip3 --version
```

