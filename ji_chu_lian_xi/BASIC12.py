n = int(input())
integ = []
for i in range(n):
    integ.append(int(input(), 16))
for j in integ:
    print(oct(j)[2:])