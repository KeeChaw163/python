# 声明用于存放素数的列表
primNumber = []
print("请输入正整数：")
# 接收键盘输入
num = input()
# 判断是否为整数，如果不是，结束程序
if num.isdigit():
    # num转化为int类型
    num = eval(num)
    if num > 2:
        # i即为要寻找的素数，常识可知，第一个是2，从2遍历到num
        for i in range(2, num):
            # flag用于标记当前的数是否为素数（true：素数，false：合数）
            flag = True
            # k从2开始遍历到根号i即可，这里图方便，遍历到i/2+1
            for k in range(2, int(i/2) + 1):
                # 判断i是否可被k整除，如果可以，直接判断为合数
                if i % k == 0:
                    flag = False
                    break
            if flag:
                primNumber.append(i)
        print(primNumber)
    else:
        print("输入是数字不能小于2！")
else:
    print("输入了非法字符！")