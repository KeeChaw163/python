# a, b, n = map(int, input().split(" "))
# day = 1
# down = 0
# while down < n:
#     if day % 6 == 0 or day % 7 == 0:
#         down += b
#     else:
#         down += a
#     day += 1
# print(day-1)

a, b, n = map(int, input().split(" "))
day = 1
week = a*5 + b*2        # 一周的题目数
days = 7 * (n//week)    # 做题天数
s = week * (n//week)    # 做题数量
while s < n:
    if day <= 5:
        s += b
    elif day <= 7 and day > 5:
        s += b
    day += 1
    days += 1
    if day > 7:
        day = 1
print(days)