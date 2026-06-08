# csv操作：方法一：原始方法

# 打开文件
with open("csv.data/01.csv", "w", encoding="utf-8") as f:

    # 写入数据
    f.write("姓名,年龄,性别,爱好\n")# 写入表头
    f.write("小王,18,男,football\n")# 写入数据
    f.write("小张,19,女,basketball\n")
    f.write("小李,20,男,swimming\n")

# 读取数据
with open("csv.data/01.csv", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# csv操作：方法一：csv模块
import csv
# newline="": 解决换行问题
# csv.DictWriter: 创建csv写入对象会出现自动换行
with open("csv.data/02.csv", "w", encoding="utf-8", newline="") as f:
    # 创建csv写入对象
    writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"])
    # 写入数据
    writer.writeheader()# 写入表头
    writer.writerow({"姓名": "小王", "年龄": "18", "性别": "男", "爱好": "football"})
    writer.writerow({"姓名": "小张", "年龄": "19", "性别": "女", "爱好": "basketball"})
    writer.writerow({"姓名": "小李", "年龄": "20", "性别": "男", "爱好": "swimming"})

#读取数据
with open("csv.data/02.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)

