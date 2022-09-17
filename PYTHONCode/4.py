
import random
x = []
#生成50个0~1000的随机数
for i in range(50):
    x.append(random.randint(0,1000))
print("随机生成的数的列表：",x)
#判断删除
for i in range(49,-1,-1):
    if x[i]%2!=0:
        del x[i]
print("删除奇数之后的列表：",x)


