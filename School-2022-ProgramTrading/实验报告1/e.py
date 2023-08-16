# 创建一个策略类，进行长短线操作

# 创建一个父类
class Strategy():
    # 类变量
    strategy_name = 'CTA策略'

    # 构造函数
    def __init__(self, parameter):
        # 实例变量
        self.parameter = parameter

    def __long__(self, price):
        print('在价位', price, '进行做多')

    def sell(self, price):
        print('在价位', price, '进行平多')


# 创建一个子类
class Strategy_Future(Strategy):
    def short(self, price):
        print('在价位', price, '进行做空')

    def cover(self, price):
        print('在价位', price, '进行平空')
