a=input('输入为一行字符串（字符串中没有空白字符，字符串长度不超过100）:')
b=a[::-1]#倒序输出
if a==b:#判断是否相等
    print('yes')
else:
    print('no')
