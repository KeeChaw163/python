# n = int(input())
# if n < 3:
#     print(1 % 10007)
# else:
#     f = [[] for i in range(n)]
#     f[0].append(1)
#     f[1].append(1)
#     for j in range(2, n):
#         f[j].append(f[j-2][0]+f[j-1][0])
#     # print(f)
#     # print(f[n-1][0])
#     print(f[n-1][0] % 10007)

n = int(input())
F = [1, 1]
if n <= 2:
    for item in range(n):
        F.append(F[item] + F[item + 1])
    print(F[n - 1] % 10007)
    # print(F)
else:
    for item in range(n - 2):
        result = (F[0] + F[1]) % 10007    # 计算出下一项后直接取余数，不影响结果
        # print(result)
        F[0], F[1] = F[1], result
    # print(F)
    print(result)  # 直接输出余数，不需要再除10007
