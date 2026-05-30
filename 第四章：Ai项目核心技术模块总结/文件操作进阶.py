# # 写文件
#
# # 打开文件
# file = open("../第三章/resource/新建文本文档.txt", "w", encoding="utf-8")
#
# try :
#     # 写入文件
#     file.write("静夜思\n\n")
#     file.write("床前明月光\n")
#     file.write("疑是地上霜\n")
#     file.write("举头望明月\n")
#     file.write("低头思故乡\n")
# finally:
#     # 关闭文件
#     file.close()

# # 写文件
#
# # 打开文件
# with open("../第三章/resource/新建文本文档.txt", "w", encoding="utf-8") as file:
#     # 写入文件
#     file.write("静夜思\n\n")
#     file.write("床前明月光\n")
#     file.write("疑是地上霜\n")
#     file.write("举头望明月\n")
#     file.write("低头思故乡\n")