import random
x = [random.randint(0,100) for i in range(20)]
print("原列表：",x) 
y = x[::2]
print("偶数坐标列表：",y) 
y.sort(reverse=True)
x[::2] = y
print("排序后列表：",x)

