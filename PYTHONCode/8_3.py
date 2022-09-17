import re
str= input("请输入：")    # 设置字符串
pattern = re.compile(r'\b(\w+)(\s+\1){1,}\b')
  # \b 匹配单词和空格间的位置
  # \w 匹配包括下划线的任何单词字符 [A-Za-z0-9_]
  # \s 匹配任何空白字符
  # {1,} 大于 1 个
matchResult = pattern.search(str)
  # 查找这样的结果
str = pattern.sub(matchResult.group(1),str)
  # sub 进行替换字符
  # group(1) 为 is   group(0) 为is is
print(str)