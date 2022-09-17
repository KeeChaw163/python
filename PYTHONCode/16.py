list = eval(input("请输入一个列表："))
a = eval(input("请输入第一个下标："))
b = eval(input("请输入第二个小标："))

if a>b:
    for i in range(b,a):
        print(list[b:a])
        break
elif a<b:
    for i in range(a,b):
        print(list[a:b])
        break
elif a==b:
    print([])
