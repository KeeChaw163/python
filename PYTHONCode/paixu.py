#冒泡排序
def bubble_sort(list):
    for i in range(0, len(list)):
        is_sorted = True
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                is_sorted = False
        if is_sorted:
            return


list1 = [97, 3, 6, 1, 8, 5, -20, 100, 50, 200, -32, 123]
bubble_sort(list1)
print("冒泡排序：")
print(list1)
print("----------------------------------------------------------------------------------")


#选择排序
def choose_sort(list):
    list_len = len(list)
    for i in range(0, list_len):
        for j in range(i + 1, list_len):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
                

list1 = [3, 6, 1, 8, 5, -20, 100, 50, 200]
choose_sort(list1)
print("选择排序：")
print(list1)

