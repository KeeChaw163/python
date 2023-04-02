# import collections
#
# n, k = map(int, input().split(" "))
# data = []
# for i in range(n):
#     h, w = map(int, input().split(" "))
#     data.append([h, w])
# # print(data)
#
# res = []
# for j in data:
#     # print(j)
#     kk = {}
#     if j[0] >= j[1]:
#         for a in range(1, j[1]+1):
#             mm = []
#             for b in range(1, j[0] * j[1]):
#                 if (a ** 2) * b <= j[0] * j[1] and a * b <= j[1]:
#                     mm.append(int(j[0]/a)*b)
#             mx = max(mm)
#             kk.update({a: mx})
#         res.append(kk)
#                     # print(a)
#                     # print('---', int(j[0]/a)*b)
#     else:
#         for a in range(1, j[0]+1):
#             mm = []
#             for b in range(1, j[0] * j[1]):
#                 if (a ** 2) * b <= j[0] * j[1] and a * b <= j[0]:
#                     mm.append(int(j[1]/a)*b)
#             mx = max(mm)
#             kk.update({a: mx})
#         res.append(kk)
#                     # print(a)
#                     # print('---', int(j[1]/a)*b)
# # print(res)
# result = {}
# for i in range(len(res)):
#     result = dict(collections.Counter(res[i-1]) + collections.Counter(res[i]))
# # print(result)
# count = 0
# rst = []
# for q in sorted(result.values(), reverse=True):
#     if q > k:
#         rst.append(sorted(result)[count])
#     count += 1
# print(max(rst))

# 二分法
def fun(mid):
    count = 0
    for i in num:
        count += (i[0] // mid) * (i[1] // mid)
    return count >= m

n, m = map(int,input().strip().split())
num = []
for i in range(n):
    num.append(list(map(int, input().strip().split())))
l = 1
r = 10000
max = 0
while l <= r:
    mid = (l+r) // 2
    if fun(mid):
        max = mid
        l = mid + 1
    else:
        r = mid - 1
print(max)
