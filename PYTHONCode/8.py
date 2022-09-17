#data用于存储在一定范围内的素数
data = set()
for n in range(1234,4321,1):
    if n % 2 ==0:
        continue
    for i in range(3,int(n ** 0.5) + 1,2):
        if n % i == 0:
            break
    else:
        data.add(n)

for num in data :
    bit = str(num)
    temp = set(bit)
    if ('1' in temp) and ('2' in temp) and ('3' in temp) and ('4' in temp):
        print(num)
