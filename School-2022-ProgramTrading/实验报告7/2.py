# 制定基于RSI策略

import tushare as ts
import talib
import pandas as pd
import mpl_finance as mpf
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import ffn

matplotlib.use('module://backend_interagg')

# 是否持仓
hold = False
# 持仓数
pos = 0
# 回测资金
capital = 100000
# 剩余资金
rest = 0
# 手续费万三
fee = 0.0003
# 每日盈亏列表
capital_list = []
# 用于计算rsi指标的数组
rsi6_array = np.zeros(7)
# 读取历史数据
df = pd.read_csv('000001.SZ.csv')

# 遍历历史数据
for i in range(len(df)):
    price = df.loc[i, 'close']
    date = df.loc[i, 'trade_date']
    # 价格序列平移
    rsi6_array[0:6] = rsi6_array[1:7]
    # 将新数据追加到数组末端
    rsi6_array[-1] = price
    # 如果小于等于6个数据就跳过
    if i <= 6:
        continue
    # 计算rsi指标
    rsi6 = talib.RSI(rsi6_array,timeperiod = 6)[-1]
    # 判断是否达到开仓信号
    if rsi6 <= 20 and hold == False:
        # 计算开仓数目
        pos = int(capital / price / 100) * 100
        # 剩余资金
        rest = capital - pos * price * (1 + fee)
        # 持仓设置为True
        hold = True
        print('buy at', date, 'price', price, 'capital', capital)
    elif rsi6 >= 80 and hold == True:
        # 计算平仓后的资金
        capital = pos * price * (1 - fee) + rest
        # 持仓数设置为0
        pos = 0
        # 持仓设置为False
        hold = False
        print('sell at', date, 'price', price, capital, capital)
        # 计算每日市值
    if hold == True:
        # 如果持仓，记录当前市值
        capital_list.append(rest + pos * price)
    else:
        # 如果没有持仓，记录当前资金
        capital_list.append(capital)

# 将资金序列转换为Series对象
capital_series = pd.Series(capital_list)
# 计算资金序列的简单收益率
capital_returns = ffn.to_returns(capital_series)
# 计算收益率
print(ffn.calc_total_return(capital_series))
# 计算最大回撤
print(ffn.calc_max_drawdown(capital_series))
# 计算夏普指标
print(ffn.calc_sharpe(capital_returns))
# 可视化资金曲线
fig = plt.figure()
plt.plot(range(len(capital_list)), capital_list)
plt.show()
