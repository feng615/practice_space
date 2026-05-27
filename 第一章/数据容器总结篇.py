"""
开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成后保存到系统中
2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5. 列出所有学生： 遍历所有学生信息并输出。
6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
7. 退出系统。
"""

students_message = {}
print("欢迎进入教务管理系统！！！")
menu = """
############################## 教务管理系统 ##############################
#                           1. 添加学生信息                              #
#                           2. 修改学生信息                              #
#                           3. 删除学生信息                              #
#                           4. 查询学生信息                              #
#                           5. 列出所有学生                              #
#                           6. 统计班级成绩                              #
#                           7. 退出系统                                 #
########################################################################
"""

# 制作菜单
while True:
    print(menu)
    choice = input("请选择你要执行的操作(1-7)")

    # 具体执行的功能
    match choice:
        case "1":  # 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成后保存到系统中
            # 提示录入
            name = input("请录入学生的姓名：")
            # 先判断学生姓名是否存在系统
            if name in students_message:
                print("该学生已录入教务系统，请重新选择你要执行的操作")
                continue

            chinese_score = float(input("请录入学生的语文成绩："))
            math_score = float(input("请录入学生的数学成绩："))
            english_score = float(input("请录入学生的英语成绩："))
            students_message[name] = {'chinese': chinese_score, 'math': math_score, 'english': english_score}
        case "2":  # 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
            name = input("请录入学生的姓名：")
            if name not in students_message:
                print("该学生未录入教务系统，请重新选择你要执行的操作")
                continue

            chinese_score = float(input("请录入学生的语文成绩："))
            math_score = float(input("请录入学生的数学成绩："))
            english_score = float(input("请录入学生的英语成绩："))
            students_message[name] = {'chinese': chinese_score, 'math': math_score, 'english': english_score}
        case "3":  # 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
            name = input("请录入学生的姓名：")
            if name not in students_message:
                print("该学生未录入教务系统，请重新选择你要执行的操作")
                continue
            #
            del students_message[name]
            print("该学生信息已删除")
        case "4":  # 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
            name = input("请录入学生的姓名：")
            if name not in students_message:
                print("该学生未录入教务系统，请重新选择你要执行的操作")
                continue

            student_info = students_message[name]
            print(
                f"学生姓名：{name}, 语文成绩：{student_info['chinese']}, 数学成绩为：{student_info['math']}, 英语成绩：{student_info['english']}")

        case "5":  # 5. 列出所有学生： 遍历所有学生信息并输出。
            for name in students_message.keys():
                student_info = students_message[name]
                print(
                    f"学生姓名：{name}, 语文成绩：{student_info['chinese']}, 数学成绩为：{student_info['math']}, 英语成绩：{student_info['english']}")

        case "6":  # 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
            if not students_message:
                print("系统中暂无学生信息")
                continue

            chinese_scores = [s['chinese'] for s in students_message.values()]
            math_scores = [s['math'] for s in students_message.values()]
            english_scores = [s['english'] for s in students_message.values()]

            # 找最高/最低分学员
            chinese_max = max(students_message.items(), key=lambda x: x[1]['chinese'])
            chinese_min = min(students_message.items(), key=lambda x: x[1]['chinese'])
            #  数学同理
            math_max = max(students_message.items(), key=lambda x: x[1]['math'])
            math_min = min(students_message.items(), key=lambda x: x[1]['math'])
            #  英语同理
            english_max = max(students_message.items(), key=lambda x: x[1]['english'])
            english_min = min(students_message.items(), key=lambda x: x[1]['english'])

            print(
                f"语文：最高{max(chinese_scores)}({chinese_max[0]}), 最低{min(chinese_scores)}({chinese_min[0]}), 平均{sum(chinese_scores) / len(chinese_scores):.2f}")
            print(
                f"数学：最高{max(math_scores)}({math_max[0]}), 最低{min(math_scores)}({math_min[0]}), 平均{sum(math_scores) / len(math_scores):.2f}")
            print(
                f"英语：最高{max(english_scores)}({english_max[0]}), 最低{min(english_scores)}({english_min[0]}), 平均{sum(english_scores) / len(english_scores):.2f}")
        case "7":
            print("教务系统已退出")
            break

        case _:
            print("非法操作，请重新选择!!!")
