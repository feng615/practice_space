"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
5. 展示全部学生成绩：展示出系统中所有学生的成绩

开发需求：学生类、教务管理系统类
"""

# 学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"学生：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"

    def update_score(self,name=None, chinese=None, math=None, english=None):
        if name is not None:
            self.name = name
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


# 教务管理系统类
class ManagementSystem:
    System_Name = '教务管理系统'
    System_version = 1.0

    def __init__(self):
        self.student_list = []
    #1. 添加学生成绩
    def add_grades(self):
        # 输入学生姓名
        name = input("请输入要添加的学生姓名：")
        # 判断学生是否存在
        for s in self.student_list:
            if s.name == name:
                print("无法添加，该学生已存在")
                return

        chinese = int(input("请输入要添加的语文成绩："))
        math = int(input("请输入要添加的数学成绩："))
        english =int( input("请输入要添加的英语成绩："))

        # 判断学生成绩是否在0-100之间
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)

        else:
            print("成绩超出范围，请重新添加！！！")


    #2. 修改学生成绩
    def update_grades(self):
        # 输入学生姓名
        name = input("请输入要修改的学生姓名：")
        # 判断学生是否存在
        for s in self.student_list:
            if s.name == name:
               print(f"当前成绩为：{s}")

               chinese = int(input("请输入要修改的语文成绩："))
               math = int(input("请输入要修改的数学成绩："))
               english = int(input("请输入要修改的英语成绩："))

               # 判断学生成绩是否在0-100之间
               if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                   s.update_score(name, chinese, math, english)
                   print("成绩修改完成！！")
                   print(f"修改后的成绩：{s}")
                   return
               else:
                   print("学生成绩应在0-100之间！！！")
                   return

        print("要修改的学生不存在！！！")

    #3. 删除学生成绩
    def del_score(self):
        # 输入学生姓名
        name = input("请输入要删除的学生姓名：")
        # 判断学生是否存在
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("该学生信息已删除！！！")
                return
        else:
            print("要删除的学生信息不存在！！")




    #4. 查询指定学生成绩
    def query_student(self):
        # 输入学生姓名
        name = input("请输入要查询的学生姓名：")
        # 判断学生是否存在
        for s in self.student_list:
            if s.name == name:
                print(s)
                return
        else:
            print("要查询的学生信息不存在！！")

    #5. 展示全部学生成绩
    def show_student(self):
        for s in self.student_list:
            print(s)


    def run(self):
        print(f"教务管理系统版本{ ManagementSystem.System_version}")
        while True:
            print("""
            #################################教务管理系统#############################
            #                             1. 添加学生成绩                            #
            #                             2. 修改学生成绩                            #
            #                             3. 删除学生成绩                            #
            #                             4. 查询指定学生成绩                         #
            #                             5. 展示全部学生成绩                         #
            #                             6. 退出系统                                #
            #########################################################################
            """)
            choice = input( "请选择你要执行的操作(1-6)：")
            try:
                match choice:# 1. 添加学生成绩
                    case "1":
                        self.add_grades()
                    case "2":# 2. 修改学生成绩
                        self.update_grades()
                    case "3":# 3. 删除学生成绩
                        self.del_score()
                    case "4":# 4. 查询指定学生成绩
                        self.query_student()
                    case "5":# 5. 展示全部学生成绩
                        self.show_student()
                    case "6":# 6. 退出系统
                        print("Bye ~~")
                        break
                    case _:# 其他情况
                        print("非法操作，请重新选择你要执行的操作(1-6)")
            except ValueError:
                print("数据添加有误，请重新添加！！！")
            except Exception:
                print("程序出现问题，请联系管理员！！！")

if __name__ == '__main__':
    edu = ManagementSystem()
    edu.run()
