"""
字符串案例
要求：邮箱格式认证：用户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.)，如果输入正确，输出“邮箱格式正确”，否则输出“邮箱格式错误”
"""

# 方式一：
# 用户输入一个邮箱
# mail = input("请输入一个邮箱：")
#
# #验证
# if mail.count('@') == 1 and mail.count('.') >= 1:
#     print(f"{mail}是合法的邮箱")
# else:
#     print(f"{mail}是非法的邮箱")

# 方式二：in 运算符---->做判断
# 用户输入一个邮箱
# mail = input("请输入一个邮箱：")
#
# #验证
# if mail.count('@') == 1 and '.' in mail:
#     print(f"{mail}是合法的邮箱")
# else:
#     print(f"{mail}是非法的邮箱")

# 练习一：输入一个字符串，判断其是否是回文(两边对称)
#输入一个字符串
# thing = input("请输入一个字符串:")
# # 判断
# if thing == thing[::-1]:
#     print(f"{thing}是回文")
# else:
#     print(f"{thing}不是回文")




# 练习二：将用户输入的十个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来

# 用户输入
# i = 1
# num_list = []
# while i <= 10:
#     thing = input(f"请输入第{i}个字符串：")
#     if thing not in num_list:
#         num_list.append(thing[::-1].upper())
#     i += 1
# print(num_list)



# 遍历
# for d in num_list:
#     print(d)


# 数据容器--tuple

# """
# 练习一：
# 根据提供的学生成绩单，完成如下需求：
# 1. 计算每个学生的总分，各科平均分，然后一并输出出来。
# 2. 统计各科成绩的最低分，最高分，平均分，并输出。
# 3. 查找成绩优秀(平均分大于90)的学生，并输出。
# """
# # 创建一个元组
# students = (
#     ('s001', '王林', 85, 92, 78),
#     ('s002', '李慕婉', 92, 88, 95),
#     ('s003', '十三', 78, 85, 82),
#     ('s004', '曾牛', 88, 79, 91),
#     ('s005', '周佚', 95, 96, 89),
#     ('s006', '王卓', 76, 82, 77),
#     ('s007', '红蝶', 89, 91, 94),
#     ('s008', '徐立国', 75, 69, 82),
#     ('s009', '许木', 86, 89, 98),
#     ('s010', '遁天', 66, 59, 72),
# )
# print("学号\t\t姓名\t\t总分\t\t平均分")
# # 方式一：
# # # 1. 计算每个学生的总分，各科平均分，然后一并输出出来
# # for s in students:
# #     total = sum(s[2:])
# #     avg = total / 3
# #     print(f"{s[0]} \t {s[1]} \t {total} \t {avg:.1f}")
#
# # 方式二：元组解包,上文的s即表示一个元组，通过五个变量直接赋值
# # 1. 计算每个学生的总分，各科平均分，然后一并输出出来
# for id, name, chinese, math, english in students:
#     total = chinese + math + english
#     avg = total / 3
#     print(f"{id} \t {name} \t {total} \t {avg:.1f}")
#
# # 2. 统计各科成绩的最低分，最高分，平均分，并输出。
#
# # 讲各科的成绩汇总
# chinese_scores = [s[2] for s in students]
# math_scores =  [s[3] for s in students]
# english_scores =  [s[4] for s in students]
#
# # 各科成绩的最低分，最高分，平均分，并输出
# print(f"语文最低分：{min(chinese_scores)} ,最高分：{max(chinese_scores)} ,平均分：{sum(chinese_scores)/ len(chinese_scores)}")
# print(f"数学最低分：{min(math_scores)} ,最高分：{max(math_scores)} ,平均分：{sum(math_scores)/ len(math_scores)}")
# print(f"英语最低分：{min(english_scores)} ,最高分：{max(english_scores)} ,平均分：{sum(english_scores)/ len(english_scores)}")
#
# # 3. 查找成绩优秀(平均分大于90)的学生，并输出。
# print("优秀学生名单如下：")
# for s in students:
#     total = sum(s[2:])
#     avg = total / 3
#     if avg > 90:
#         print(f"学号：{s[0]}, 姓名：{s[1]}, 平均分：{avg:.1f}")

# 数据容器---set
# """
# 案例一：
# 1. 找出同时选修了法语和艺术的学生
# 2. 找出同时选修了所有四门课程的学生
# 3. 找出选修了足球，但是没有选修篮球的学生
# 4. 统计每一个学生选修的课程数量
# """
# # 统计名单
#
# # 选修足球学生名单
# football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
#
# # 选修篮球学生名单
# basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
#
# # 选修法语学生名单
# french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
#
# # 选修艺术学生名单
# art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
#
# # 1. 找出同时选修了法语和艺术的学生
# # 方式一：
# s1 = french_set.intersection(art_set)
# print("同时选修了法语和艺术的学生名单如下：")
# print(s1)
#
#
# # 方式二：& ---> 求交集
# fa_set = french_set & art_set
# print(fa_set)
# print()
# # 2. 找出同时选修了所有四门课程的学生
# s2 = football_set.intersection(basketball_set)
# s3 = french_set.intersection(art_set)
# s5 = s2.intersection(s3)
# print("同时选修了所有四门课程的学生名单如下：")
# print(s5)
# print()
#
# # 3. 找出选修了足球，但是没有选修篮球的学生
# # 方式一：常用方法
# s4 = football_set.difference(basketball_set)
# print("选修了足球，但是没有选修篮球的学生名单如下：")
# print(s4)
#
#
# #方式二："-" ---> 减号也可用于寻找差集
# fb_set = football_set - basketball_set
# print(fb_set)
#
#
# # 方式三：集合推导式 {要采集的元素 for s in set if 条件}
# fb_set1  = {s for s in football_set if s not in basketball_set}
# print(fb_set1)
# print()
# # 4. 统计每一个学生选修的课程数量
# # 4.1 建立学生名单
# # 方式一：union方法，自动去重
# all_set = football_set.union(basketball_set).union(art_set).union(french_set)
# print(all_set)
# # 方式二：| ---> 表示并集
# all_set2 = football_set | basketball_set | french_set | art_set
# print(all_set2)
#
#
# # 4.2 统计课程数量
# # 采用列表嵌套集合,解包
# for s in all_set:
#     all_list = [*football_set, *basketball_set, *french_set, *art_set]
#     print(f"{s}选修的课程数量为{all_list.count(s)}")
