# 1.分支结构 - if语句
:<<EOF
语法1：if
if 条件语句
then
        满足条件执行的代码段
fi

语法2：if-else
if 条件语句
then
        满足条件执行的代码段
else
        不满足条件执行的代码段
fi

语法3：if-elif-else
if 条件语句1
then
        满足条件1执行的代码
elif 条件语句2
then
        满足条件2执行的代码
elif 条件语句3
then
        满足条件3执行的代码
...
else
        所有条件都不满足执行的代码
fi
EOF

printf 请输入年龄：
read age
if [ $age -lt 12 ]
then
        echo 儿童
elif [ $age -le 18 ]
then
        echo 少年
elif [ $age -le 28 ]
then
        echo 青年
elif [ $age -le 50 ]
then
        echo 壮年
else
        echo 老年
fi

echo ====================for循环=======================
# 2.for循环
:<<EOF
语法：
for 变量 in 序列
do
        循环体
done
EOF

# 遍历多个值
for char in "hello world！" 100 'abc'
do
        echo char:$char
done

#遍历数组       -       for循环主要用于遍历数组
names=(小明 小红 小花 tom bob)
for item in ${names[*]}
do
        echo name:$item
done

# 3.while循环
:<<EOF
语法：
while 条件语句
do
        循环体
done
EOF
string='hello world!'
len=${#string}
index=0
while [ $index -lt $len ]
do
        echo string:${string:$index:1}
        index=`expr $index + 1`
done

#练习计算100累加
index=0
num=1
while [ $indef -lt 101 ]
do
        num=`expr $sum + $num`
        index=`expr $num + 1`
done
echo num:$num
