import jieba
txt = open("D:\CODE\Example\English.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
list2 = []
list3 = []
result = []                   # 变换之后的结果
for i in words:
    if i == 'I' or i == ' ':
        list2.append(i)
        result += list2
        list2.clear()
    else:
        list1 = list(i)
        for ch in list1:
            if ch == 'I':
                ch = ch.replace('I', 'i')
            list3.append(ch)
        result += list3
        list3.clear()
print(txt)
print(''.join(result))

