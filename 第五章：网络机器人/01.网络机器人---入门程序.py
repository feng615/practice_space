# 导入requests模块
import requests

# 获取地址
target_url = "https://www.tiobe.com/tiobe-index/"

# 获取响应
request = requests.get(target_url)


# 打印响应
print(request.text)