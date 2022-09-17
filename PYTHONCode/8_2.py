str = input("请输入：")
import re
pattern = re.compile(r'(?:[^\w]|\b)i(?:[^\w])')
while True:
    result = pattern.search(str)
    if result:
        if result.start(0) != 0:
            str = str[:result.start(0)+1]+'I'+str[result.end(0)-1:]
        else:
            str = str[:result.start(0)]+'I'+str[result.end(0)-1:]
    else:
        break
print(str)