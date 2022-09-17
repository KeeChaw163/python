a= [399,4396,539,288,109,749,235,190,99,1000]
b= int(input("请输入最大价格:"))
c = int(input("请输入最小价格:"))
a1 =[]
a1 = filter(lambda x:x<=b and x>=c,a)
print(list(a1))
d=input('''1.价格降序排列
2.价格升序排列
请选择...:''')
if d =='1':
    f=sorted(a1,reverse=True)
    print(f)
if d =='2':
    a1.sort()
    print(a1)