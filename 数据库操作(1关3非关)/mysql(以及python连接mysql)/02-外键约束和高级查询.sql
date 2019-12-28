-- 1.E.R实体关系图
-- 通过图表的形式来表示数据库中表和字段以及表和表之间的关系
-- 表和表之间的关系主要有4种：一对一，一对多，多对一，多对多；

-- 2.外键约束
-- 外键约束：让字段的值的取值范围在另外一张表的主键中
-- 怎么添加外键约束：1)保证当前表中有一个字段能够保存另外一张表的主键	2)添加外键约束
--     不同对应关系外键的添加的要求不同
--     一对一：可以添加到任意一张表中
--     一对多和多对一：添加到多的那种表中
--     多对多：两张表没有办法建立多对多的对应关系，需要第三方表


use school;
alter table tb_student add column colid int comment '所在学院'; -- 在学生表中添加新的字段保存学院表的主键

-- 3.怎么添加约束
-- 3.1 创建表或者添加字段的时候直接在字段后面添加约束
-- 3.2 通过修改表的表示添加和删除约束
-- alter table 表名 add constraint 约束索引名 约束名(字段);  - 给指定	字段添加指定约束(只能添加唯一约束和主键约束)
-- alter table 表名 drop index 约束索引名; -- 删除指定约束

-- alter table tb_student add constraint unique_colid unique (colid);
alter table tb_student drop index unique_colid;
drop index unique_colid on tb_student ;

-- alter table 表1 add CONSTRAINT 约束索引名 foreign key (字段1) references 表2 (字段2);
alter table tb_student add constraint fk_collid_coll foreign key (colid) references tb_college (collid);
alter table tb_student drop foreign key fk_collid_coll;


-- 同理对教师表和学院表/教师表和课程表 - 添加约束
alter table tb_teacher add column cid int comment '所在学院';
alter table tb_teacher add constraint fk_collid_tea foreign key (cid) references tb_college (collid);

alter table tb_course add column tid int comment '课程老师';
alter table tb_course add constraint fk_collid_cou foreign key (tid) references tb_teacher (teaid);

-- 多对多添加外键约束
create table if not exists tb_record(
reid int auto_increment comment '选课记录编号',
sid int comment '学生外键',
cid int comment '课程外键',
redate date comment '选课日期',
score float comment '分数',
primary key (reid),
foreign key (sid) references tb_student (stuid),
foreign key (cid) references tb_course (couid)
);

-- 4.高级查询
-- 1.去重： selelct distinct 字段名 from 表名;
select distinct redate from tb_record order by redate; -- 查询课程日期按顺序排列
select distinct sid from tb_record; -- 查询所有选课的学生的id

-- 2.限制和分页
-- 限制：select * from 表名 limit N; - 查询的时候只获取前N条数据
-- 偏移：select * from 表名 limit M offset N; - 跳过前N条数据获取M条数据(从第N+1条数据开始,获取M条数据)
--       select * from 表名 limit M,N; - 跳过前M条数据取N条数据
select * from tb_record limit 5; -- 获取tb_record表中前5条数
select * from tb_record limit 7 offset 3; -- 跳过前3条获取7条数据
select * from tb_record limit 3,7; -- 跳过前3条获取7条数据

select * from tb_record order by score desc limit 3; -- 获取成绩前3的选课记录 

-- 3.聚合：max(),min(),sum(),avg(),count() - mysql
use school;

select max(score) as max_score from tb_record; -- 获取tb_record中最高分
select min(score) as min_score from tb_record; -- 获取tb_record中最低分
select sum(score) as sum_score from tb_record; -- 求和所有分数的和，如果某一个记录的分数是空，那么这条记录不存在与运算
select avg(score) as avg_score from tb_record; -- 求平均分(空不参与运算)
select count(score) as c_score from tb_record; -- 统计分数的个数(空不参与计算)

-- 4.分组：
-- select 聚合操作 from 表名 group by (字段); - 按指定字段的值对表进行分组，然后对每个分组进行聚合操作
-- 注意：分组后，除了分组字段以外，其它字段只能聚合操作
-- 分组后加条件 用having代替where

-- 获取每个学生的平均分
select sid, avg(score) from tb_record group by (sid);

-- 获取每个学科的平均分
select cid, avg(svore) from tb_record group by (cid);

-- 获取每个学生选课数量
select sid, count(cid) from tb_record group by (sid);


-- 子查询：将一个查询的结果作为另外一个查询的条件或者查询对象
-- 第一种子查询：将查询结果作为另外一个查询的条件

-- 获取成绩是最高分的所有的学生的id
select max(score) as max_s from tb_record;
select sid from tb_record where score=(select max(score) as maax_s from tb_record);

-- 获取分数前3的所有的学生的id(版本不支持limit的子查询)
-- select distinct(score) from tb_record order by score desc limit 3;
-- select sit from tb_record where score in (select distinct(score) from tb_record order by score desc limit 3);

-- 获取选了2门课程以上的学生的id(分组+聚合)
select sid,count(cid) from tb_record group by (sid) faving count(cid)>2;
select sid,count(cid) as c_course from tb_record group by (sid) having c_course>2;
select sid from tb_record group by (sid) having count(cid)>2;

-- 获取选了2门课程以杀那个的学生的姓名(子查询)
select stuname from tb_student where stuid in (select sid from tb_record group by (sid) having count(cid)>2);


-- 第二种子查询：将一个查询的结果作为另一个查询的查询对象
-- 注意：如果要将查询结果作为查询对象，那么查询结果对应的查询必须重命名
select * from tb_student limit 4.5;
select stuname from (select * from tb_student limit 4,5) as t1;

select stuname as sname,stuaddr as saddr from tb_student where stusex=0;
select sname,saddr from(select stuname as sname,stuaddr as saddr from tb_student where stusex=0) as t1 where saddr like '%成都';


-- 6.连接查询：同时查询多张表
-- select * 
-- from 表名1,表名2,... 
-- where 表1.字段=表2.字段 and ... and 查询条件; 


use school;
-- 1.学院表
create table if not exists tb_college
(
collid int auto_increment comment '学院id',
collname varchar(20) not NULL UNIQUE comment '学院名称',
collintro varchar(200) comment '学院简介',
PRIMARY KEY (collid)
);

insert into tb_college (collname, collintro) values 
('计算机学院', '创建于1956年是我国首批建立计算机专业。学院现有计算机科学与技术一级学科和网络空间安全一级学科博士学位授予权，其中计算机科学与技术一级学科具有博士后流动站。计算机科学与技术一级学科在2017年全国第四轮学科评估中评为A；2019 U.S.News全球计算机学科排名26名；ESI学科排名0.945‰，进入全球前1‰，位列第43位。'),
('外国语学院', '1998年浙江大学、杭州大学、浙江农业大学、浙江医科大学四校合并，成立新的浙江大学。1999年原浙江大学外语系、原杭州大学外国语学院、原杭州大学大外部、原浙江农业大学公外部、原浙江医科大学外语教学部合并，成立浙江大学外国语学院。2003年学院更名为浙江大学外国语言文化与国际交流学院。'),
('经济管理学院', '四川大学经济学院历史悠久、传承厚重，其前身是创办于1905年的四川大学经济科,距今已有100多年的历史。已故著名经济学家彭迪先、张与九、蒋学模、胡寄窗、陶大镛、胡代光，以及当代著名学者刘诗白等曾先后在此任教或学习。在长期的办学过程中，学院坚持以马克思主义的立场、观点、方法为指导，围绕建设世界一流经济学院的奋斗目标，做实“两个伟大”深度融合，不断提高党的建设质量与科学推进一流事业深度融合。');


-- 2.学生表
create table if not exists tb_student
(
stuid 		int not null comment '学号',
stuname 	varchar(20) not null comment '姓名',
stusex 		boolean default 1 comment '性别',
stubirth 	date not null comment '出生日期',
stuaddr 	varchar(255) default '' comment '籍贯',
primary key (stuid)
);


insert into tb_student (stuid, stuname, stusex, stubirth, stuaddr) values
(1001, '杨逍', 1, '1990-3-4', '四川成都'),
(1002, '任我行', 1, '1992-2-2', '湖南长沙'),
(1033, '王语嫣', 0, '1989-12-3', '四川成都'),
(1572, '岳不群', 1, '1993-7-19', '陕西咸阳'),
(1378, '纪嫣然', 0, '1995-8-12', '四川绵阳'),
(1954, '林平之', 1, '1994-9-20', '福建莆田'),
(2035, '东方不败', 1, '1988-6-30', null),
(3011, '林震南', 1, '1985-12-12', '福建莆田'),
(3755, '项少龙', 1, '1993-1-25', null),
(3923, '杨不悔', 0, '1985-4-17', '四川成都'),
(4040, '隔壁老王', 1, '1989-1-1', '四川成都');

-- 3.老师表
create table if not EXISTS tb_teacher
(
teaid 		int not null comment '工号',
teaname 	varchar(20) not null comment '姓名',
teatitle 	varchar(10) default '助教' comment '职称',
primary key (teaid)
);

insert into tb_teacher (teaid, teaname, teatitle) values 
(1122, '张三丰', '教授'),
(1133, '宋远桥', '副教授'),
(1144, '杨逍', '副教授'),
(2255, '范遥', '副教授'),
(3366, '韦一笑', '讲师');

-- 4. 课程表
create table if not EXISTS tb_course
(
couid 		int not null comment '编号',
couname 	varchar(50) not null comment '名称',
coucredit 	int not null comment '学分',
primary key (couid)
);

insert into tb_course (couid, couname, coucredit) values 
(1111, 'Python程序设计', 3),
(2222, 'Web前端开发', 2),
(3333, '操作系统', 4),
(4444, '计算机网络', 2),
(5555, '编译原理', 4),
(6666, '算法和数据结构', 3),
(7777, '经贸法语', 3),
(8888, '成本会计', 2),
(9999, '审计学', 3);


use school;

-- 查询所有学生信息
select * from tb_student;

-- 查询所有课程名称及学分
select couname,coucredit from tb_course; 

-- 查询所有学生的姓名和性别
select stuname,
if (stusex,'男','女')as gender
from tb_student;


-- 查询所有女学生的姓名和出生日期
select stuname,stubirth from tb_student where stusex=0;
SELECT stuname, stubirth FROM tb_student where stusex=0;

-- 查询所有80后学生的姓名、性别和出生日期
select * from tb_student where stubirth>'1980-1-1';
SELECT stuname, if(stusex, '男', '女') as gender, stubirth FROM tb_student 
WHERE stubirth >= '1980-1-1' and stubirth <= '1989-12-31';

-- 查询姓"杨"的学生姓名和性别
select * from tb_student where stuname like '杨%';
SELECT stuname, if(stusex, '男', '女') as gender FROM tb_student where stuname like '杨%';


-- 查询姓"杨"名字两个字的学生姓名和性别
select * from tb_student where stuname like '杨_';
SELECT stuname, if(stusex, '男', '女') as gender FROM tb_student where stuname like '杨_';


-- 查询姓"杨"名字三个字的学生姓名和性别
select * from tb_student where stuname like '杨__';
SELECT stuname, if(stusex, '男', '女') as gender FROM tb_student where stuname like '杨__';


-- 查询名字中有"不"字或"嫣"字的学生的姓名
select * from tb_student where stuname like'%嫣%' or stuname like '%不%'; -- 待改进
SELECT stuname FROM tb_student where stuname like '%不%' or stuname like '%嫣%';


-- 查询没有录入家庭住址的学生姓名
select * from tb_student where stuaddr is null;
SELECT stuname FROM tb_student WHERE stuaddr is NULL;


-- 查询录入了家庭住址的学生姓名
select * from tb_student where stuaddr is not null;
SELECT stuname FROM tb_student WHERE stuaddr is not NULL;


-- 查询学生选课的所有日期
select stuname,redate 
from tb_student as stu,tb_record as re,tb_course as cou 
where stu.stuid=re.sid and cou.couid=re.cid;
SELECT distinct redate FROM tb_record;


-- 查询学生的家庭住址
select stuname,stuaddr
from tb_student
select distinct stuaddr FROM tb_student;


-- 查询男学生的姓名和生日按年龄从大到小排列
select stuname,stubirth
from tb_student 
where stusex=1
order by stubirth;
SELECT stuname, stubirth FROM tb_student where stusex=1 ORDER BY stubirth;


-- 查询年龄最大的学生的出生日期
select min(stubirth)
from tb_student;
SELECT min(stubirth) FROM tb_student;


-- 查询年龄最小的学生的出生日期
select max(stubirth)
from tb_student;
SELECT max(stubirth) FROM tb_student;


-- 查询男女学生的人数
select if (stusex,'男','女') as stusex, count(stusex)
from tb_student
group by (stusex);
SELECT if(stusex, '男生', '女生') as gender, count(stuid) as c_stu FROM tb_student GROUP BY (stusex);


-- 查询课程编号为1111的课程的平均成绩
select avg(score)
from tb_record
group by (cid)
having cid=1111
SELECT avg(score) FROM tb_record WHERE cid=1111;


-- 查询学号为1001的学生所有课程的平均分
select *,avg(score)
from tb_student as stu,tb_record as re
where stu.stuid=re.sid and stu.stuid=1001
group by (re.sid)
SELECT avg(score) FROM tb_record WHERE sid=1001;


-- 查询每个学生的学号和平均成绩
select re.sid,avg(score)
from tb_student as stu,tb_record as re
where stu.stuid=re.sid
group by (re.sid)
SELECT sid, avg(score) FROM tb_record GROUP BY (sid);


-- 查询平均成绩大于等于90分的学生的学号和平均成绩
-- select sid,avg(score)from tb_record group by (sid);

select stuid,avg_sc
from tb_student as t1,(select sid,avg(score) as avg_sc from tb_record group by (sid)) as t2
where t1.stuid=t2.sid and avg_sc>=90;
SELECT sid, avg(score) as avg_score FROM tb_record GROUP BY (sid) having avg_score>=90;


-- 查询年龄最大的学生的姓名
-- aaa
SELECT stuname FROM tb_student where stubirth=(select min(stubirth) from tb_student);

-- 查询年龄最大的学生姓名和年龄
SELECT stuname, DATEDIFF(CURDATE(),stubirth) div 365 as age FROM tb_student where stubirth=(select min(stubirth) from tb_student);

-- 查询选了两门以上的课程的学生姓名
select stuname FROM tb_student where stuid in (select sid FROM tb_record GROUP BY (sid) HAVING count(cid)>2);

-- 查询学生姓名、课程名称以及成绩
select stuname, couname, score FROM
tb_student,
tb_course,
tb_record
where tb_student.stuid=tb_record.sid and tb_course.couid=tb_record.cid;

-- 查询学生姓名、课程名称以及成绩按成绩从高到低查询第11-15条记录
select stuname, couname, score FROM
tb_student,
tb_course,
tb_record
where tb_student.stuid=tb_record.sid and tb_course.couid=tb_record.cid
ORDER BY score DESC
LIMIT 10, 5;

-- 查询选课学生的姓名和平均成绩
select stuname, avg(score) FROM 
tb_student as t1, 
tb_record as t2
where t1.stuid=t2.sid GROUP BY(sid);

select stuname, avg_s FROM
tb_student as t1,
(select sid, avg(score) as avg_s FROM tb_record GROUP BY (sid)) as t2
where t1.stuid=t2.sid;

-- 查询每个学生的姓名和选课数量
select stuname, count(cid) FROM
tb_student as t1,
tb_record as t2
WHERE t1.stuid=t2.sid 
GROUP BY (sid);

SELECT stuname, count_c FROM 
tb_student as t1,
(select sid, COUNT(cid) as count_c FROM tb_record GROUP BY (sid)) as t2
WHERE t1.stuid=t2.sid;

