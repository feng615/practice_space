# 导入模块
import requests
from lxml import html
import csv

# 常量
Weather_URL ="https://www.weather.com.cn"
TOB_Weather_URL = "https://www.weather.com.cn/weather40d/101180806.shtml"

# 获取天气数据
request = requests.get(TOB_Weather_URL, timeout=60)
print(f"发送请求，获取天气数据中~")


# 解析数据
with open("csv.data/weather.csv", "w", encoding="UTF-8", newline="") as f:
    doc = html.fromstring(request.text)
    weather_list = doc.xpath("//*[@id='table']/tbody/tr[2]/td")
    for weather in weather_list:
        weather_date = weather.xpath("div[@class='sk_40']/h6/text()")
        print(weather_date)