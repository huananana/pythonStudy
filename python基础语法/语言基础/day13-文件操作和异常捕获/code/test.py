"""__author__=桃花寓酒寓美人"""


def addition(seq):
    button = '1'
    while True:
        student_time = {}
        if button == '1':
            student_time['index'] = next(seq)
            student_time['name'] = input('请输入学生的姓名：')
            student_time['age'] = input('请输入学生的年龄：')
            student_time['phone'] = input('请输入学生的电话号码：')
            student_date.append(student_time)
        elif button == '2':
            break
        else:
            print('重新输入')
        button = input('1.继续添加：' + '\n'
                       '2.返回上一层')


def search(seq):
    while True:
        button = input('1.查询所有的学生信息：' + "\n"
                       '2.根据名字查看学生信息：' + "\n"
                       '3.返回上一层')
        if button == '1':
            print(student_date)
        elif button == '2':
            name = input('name>>>')
            for student in student_date:
                if student['name'] == name:
                    print(student)
        elif button == '3':
            break
        else:
            print('目标不存在，请重新输入')


def cancel():
    button = '1'
    while True:
        if button == '1':
            name = input('name>>>')
            for student in student_date:
                if student['name'] == name:
                    print(student)
            index = input('index>>>')
            for student in student_date:
                if student['index'] == int(index):
                    student_date.remove(student)
                    print('删除成功')
        elif button == '2':
            break
        else:
            print('目标不存在，请重新输入')
        button = input('1.继续删除' + '\n'
                       '2.返回')

student_date = []

index = (x for x in range(100))

while True:
    button = input('1.添加学生' + '\n'
                   '2.查询学生' + '\n'
                   '3.删除学生' + '\n'
                   'q.退出系统')
    if button == '1':
        addition(index)
    elif button == '2':
        search(student_date)
    elif button == '3':
        cancel()
    elif button == 'q':
        break
    else:
        print('目标不存在，请重新输入')
    print(student_date)
