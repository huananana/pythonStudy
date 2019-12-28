# shell运算符：算术运算符、关系运算符、布尔运算符、字符串运算符
# 1.算术运算符(数学运算符):+,-,*,/,%
# 算术运算符的运算对象是数字
# 注意：1)算术符在用的时候不能直接用运算符加数字进行运算
#               `expr 整数运算表达式` 或者 `echo "小数运算表达式"|bc`
#               `echo "scale=小数点位数;小数运算表达式"|bc`
#               2)运算表达式中的运算符和数字之间需要有一个空格

echo ==========================加法运算=======================
# 1)加法运算
# sum1=10 + 20 # 写法不对！
sum1=`expr 10 + 20`
echo $sum1

# sum2=`expr 1.3 + 2.4` # 写法不对！
sum2=`echo "1.3 + 2.4"|bc`
echo $sum2

sum3=`echo "scale=5;7 / 3"|bc`
echo $sum3

echo ===减法运算===
# 2)减法运算
echo `expr 10 - 20`
echo `echo "9.3 - 2.0"|bc`
echo ===乘法运算===
# 3)乘法运算: *在整数运算前需要加\
echo `expr 2 \* 3`
echo `echo "2.1 * 4.0"|bc`

# 4)除法运算
echo `expr 5 / 2`
sum3=`echo "scale=2;7.0 / 3"|bc`
echo $sum3

# 5)取余
echo `expr 8 % 3`
echo `expr 452 % 10`

echo =====================比较运算符=========================
# 2.比较运算符
:<<EOF
-eq             -       等于，相当于 ==
-ne             -       不等于，相当于 !=
-gt             -       大于
-lt             -       小于
-ge             -       大于等于
-le             -       小于等于

使用语法：[ 值1 比较运算符 值2 ]

注意：比较运算表达式只能配合if语句或者while循环来使用
EOF

age=20
if [ $age -gt 18 ]
then
        echo 成年！
else
        echo 未成年！
fi

echo ================布尔运算符==================
# 3.布尔运算符(逻辑运算符)
:<<EOF
-a              -       逻辑与 运算
-o              -       逻辑或运算
!               -       逻辑非运算

使用语法: [ 布尔1 逻辑运算符 布尔2 ]
注意：结果只能用在if或者while循环的条件上
EOF
score=98
age=20

# 年龄大于等于18并且分数大于等于95
if [ $age -ge 18 -a $score -ge 95 ]
then
        echo 可以参加比赛
else
        echo
fi

# 练习
echo ===判断输入的年是否是闰年===
read year
num1=`expr $year % 4`
num2=`expr $year % 100`
num3=`expr $year % 400`
if [ $num1 -eq 0 -a $num2 -ne 0 -o $num3 -eq 0 ]
then
        echo ${year}是闰年
else
        echo ${year}不是闰年
fi

echo ===============字符串运算符===============
# 4.字符串运算符
:<<EOF
[ 字符串1 = 字符串2 ]   -       判断两个字符是否相等
[ 字符串1 != 字符串2 ]  -       判断两个字符串是否不相等
[ -z 字符串 ]                   -       判断字符串长度是否为0
[ -n "字符串" ]                 -       判断字符串长度是否不为0
[ $ 字符串 ]                    -       判断字符串是否是空串
EOF

if [ abc = 'abc' ]
then
        echo 相等！
else
        echo 不相等！
fi

str1="abc"
if [ $str1 = 'abc' ]
then
        echo 相等
else
        echo 不相等
fi

if [ -z $str1 ]
then
        echo 空串
else
        echo 不是空串
fi

if [ -n "$str1" ]
then
        echo 长度不为0
else
        echo 长度为0
fi
