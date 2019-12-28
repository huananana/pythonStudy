"""__author__=桃花寓酒寓美人"""
import function as func

student_date = []

index = (x for x in range(100))

while True:
    button = input('1.登录' + '\n'
                   '2.注册' + '\n'
                   '3.退出')

    if button == '1':
        func.login()
        func.student_sys(index, student_date)
    elif button == '2':
        func.create_account()
    elif button == '3':
        break
    else:
        print('重新输入')

