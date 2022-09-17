import random
x=[random.randint(1,100) for i in range(20)]
a=sorted(x[:10])
b=sorted(x[10:],reverse=True)
x=a+b
print(x)
