"""
示例一：
定义一个类描述数字时钟，提供走字和显示时间的功能。
"""
import time
# 定义一个时钟类
class Clock:
    def __init__(self,hour,minute,second):
        # 初始化
        self.hour = hour
        self.min = minute
        self.sec = second
# 提供走字
    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0



# 显示时间
    def show(self):
       """显示时间"""
       return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'

# 创建对象：clock,clock1
clock = Clock(23, 59, 58)
clock1 = Clock(10,45,60)

# 调用
while True:
    # 给时钟对象发消息读取时间
    print(clock.show())
    # 休眠1秒钟
    time.sleep(1)
    # 给时钟对象发消息使其走字
    clock.run()

