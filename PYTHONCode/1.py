friends_list = []
print("欢迎使用好友管理系统")
print("1：添加好友")
print("2：删除好友")
print("3：备注好友")
print("4：展示好友")
print("5：退出")

while True:
    zhuye = int(input("请选择你的操作："))
    if zhuye == 1:
        friend = input("请输入要添加好友姓名")
        friends_list.append(friend)
        print("添加成功！")
    elif zhuye == 2:
        friend = input("请输入要删除好友姓名")
        friends_list.remove(friend)
        print("删除成功！")
    elif zhuye == 3:
        old_name = input("请输入要修改的好友姓名")
        index = friends_list.index(old_name)
        new_name = input("请输入备注名")
        friends_list[index] = new_name
        print('备注成功')
    elif zhuye == 4:
        if len(friends_list):  # 存在值即为真
           print(f'我的好友列表是：{sorted(friends_list)}') 
        else:# list_temp是空的
            pirint("列表为空")
    elif zhuye == 5:
        break
print("程序结束！")

