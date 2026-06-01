# 导入requests模块
import requests
from lxml import html

# 获取地址
target_url = "https://www.tiobe.com/tiobe-index/"

# 获取响应
request = requests.get(target_url)


# # 打印响应
# print(request.text)

# 将响应转为HTML
doc = html.fromstring(request.text)

# 获取表头数据
th_list = doc.xpath("//*[@id='top20']/thead/tr/th/text()")
print("------>表头数据：",th_list)

# 获取表中所有数据
tr_list = doc.xpath("//*[@id='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print("------>数据：",td_list)













