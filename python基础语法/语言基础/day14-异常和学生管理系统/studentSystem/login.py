"""__author__=桃花寓酒寓美人"""
from studentSystem import fileManeger

users_file = 'users.json'
"""
账号密码的存储：
程序中：用一个字典保存所欲的账号和密码 - {账号1：密码1，账号2：密码2，...}
数据需要持久化：将所有账号对应的字典保存在文件中(users.json)
"""


def register():
    # 输入账号
    while True:
        user_name = input('请输入账号(3~6位)：')
        if 3 <= len(user_name) <= 6:
            break
        else:
            print('账号不符合要求，请重新输入！')

    # 输入密码
    while True:
        password = input('请输入密码(6~12)：')
        if 6 <= len(password) <= 12:
            break
        else:
            print('密码不符合要求，请重新输入！')

    # 3.检测账号时候已经注册过
    all_user = fileManeger.read_json_file(users_file)
    if not all_user:
        all_user = {}
    if user_name in all_user:
        print('注册失败，该账号已经注册过')
        return

    # 4.注册
    all_user[user_name] = password
    result = fileManeger.weite_json_file(users_file, all_user)
    if result:
        print('注册成功')
    else:
        print('注册失败')


def login():
    pass


def show_login_page():

    # 获取主页面
    page = fileManeger.read_text_file('loginPage')
    while True:
        # 显示主页面
        print(page)
        # 选择
        value = input('请选择(1~3):')
        if value == '1':
            # print('登录')
            login()
        elif value == '2':
            # print('注册')
            register()
        elif value == '3':
            # 三种方式退出 break，return，exit()
            exit()
        else:
            print('输入错误')


register()