s = input("请输入两个四字符的字符串：")
lst = s.split()
a=lst[0][0]+lst[0][1]+lst[1][2]+lst[1][3]
b=lst[1][0]+lst[1][1]+lst[0][2]+lst[0][3]
print(a,b,sep='\n')