s = input("请输入一个不超过255字符的字符串：")
count =0
for x in s:
    if x.isdigit():
        count +=1
print(count)
    
        