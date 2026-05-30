# 导入lxml模块
from lxml import html


# 获取HTML的源码
with open("resources/仙逆人物志.html", "r", encoding="utf-8") as file:
    html_text = file.read()
    #print("------>获取的文本数据：",html_text)


# 获取HTML的文本数据
doc = html.fromstring(html_text)

#解析表头
headers = doc.xpath("//table/thead/tr/th/text()")
#print("------>表头：",headers)

#解析表中数据
rows = doc.xpath("//table/tbody/tr[1]/td/text()")
#print("------>表中数据：",rows)

#解析表中所有的数据
all_rows = doc.xpath("//table/tbody/tr")
for row in all_rows:
    row_data = row.xpath("td/text()")
    print("------>表中数据：",row_data)