# 文件操作入门

#读文件
# 打开文件
file = open("resource/新建 文本文档.txt", "r", encoding="utf-8")

#读取文件
print(file.read())

#关闭文件
file.close()


#创建一个文件
# 打开文件
file = open("resource/message.txt", "w", encoding="utf-8")
# 写入文件
file.write("静夜思\n\n")
file.write("床前明月光\n")
file.write("疑是地上霜\n")
file.write("举头望明月\n")
file.write("低头思故乡\n")

# 关闭文件
file.close()