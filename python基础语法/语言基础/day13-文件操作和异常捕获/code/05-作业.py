"""__author__=桃花寓酒寓美人"""


# button
def login():
    id = input('id>>>')
    pw = input('pw>>>')
    with open('account.txt', 'r', encoding='utf-8') as f:
        account = eval(f.read())
    for ac in account:
        for key in ac:
            if key == id:
                if ac[key] == pw:
                    print('登陆成功')
                else:
                    print('账号或密码错误')


def create_account():
    id = input('id>>>')
    pw = input('pw>>>')
    account_time = {}
    with open('account.txt', 'r', encoding='utf-8') as f:
        re = f.read()
        if re == '[]':
            account_time[id] = id
            account_time[pw] = pw
            account = '{}{}]'.format(re[:-1], account_time)
        else:
            account_time[id] = id
            account_time[pw] = pw
            account = '{}, {}]'.format(re[:-1], account_time)
    with open('account.txt', 'w', encoding='utf-8') as f:
        f.write(account)


while True:
    button = input('1.登录' + '\n'
                   '2.注册' + '\n'
                   '3.退出')

    if button == '1':
        login()
    elif button == '2':
        create_account()
    elif button == '3':
        break
    else:
        print('重新输入')
