"""
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1. 添加购物车：用户根据提示录入商品的价格、数量，保存该商品信息到购物车
2. 修改购物车：要求用户输入要修改的购物车商品名称，然后在提示输入该商品的价格、数量，输入完成后修改该商品信息。
3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4. 查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：xxx， 商品价格：xxx， 商品数量：xxx”
5. 退出购物车
"""


shaping_dict = {}
print("欢迎进入购物车系统！！！")
nume = """
########### 购物车系统 ############
#        1. 添加购物车            #  
#        2. 修改购物车            #  
#        3. 删除购物车            #  
#        4. 查询购物车            #  
#        5. 退出购物车            #  
#################################
"""
# 制作菜单
while True:
    print(nume)
    choice = input("请选择要执行的操作(1-5)：")

    # 执行的具体操作
    match choice:  # 添加购物车：用户根据提示录入商品的价格、数量，保存该商品信息到购物车
        case "1":
            # 提示用户输入：
            goods_name = input("请输入商品的名称：")
            goods_price = input("请输入商品的价格：")
            goods_num = input("请输入商品的数量：")
            # 判断商品是否存在购物车
            if goods_name in shaping_dict:
                print("该商品已存在，请重新选择！！！")
            else:
                shaping_dict[goods_name] = {'price': goods_price, 'num': goods_num}
        case "2":  # 修改购物车：要求用户输入要修改的购物车商品名称，然后在提示输入该商品的价格、数量，输入完成后修改该商品信息
            # 提示用户输入：
            goods_name = input("请输入商品的名称：")
            goods_price = input("请输入商品的价格：")
            goods_num = input("请输入商品的数量：")
            # 判断商品是否存在购物车
            if goods_name not in shaping_dict:
                print("该商品不存在，请重新选择！！！")
            else:
                shaping_dict[goods_name] = {'price': goods_price, 'num': goods_num}
        case "3":  # 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
            goods_name = input("请输入商品的名称：")
            # 判断商品是否存在购物车
            if goods_name not in shaping_dict:
                print("该商品不存在，请重新选择！！！")
            else:
                del shaping_dict[goods_name]
                print("该商品已删除")
        case "4":  # 4. 查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：xxx， 商品价格：xxx， 商品数量：xxx”
            for goods_name in shaping_dict.keys():
                goods_info = shaping_dict[goods_name]
                print(f"商品名称为：{goods_name}, 商品价格为：{goods_info['price']}， 商品数量为：{goods_info['num']}")
        case "5":  # 退出购物车
            print("购物车系统已退出")
            break
        case _:
            print("非法操作，请停止！！！！")






