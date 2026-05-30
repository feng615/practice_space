import  json

user_info = {
    "name": "王林",
    "age": 18,
    "sex": "男",
    "habit":["看电影", "看小说", "看动画"],
       }

# 写入json文件
with open("resource/user.json", "w", encoding="utf-8") as f:
    json.dump(user_info, f, ensure_ascii=False, indent=4)
    print("写入成功")

# 读取json文件
with open("resource/user.json", "r", encoding="utf-8") as f:
    user_info = json.load(f)
    print(user_info)