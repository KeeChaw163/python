n = int(input())
res = []
for i in range(n):
    res.append([])
    for j in range(i+1):
        if j == 0 or j == i:
            res[i].append(1)
        else:
            res[i].append(res[i-1][j-1]+res[i-1][j])
    print(" ".join(str(a) for a in res[i]))
print(res)