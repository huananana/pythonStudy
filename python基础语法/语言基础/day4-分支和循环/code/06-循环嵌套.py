
# 循环嵌套：外面的循环执行一次，里面的循环要执行完
# 循环嵌套最多不要超过3层，找其它更好的方法
for x in range(3):
    for y in range(4):
        print(x,y)

# 计算 1!+2!+3!+...+10!
# N! = 1*2*3*4*...*N
count = 0

for x in range(1,11):
    num = 1
    for y in range(1,x):
        num *= y
        print(num)
        count += num
print(count)













