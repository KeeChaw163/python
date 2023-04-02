n = int(input())
str = input().split()
res = []
for i in str:
    res.append(int(i))
print(max(res))
print(min(res))
print(sum(res))