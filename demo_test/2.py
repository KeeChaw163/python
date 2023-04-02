n = int(input())
x = []
res = []
for i in range(n):
    x.append([])
    for j in range(i+1):
        if j == 0 or j == i:
            x[i].append(1)
        else:
            x[i].append(x[i-1][j]+x[i-1][j-1])
        res.append(x[i][j])
print(res.index(n)+1)