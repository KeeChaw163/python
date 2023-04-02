n, m = map(int, input().split(" "))
for i in range(1, n+1):
    qian = ''
    hou = ''
    for j in range(0, i):
        qian += str(chr(ord('A')+j))
    new_qian = qian[::-1]
    for a in range(0, m-i):
        hou += str(chr(ord('B')+a))
    res = new_qian+hou
    print(res[:m])