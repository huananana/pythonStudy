"""__author__=桃花寓酒寓美人"""
import pymysql


def query_table(connect):
    # 注意：执行查询的sql语句，查询结果保存在游标对象中的
    # 注意：cursor中的查询结果，取一个就少一个
    sql_str = 'select * from tb_student;'
    with connect.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(sql_str)

        # 1.fetchall() - 获取当前查询的所有的结果
        # all_result = cursor.fetchall()
        # print('数据个数：', len(all_result))
        # print('表内容：', all_result)
        # for dic in all_result:
        #     print(dic['stuname'])

        # 2.游标对象.fetchone() - 获取当前查询中的一条数据
        print(cursor.fetchone())
        print(cursor.fetchone())

        # 3.游标对象.fetchmany(size)
        print(cursor.fetchmany(2))
        print(cursor.fetchone())


def operate_table(connect):
    # 增删改

    # 直接代码插入数据
    # sql_str = '''
    # insert into tb_student (stuname, stusex,stuage,stutel)
    # values
    # ('张三',1,30,'13011111111');
    # '''

    # 用户输入字段插入数据
    str1 = '''
    insert into tb_student (stuname, stusex, stuage, stutel)
    values 
    %s;
    '''
    str2 = ''
    while True:
        name = input('请输入名字：')
        sex = int(input('请输入性别(0/1)：'))
        age = int(input('请输入年龄：'))
        tel = input('请输入电话号码：')
        value = input('时候继续添加(y/n)')
        str2 += "('%s',%d,%d,'%s')," % (name, sex, age, tel)
        if value == 'n':
            print(str2)
            sql_str = str1 % str2[:-1]
            print(sql_str)
            break
    with connect.cursor() as cursor:
        cursor.execute(sql_str)


def use_ddl(connect):
    with connect.cursor() as cursor:
        # 1.===创建学生表===
        try:
            sql_str = """
             create table tb_student
            (
                stuid int auto_increment,
                stuname varchar(10) not null,
                stuage int,
                stusex bit default 1,
                stutel varchar(11),
                primary key (stuid)
            );
            """
            cursor.execute(sql_str)
        except:
            pass

        # 自定制表
        table_name = input('表名：')
        cnames = []
        while True:
            cname = input('请输入字段名(q-退出):')
            if cname == 'q':
                break
            cnames.append(cname + ' text,')

        str1 = '''
        create table if not exists tb_%s
        (
            %sid int auto_increment,
            %s
            primary key (%sid)
        );
        '''
        sql_str = str1 % (
            table_name,
            table_name[:3],
            ''.join(cnames),
            table_name[:3]
        )
        print(sql_str)
        cursor.execute(sql_str)


def main():
    # 1.建立连接
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='mysql&272727',
        port=3306,
        charset='utf8',
        autocommit=True,
        # cursors='pymysql.cursors.DictCursor'
    )

    # 2.切换数据库
    with con.cursor() as cursor:
        cursor.execute('use pyschool;')

    # 3.DDL
    # use_ddl(con)

    # 4.DML
    # operate_table(con)

    # 5.查询数据
    query_table(con)


if __name__ == '__main__':
    main()
