for i in range(100, 999+1):
    sum = 0
    for j in range(len(str(i))):
        sum += int(str(i)[j])**3
    if sum == i:
        print(i)