from collections import Counter     #导入Counter
print("输入字符串")
data=input()            #手动输入
datalist=data.split(",")    #分割字符串
#print(datalist)
data=datalist
#data=['hello','world','python','aaabbb','cccdd']
print(data)         #输出字符串列表
for i in data:      #for循环
    a=Counter(i)        #对列表中每一个字符串进行计数
    #print(Counter(i))
    maxlen=0
    for j in a:
        #print(key,a[j])        #输出的是字母和个数
        if maxlen< a[j]:
            maxlen= a[j]        #得到字符串中字母重复最多的
    #print(maxlen)      #输出重复数量
    if maxlen <= len(i)/2:      #重复最多的字母的重复个数与该字符长度比较，没有超过一半则输出该字符串
        print(i)

