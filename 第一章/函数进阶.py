"""
案例二： 定义一个根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额的函数
具体规则如下：
        1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
        2. 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣一元(且抵扣金额不能超过商品总价，积分只能整百抵扣)。
"""
def calculate_goods_amount(*args:tuple[str,float,int],coupon=0,points=0,fare=0):
    """
    传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额
    :param args: (商品名、价格、数量)
    :param coupon: 优惠券
    :param points: 积分抵扣
    :param fare: 运费
    :return: 订单的总金额
    """
    # 1.计算商品总金额(单件商品金额=价格*数量)、商品总金额=sum(单件商品金额)
    goods_cost = [goods[1] * goods[2] for goods in args]
    total_cost = sum(goods_cost)

    # 2. 优惠券抵扣
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon


    # 3.  积分抵扣
    points_cost = points // 100
    if total_cost >= 5000 and points_cost <= total_cost:
        total_cost -= points_cost



    # 运费
    total_cost += fare
    return total_cost

# goods_info = (
#     ('手机',3989,1),
#     ('巧克力',236,2),
#     ('玩偶',1999,2)
#
# )
# goods_cost1 = calculate_goods_amount(*goods_info,coupon=100,points=1000,fare=10)
# print(goods_cost1)

goods_cost1 = calculate_goods_amount(('手机',3989,1),('巧克力',236,2),('玩偶',1999,2))
print(goods_cost1)