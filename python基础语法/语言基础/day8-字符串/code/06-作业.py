"""__author__=蒋志颖"""
for x in range(1,10,2):
    print(x)

str1 = 'how are you? Im fine, Thank you!'
str2 = 'you'

for x in range(len(str1)-2):

    if str1[x:x+3] == str2:
        print(x)
        break
else:
    print('k')