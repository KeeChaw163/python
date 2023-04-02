a = ['jia', 'yi', 'bing', 'ding', 'wu', 'ji', 'geng', 'xin', 'ren', 'gui']
b = ['zi', 'chou', 'yin', 'mao', 'chen', 'si', 'wu', 'wei', 'shen', 'you', 'xu', 'hai']
n = int(input())
# print(n % len(a))
# print(n % len(b))
print(a[n % len(a)-4]+b[n % len(b)-4])