import re
words=open("D:\CODE\Example\English.txt", "r", encoding='utf-8').read()
l=re.split('[\. ]+',words)  #使用空格分隔词语，得到各个单词
print(l)
i=0
print (words)
for i in l:
    if len(i)==3:  #如果单词的长度为3  输出
        print (i)