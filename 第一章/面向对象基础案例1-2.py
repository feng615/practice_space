"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
5. 退出购物车

想法：创建两个类：商品信息类、购物车管理系统类
"""


# 商品信息类
class Goods:
    #初始化属性
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number
    # 魔法方法
    def __str__(self):
        return f"商品名称:{self.name} | 价格:{self.price} | 数量:{self.number}"

    #修改商品信息
    def modify_goods(self, name=None, price=None, number=None):
        if name is not None:
            self.name = name
            if price is not None:
                self.price = price
                if number is not None:
                    self.number = number



# 购物车管理系统类
class ShoppingCartMS:
    System_Name = '购物车管理系统'
    System_version = 2.0

    # 创建列表，存放学生信息
    def __init__(self):
        self.goods_list = []

    # 1. 添加购物车
    def add_goods(self):
        name = input("请输入要添加的商品名称：")
        for s in self.goods_list:
            if s.name == name:
                print("该商品已存在，请重新选择！！")
                return

        price = int(input("请输入要添加的商品价格："))
        goods_number = int(input("请输入要添加的商品数量："))
        # 创建名为Goods类的实例对象：s：存放商品名称、价格、数量
        s = Goods(name, price, goods_number)
        self.goods_list.append(s)

    #2. 修改购物车
    def update_goods(self):
        name = input("请输入要修改的商品名称：")
        for s in self.goods_list:
            if s.name == name:
                print(f"当前商品信息：{s}")

                price = int(input("请输入要添加的商品价格："))
                goods_number = int(input("请输入要添加的商品数量："))
                s.modify_goods(name, price, goods_number)
                print("该商品信息修改完成！！！")
                return
        print("当前商品信息不存在！！！")

    #3. 删除购物车
    def delete_goods(self):
        name = input("请输入要删除的商品名称：")
        for s in self.goods_list:
            if s.name == name:
                self.goods_list.remove(s)
                print("该商品信息已删除！！！")
                return
        print("当前商品信息不存在！！！")


    #4. 查询购物车
    def show_goods(self):
        for s in self.goods_list:
           print(s)


    #运行功能
    def run(self):
        while True:
            print(f"{ShoppingCartMS.System_Name}版本{ShoppingCartMS.System_version}")
            print("""
                    ###############################购物车管理系统################################
                    #                              1. 添加购物车                               # 
                    #                              2. 修改购物车                               # 
                    #                              3. 删除购物车                               # 
                    #                              4. 查询购物车                               # 
                    #                              5. 退出购物车                               # 
                    ##########################################################################
                    """)
            choice = input("请选择你要执行的操作(1-5)：")
            match choice:
                case "1":#1. 添加商品信息
                    self.add_goods()

                case "2":#2. 修改购物车
                    self.update_goods()

                case "3":#3. 删除购物车
                    self.delete_goods()

                case "4":#4. 查询购物车
                    self.show_goods()

                case "5":# 5. 退出购物车
                    print("Bye ~~")
                    break

                case _:#6. 其他情况
                    print("非法操作！！！，请重新选择")


#测试
if __name__ == '__main__':
    # 创建对象
    goods = ShoppingCartMS()

    # 调用方法
    goods.run()


