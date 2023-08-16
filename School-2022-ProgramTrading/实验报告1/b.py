# 定义一个函数，包含合约及价格，并进行输出

# 定义一个函数
def print_information(id, price):
    print('合约', id, '的价格是', price)


# 定义变量
stock_id = 'rb1901'
stock_price = 3100
# 调用函数
print_information(stock_id, stock_price)
