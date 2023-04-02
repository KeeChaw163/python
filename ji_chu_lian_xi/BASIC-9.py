n = int(input())
for i in range(10000, 999999+1):
    sum = 0
    for j in range(len(str(i))):
        sum += int(str(i)[j])
    if sum == n:
        # print(str(i), end=' ')
        # print(str(i)[::-1])
        if str(i) == str(i)[::-1]:
            print(i)