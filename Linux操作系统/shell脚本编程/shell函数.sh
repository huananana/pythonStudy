# 1.函数
# 1)函数的声明

N=1
:<<EOF
语法：

函数名(){
        函数体
}

说明:
函数名  -       程序员自己命名；标识符，不是关键字
形参    -       shell中不需要用形参来获取实参，而是通过${N}去获取第N个实参
EOF

# 2)函数的调用
:<<EOF
语法：函数名 实参1 实参2 ...
EOF

# 声明一个函数打印两个数的和
sum(){
        echo 求和函数：`expr ${1} + ${2}`
        echo ${#}
}

sum 100 300

# 3)函数返值
# 在函数体中写 return语句来返回数据，但是return后面的值必须是数字，而且是在0~255
# 获取函数返回值：在函数调用表达式后面获取${?}的值
func1(){
        echo 函数被调用
        return 258
}

func1
echo 函数返回值：${?}   # 打印函数的返回值

echo ==================func2===================
func2(){
        s=`expr ${1} + ${2}`
        touch /home/shell编程/result.txt
        echo ${s} > /home/shell编程/reshult.txt
}

func2 10 20
re=$(cat ./result.txt)
echo $re
