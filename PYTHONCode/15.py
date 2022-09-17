import random
ls = list()
ls = [random.randint(0,100) for i in range(1000)]
st = set(ls)
for i in st:
    print(i, '出现的次数为： ', ls.count(i))