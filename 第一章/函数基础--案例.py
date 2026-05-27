"""
1. 定义一个函数：根据传入的底和高计算三角形面积的函数(三角形面积 = 底 * 高 / 2)
2. 定义一个函数：计算传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)
3. 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留一位小数)，并返回。
"""



# # 1. 定义一个函数：根据传入的底和高计算三角形面积的函数(三角形面积 = 底 * 高 / 2)
# def triangle_area(l, h):
#     """
#     传入的底和高计算三角形面积的函数(三角形面积 = 底 * 高 / 2)
#     :param l: 三角形的底
#     :param h: 三角形的高
#     :return: 三角形面积
#     """
#     area = l * h / 2
#     return area
# area = triangle_area(10,7)
# print(area)
#
# #  2. 定义一个函数：计算传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)
# def statistics(a):
#     """
#     计算传入的字符串中元音字母的个数
#     :param a: 传入的字符串
#     :return: 统计的个数
#     """
#     num2 = 0
#     for num1 in a:
#         if num1 in 'aeiouAEIOU':
#             num2 += 1
#     return num2
# num = statistics('genius')
# print(num)
#
# # 3. 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留一位小数)，并返回。
# def students_grade(s):
#     students_score = (list(s))
#     score_max = max(students_score)
#     score_min = min(students_score)
#     score_avg =  round(sum(students_score) / len(students_score),1)
#     return score_max, score_min, score_avg
#
# students_score = [145, 785, 456, 654, 489, 475, 568, 753, 458]
# score = students_grade(students_score)
# print(score)

"""
1. 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
分数 >= 90: A
分数 >= 75: B
分数 >= 60: C
分数 < 60: D

2. 定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）

3. 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。

4. 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
"""

# 1. 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
def grade(g):
    """
    根据传入的分数，计算对应的分数等级
    :param g: 传入的分数
    :return: 分数等级
    """
    if g >= 90:
        return "A"
    elif g >= 75:
        return "B"
    elif g >= 60:
        return "C"
    else:
        return "D"

print(grade(60))  # C

# 2.    定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
#       把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）
def result(str_name):
    return str_name == str_name[::-1]
nume = '黄山落叶松叶落山黄'
str_result = result(nume)
print(str_result)

# 3. 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def convert_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return hours, minutes, secs

h, m, s = convert_time(3661)
print(f"{h}小时{m}分钟{s}秒")   # 1小时1分钟1秒


# 4. 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
def triangle(a, b, c):
    # 先判断能否构成三角形
    if a + b <= c or a + c <= b or b + c <= a:
        return "不能构成三角形"

    if a == b == c:
        return "等边三角形"
    elif a == b or a == c or b == c:
        return "等腰三角形"
    else:
        return "普通三角形"


print(triangle(3, 3, 3))  # 等边三角形
print(triangle(3, 3, 4))  # 等腰三角形
print(triangle(3, 4, 5))  # 普通三角形
print(triangle(1, 2, 3))  # 不能构成三角形















