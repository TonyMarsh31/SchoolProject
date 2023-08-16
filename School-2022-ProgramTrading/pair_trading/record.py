# 回测结果模块

import numpy as np
import matplotlib.pyplot as plt
import ffn
import pandas as pd
import matplotlib

np.seterr(divide='ignore', invalid='ignore')
matplotlib.use('module://backend_interagg')


# 仓位主体，监控回测仓位变化以及统计回测结果
class Position():
    def __init__(self):
        # 持仓状态 0空仓 -1A空B多  1A多B空
        self.state = 0
        # 当前累计收益
        self.profit = 0
        # 累计收益列表
        self.profit_list = []
        # 持仓价格
        self.hold_A_price = 0
        self.hold_B_price = 0
        self.hold = False
        # 交易次数
        self.tradeNum = 0
        # 盈利次数
        self.winNum = 0
        # 损失次数
        self.lossNum = 0

    # 追加累计收益
    def append_profit(self, profit):
        self.profit_list.append(profit)

    # 展示交易记录图像
    def showTradeRecord(self, mspread, open, stop):
        fig = plt.figure()
        # 收益图
        ax1 = fig.add_subplot(211)
        ax1.plot(range(len(self.profit_list)), self.profit_list)
        ax1.set_title('Profit Record')
        # 开仓以及止损阈值
        ax2 = fig.add_subplot(212)
        open = np.array(open)
        stop = np.array(stop)
        ax2.plot(range(len(mspread)), mspread)
        ax2.plot(range(len(open)), open, c='r')
        ax2.plot(range(len(stop)), stop, c='b')
        ax2.plot(range(len(open)), -open, c='r')
        ax2.plot(range(len(stop)), -stop, c='b')
        ax2.set_title('mspread & open threshold & stop threshold')
        ax2.legend(['mspread', 'open', 'stop'])
        plt.tight_layout()
        plt.show()

    # 计算最大回撤
    def cal_maxDrawdown(self, profit_list):
        profit_series = pd.Series(data=profit_list)
        return ffn.calc_max_drawdown(profit_series)

    # 计算夏普比率
    def cal_sharpeRatio(self, profit_list):
        profit_series = pd.Series(data=profit_list)
        return ffn.calc_sharpe(profit_series)

    # 打印回测结果
    def printResult(self):
        winRate = self.winNum / self.tradeNum
        maxDrawdown = self.cal_maxDrawdown(self.profit_list)
        sharpeRatio = self.cal_sharpeRatio(self.profit_list)
        print('交易次数：', self.tradeNum)
        print('盈利次数：', self.winNum)
        print('胜率：', winRate)
        print('最大回撤率：', maxDrawdown)
        print('夏普比率：', sharpeRatio)
