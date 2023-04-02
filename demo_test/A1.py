from math import floor

n = int(input())
res = []
while n > 0:
    x = int(input())
    res.append(x)
    n -= 1
print(max(res))
print(min(res))
print('%.2f'%float(sum(res)/len(res)))