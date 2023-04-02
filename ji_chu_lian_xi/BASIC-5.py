n = int(input())
str = input().split(" ")
fi = input()
if fi in str:
    # for i in range(len(str)):
    #     if str[i] == fi:
    #         print(i+1)
    #         break
    print(str.count(fi))
else:
    print(-1)