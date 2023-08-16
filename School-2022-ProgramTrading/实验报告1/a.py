# 定义一个价格列表，以及买入、卖出价位，循环遍历价格，进行买卖操作

# 定义一个价格列表
price_list = [5.78, 5.80, 5.91, 6.23, 6.22, 6.73, 6.62]
# 定义一个买入价位
buy_price = 5.78
# 定义一个卖出价位
sell_price = 6.22
# 定义是否持仓
position = False
# for循环遍历价格
for price in price_list:
    if price > buy_price and not position:
        print('but at', price)
        position = True
    elif price > sell_price and position:
        print('sell at', price)
        position = False
    else:
        print('do nothing')
