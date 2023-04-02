# n = int(input())
# s = n
# while n // 3 >= 3:
#     s += n // 3
#     n = n // 3 + n % 3
# print(s+n % 3)


n = int(input())
cnt, cap = n, n  # cnt代表喝了多少，cap代表手上的瓶盖数量，这里表示先把n瓶喝完了
while cap > 2:
    tmp, cap = cap // 3, cap % 3  # 换饮料
    cnt, cap = cnt + tmp, cap + tmp  # 喝饮料
print(cnt)
