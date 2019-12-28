"""__author__=桃花寓酒寓美人"""
a = float(input("长>>>"))
b = float(input("宽>>>"))
S = a*b
print(S)
if S - int(S) >=0.5:
    S = int(S)+1
else:
    S = int(S)
print("S=%.2f"%S)