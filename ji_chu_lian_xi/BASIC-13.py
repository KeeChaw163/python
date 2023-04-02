n = int(input())
strr = input().split()
countt = 0
# x = sorted([int(i) for i in str])
x = list(map(int, strr))
x.sort()
for j in x:
    countt += 1
    if countt == len(x):
        print(str(j), end="")
        break
    else:
        print(str(j), end=" ")