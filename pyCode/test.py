# # 导入requests库
# import requests
# # 请求的URL路径和查询参数
# url = "http://www.baidu.com"
# # 发送GET请求，返回一个响应对象
# response = requests.get(url)
# # 查看响应的内容
# print(response.text)

# ========== ==========
# 导入requests库
import requests
# 请求的URL路径和查询参数
url = "http://www.baidu.com/s"
param = {"wd": "兰州文理学院"}
# 请求报头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# 发送GET请求，返回一个响应对象
response = requests.get(url, params=param, headers=headers)
# 查看响应的内容
print(response.text)
