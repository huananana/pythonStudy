"""__author__=桃花寓酒寓美人"""


# 删除学生
def cancel(date):
    button = '1'
    while True:
        if button == '1':
            name = input('name>>>')
            for student in date:
                if student['name'] == name:
                    print(student)
            index = input('index>>>')
            for student in date:
                if student['index'] == int(index):
                    date.remove(student)
                    print('删除成功')
        elif button == '2':
            break
        else:
            print('目标不存在，请重新输入')
        button = input('1.继续删除' + '\n'
                       '2.返回')


# 查找学生
def search(seq):
    while True:
        button = input('1.查询所有的学生信息：' + "\n"
                       '2.根据名字查看学生信息：' + "\n"
                       '3.返回上一层')
        if button == '1':
            print(seq)
        elif button == '2':
            name = input('name>>>')
            for student in seq:
                if student['name'] == name:
                    print(student)
        elif button == '3':
            break
        else:
            print('目标不存在，请重新输入')


# 添加学生
def addition(seq, date):
    button = '1'
    while True:
        student_time = {}
        if button == '1':
            student_time['index'] = next(seq)
            student_time['name'] = input('请输入学生的姓名：')
            student_time['age'] = input('请输入学生的年龄：')
            student_time['phone'] = input('请输入学生的电话号码：')
            date.append(student_time)
        elif button == '2':
            break
        else:
            print('重新输入')
        button = input('1.继续添加：' + '\n'
                       '2.返回上一层')


# 登录
def login():
    id = input('id>>>')
    pw = input('pw>>>')
    with open(r'.\Account\account.txt', 'r', encoding='utf-8') as f:
        account = eval(f.read())
    for ac in account:
        for key in ac:
            if key == id:
                if ac[key] == pw:
                    print('登陆成功')
                else:
                    print('账号或密码错误')


# 创建
def create_account():
    account_time = {}
    id = input('id>>>')
    pw = input('pw>>>')
    with open(r'.\Account\account.txt', 'r', encoding='utf-8') as f:
        re = f.read()
    if re == '[]':
        account_time[id] = id
        account_time[pw] = pw
        account = '{}{}]'.format(re[:-1], account_time)
    else:
        for account in re:
            if id == account:
                print('账户已存在')
                break
            else:
                account_time[id] = id
                account_time[pw] = pw
                account = '{}, {}]'.format(re[:-1], account_time)
                with open(r'.\Account\account.txt', 'w', encoding='utf-8') as f:
                    f.write(account)


def student_sys(seq, date):
    while True:
        button = input('1.添加学生' + '\n'
                                  '2.查询学生' + '\n'
                                             '3.删除学生' + '\n'
                                                        'q.退出系统')
        if button == '1':
            addition(seq)
        elif button == '2':

            search(date)
        elif button == '3':
            cancel()
        elif button == 'q':
            break
        else:
            print('目标不存在，请重新输入')
        print(date)

