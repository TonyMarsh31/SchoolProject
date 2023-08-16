import matplotlib.pyplot as plt
import tushare as ts
import talib
import pandas as pd
import mpl_finance as mpf
import numpy as np

# K线组合的模式识别(晨星、昏线、锤子线)

df = pd.read_csv('000008.SZ.csv')
# 识别上吊线的K线组合
nums = talib.CDLHANGINGMAN(df['open'], df['high'], df['low'], df['close'])
# 可视化
fig = plt.figure()
ax = fig.add_subplot(111)
# 绘制K线图
mpf.candlestick2_ohlc(ax, df['open'], df['high'], df['low'], df['close'], width=0.6, colorup='red', colordown='green')
# 标注识别K线组合的位置
index = nums[nums == -100].index.values
for i in index:
    ax.annotate(s='', xy=(i, df['high'][i]), xytext=(i, df['high'][i] + 0.2), arrowprops={'arrowstyle': '->'})
plt.show()
