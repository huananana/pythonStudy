-- 1.sql基础
-- sql又叫结构化查询语言，分为三大类：DDL(数据定义语言)、DML(数据操作语言)、DCL(数据控制语言)
-- DDL：create(创建数据库和表)、drop(删除数据库和表)、alter(修改表)
-- DML：insert(增)、delete(删)、update(改)、select(查)
-- DCL：grant(授权)、revoke(召回授权)
-- sql的注释实在注释前加--
-- sql的关键字不区分大小写
-- sql语句结束后需要加分号
-- ---------------------------------DDL(数据定义语言)---------------------------------
-- 1.create的使用(写了三种,只掌握最后一种即可)
-- 语法：create database 数据库名称;		-	创建指定数据库，如果这个数据库已经存在，会报错
-- 语法：create database if not exists 数据库名称；	- 当指定数据库不存在的时候创建对应的数据库
-- 语法：create database if not exists 数据库名称 default charset utf8;	- 创建数据库的时候指定数据库文件编码方式
-- 2.删除数据库
-- 语法：drop database 数据库名称;
-- 语法：drop database if exists 数据库名;  {if exists -> 如果存在数据库;代码意义：避免删除空的数据库而出现的错误提示}  
-- 3.切换/使用数据库
-- 语法：use 数据库; - 切换/使用指定数据库;切换后所有数据库相关操作都是针对这个数据库{注意的是：建表之前一定要先切换到你想要操作的数据库中}
-- ---表的操作---
-- 1.创建表(数据库文件是通过表来存数据)
-- 语法：crate table if not exists 表名(字段名1 类型名1 约束1, 字段名2 类型名2 约束2, ...) {注意：1.约束可无可多,约束可以单独添加(语法：约束(字段))}
-- 表名：程序员自己命名，要求见名知义，一般需要加前缀t_/tb_表示这是一个表
-- 字段名：程序员自己命名，要求见名知义；值得注意的是必须有一个字段作为主键(唯一，不能为空，一般为int类型)(意义：为每行数据赋予id)
-- 类型名：必须是数据库支持的类型；常见类型：int(整型)、float(浮点型)、varchar(字符串)/text(字符串)、bit(布尔0-false,1-true)、date(ymd)/datetime(ymdhms)
-- 约束：not null(不能为空),unique(唯一约束),default(默认值约束),primary(主键约束),foreign key(外键约束),auto_increment(自动增长)
-- 2.删除表
-- 语法：drop table if exists 表名;	- 删除指定表
-- 3.修改表
-- 添加删除字段
-- 语法：alter table 表名 add/drop column 字段名 字段类型 字段约束;
-- 修改字段名
-- 语法：alter table 表名 change 原字段 新字段 新类型;
-- 添加删除约束
-- 语法：
-- ==========实例==========
-- 实例1：创建school数据库
CREATE DATABASE
IF NOT EXISTS school DEFAULT charset utf8;

-- 实例2：删除school数据库
DROP DATABASE
IF EXISTS school;

-- 实例3：切换数据库
USE school;

-- 实例4：创建表tb_stu
CREATE TABLE
IF NOT EXISTS tb_stu (
	stu_id INT PRIMARY KEY auto_increment,
	stu_name VARCHAR (20) NOT NULL,
	stu_brith date,
	stu_sex bit DEFAULT 1,
	stu_tel VARCHAR (11) UNIQUE
);

-- 实例5:删除表tb_stu
DROP TABLE
IF EXISTS tb_stu;

-- 实例6:添加/删除字段
ALTER TABLE tb_stu ADD COLUMN stu_addr VARCHAR (200);

ALTER TABLE tb_stu DROP COLUMN stu_addr;

-- 实例7：修改字段名
ALTER TABLE tb_stu CHANGE stu_tel stu_newtel VARCHAR (11);

-- 实例8：添加删除约束
-- ...
-- ---------------------------------DML(数据操作语言)---------------------------------
-- 数据操作主要提供表中数据的增删查改操作
-- 1.insert(增)
-- 语法1：insert into 表名 values(值1,值2,...); {值按表中字段的顺序一次给每个字段赋值，最终形成一条新的记录}
-- 语法2：insert into 表名 (字段名1, 字段名2, ...) values (值1, 值2, ...); { 按指定顺序给指定字段赋值，最终形成一条新的记录}
-- 语法3：insert into 表名 (字段名1, 字段名2, ...) values (值1, 值2, ...), (值1, 值2, ...), ... ; {同时按指定顺序给指定字段赋值，最终形成多条新的记录}
-- 补充1：值的问题
-- 				字符串 - 用引号引起来
-- 				日期(date) - 1)日期字符串 2)date(now())-当前日期 3)year(now()) - 当前年 ... 类推 month, day, hour, minute, second
-- ===实例===
INSERT INTO tb_stu
VALUES
	(
		1001,
		'常山赵子龙',
		date(now()),
		1,
		'11111111111'
	);

INSERT INTO tb_stu
VALUES
	(
		1002,
		'小姐姐',
		date(now()),
		0,
		'11111111116'
	);

INSERT INTO tb_stu (stu_name, stu_brith, stu_tel)
VALUES
	(
		'武圣关羽',
		'2020-10-10',
		'11133322244'
	),
	(
		'飞将军吕布',
		'2011-11-11',
		'22211144455'
	),
	(
		'鬼才郭嘉',
		'1999-11-12',
		'1234687991'
	),
	(
		'卧龙诸葛',
		'1920-12-12',
		'66666666666'
	),
	(
		'凤雏庞统',
		'1111-11-11',
		'13548651334'
	),
	(
		'锦马超',
		'2222-12-12',
		'11278524569'
	),
	(
		'小霸王孙策',
		'1212-12-12',
		'13045698745'
	),
	(
		'恶来典韦',
		'1992-01-05',
		'15545214568'
	),
	(
		'毒士贾诩',
		'1878-07-08',
		'12245321486'
	),
	(
		'虎痴许诸',
		'1979-10-15',
		'13648952164'
	),
	(
		'吴下阿蒙',
		'2002-02-02',
		'12554862156'
	),
	(
		'美周郎',
		'1500-12-31',
		'14525463215'
	);

-- 2.delete
-- 语法1：delete from 表名; - 清空所有记录
-- 语法2：delete from 表名 where 条件;  - 删除所有满足条件的记录
-- 补充:sql条件语句的写法(筛选) (条件语句在写的时候可以通过加()改变运算顺序)
-- 比较运算: =(等于),<>(不等于),>,<,>=,<=
-- 逻辑运算：and(与),or(或),not(非)
-- 集合包含: in
-- 范围 between ...and...
-- 判断是否为空: is null, is not null
-- 筛选: like (% - 任意字符;_ - 表示单个任意字符)
-- ===实例===
DELETE
FROM
	tb_stu;

DELETE
FROM
	tb_stu
WHERE
	stu_name = '美周郎';

-- 3.update
-- 语法1：update 表名 set 字段1=新值1,字段2=新值2,...; - 将指定表中所有记录中指定的字段修改成指定值
-- 语法2：update 表名 set 字段1=新值1,字段2=新值2,... where 条件; - 满足条件修改指定值
-- ===实例===
UPDATE tb_stu
SET stu_brith = '2000-1-1'
WHERE
	stu_name = '美周郎';

-- 4.select
-- 语法1：select * from 表名; - 获取指定表中所有字段的数据
-- 语法2(映射)：select 字段1,字段2,字段3,... from 表;  - 获取表中指定字段的所有数据
-- 语法3(列重命名)：select 字段1 as 新字段1,字段2 as 新字段2,...from 表名;
-- 结果重新赋值(主要针对布尔)
-- select if(字段名,值1,值2) from 表名; - 如果if中对应的字段是值1,结果就是值1，否则值2
-- MySQL写法:if(字段,新值1,新值2)
-- 通用:case 字段 when 值 then 新值1 else 新值2 end
-- 列合并(查询的时候将多个字段合并成一个数据返回结果)
-- select concat(字段1,字段2,...) from 表名;
-- 筛选
-- 上面所有的查询语法的后面都可以加'where 条件'对记录进行筛选
-- select * from 表名 where 条件;
-- 排序
-- select * from 表名 order by 字段; - 将查询结果按指定字段的值从小到大进行排序
-- 在字段最后加desc可以从大到小排序
-- ===实例===
SELECT
	*
FROM
	tb_stu;

SELECT
	stu_name,
	stu_sex
FROM
	tb_stu;

SELECT
	stu_name AS '名字',
	stu_sex AS '性别'
FROM
	tb_stu;

SELECT

IF (stu_sex, '男', '女')
FROM
	tb_stu;

SELECT
	concat(stu_name, stu_tel)
FROM
	tb_stu;

SELECT
	*
FROM
	tb_stu
WHERE
	stu_sex = 0;

SELECT
	*
FROM
	tb_stu
ORDER BY
	stu_brith;

-- 最后：每次按照规范化书写是不是很麻烦呢；教你一招，点击工具栏中的美化SQL自动修改成规范格式哦！