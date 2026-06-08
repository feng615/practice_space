import json

# json文件操作

user ={
    "name": "王林",
    "age": 18,
    "sex": "男",
    "habit":["看电影", "看小说", "看动画"],
       }

# 写入json文件
with open("resource/user.json", "w", encoding="utf-8") as f:
   # ensure_ascii:
    # 默认为True，如果为False，则中文会显示为Unicode编码
   # indent:
       # 缩进，默认为None
    json.dump(user, f, ensure_ascii=False, indent=4)

# 读取json文件
with open("resource/user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user)
