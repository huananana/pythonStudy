-- ===1.内连接和外连接===
-- 1.1 内连接
-- 之前的连接就是内连接，有两种写法
-- 写法一：select * from 表1，表2，... where 连接条件 查询条件;
-- 写法二：select * from 表1，inner join 表2 on 表2连接条件 inner join 表3 on 表3连接条件 ... where 查询条件;
-- 注意：如果不写连接条件，就是按 “笛卡尔积” 进行连接 ；写法2中表1是连接后面表的媒介

-- 1.2 外连接：
-- 在mysql 中只支持左外连接(left join)和右外连接(right join)
-- 表1 left join 表2：先将表1的记录全部取出，按连接条件依次连接表2中的记录；1)表2中没有满足表1的记录，表1对应位置为null；2)表2中有的记录，表1没有是不会被记录的；
-- 表1 right join 表2：将表2的记录全部取出来，按连接条件去依次连接表1中的记录，表2中的记录找不到满足条件表1记录那么连接的内容就是空

 -- 

-- ===2.DCL(数据控制语言)===
-- DCL主要提供授权和召回授权以及事务等相关功能
-- 1.用户管理(root账号才有的权限)
-- 1)创建用户
-- create user '用户名'@'登陆地址'; - 创建数据用户，该用户登录不需要密码
-- create user '用户名'@'登陆地址' identified by '密码'
-- 说明：用户名 - 见名知义; 登陆地址 - ip地址/localhost(本机)/%(任意地理位置)

create user '一号打杂小姐姐'@'localhost' identified by 'xjj&272727';

-- 2)删除用户
-- drop user 用户名;
drop user '一号打杂小姐姐'@'localhost';

-- 2.授权管理
-- 1) 授权
-- grant 权限类型 on 数据库.表 to 用户名;
-- 说明: 权限类型 insert,delete,update,select,all privileges(所有权限，慎重！！！)
grant select on school.tb_student to '一号打杂小姐姐'@'localhost';

-- 2) 召回授权
revoke select on school.tb_student from '一号打杂小姐姐'@'localhost';

-- 3.事务
-- 如果完成一个任务需要多个操作，但是要求多个操作中只要有一个失败，整个任务取消，让数据库回到开始状态。
-- 只有所有操作都成功，数据库才更新。
-- 


use school;

-- 开启事务环境
update tb_student set stubirth=curdate()


-- ===3.视图===
-- 视图是用来存储一个sql查询语句的结果；
-- create view 视图名 as sql查询语句;

-- 练习：创建学生表的视图:要求这个视图不能看到生日，


CREATE VIEW test AS SELECT
	stuid,
	stuname,

IF (stusex, '男', '女'),
 collname,
 stuaddr
FROM
	tb_student,
	tb_college
WHERE
	tb_student.colid = tb_college.collid;


drop view test;

-- ===4.索引===
-- 索引就像书的目录，记录了数据的位置，可以提高查询速度。(空间换时间)
-- 一般需要给使用频率高的字段添加索引。(主键自带索引-唯一索引)

-- 4.1 添加索引
-- create index 索引名 on 表名 (字段) - 给指定字段添加普通索引
-- create unique index 索引名 on 表名(字段) - 给指定字段添加唯一索引(字段值是唯一的时候才能添加唯一索引)

-- 4.2 删除索引
-- alter table 表名 drop index 索引名;

-- explain - 获取sql语句的执行计划(主要用于检测sql语句的性能)
