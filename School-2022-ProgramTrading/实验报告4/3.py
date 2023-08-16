# 金融数据的可视化操作，如：K线数据的可视化，成交量的可视化

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf

df = pd.read_csv('./000001_Daily_2006_2018.csv')[:50]

fig = plt.figure()
ax = fig.add_subplot(111)
mpf.candlestick2_ohlc(ax, df['Open'], df['High'], df['Low'], df['Close'], colordown='green', colorup='red', width=0.6)
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
mpf.candlestick2_ohlc(ax1, df['Open'], df['High'], df['Low'], df['Close'], colordown='green', colorup='red', width=0.6)
mpf.volume_overlay(ax2, df['Open'], df['High'], df['Vol'], colordown='green', colorup='red', width=0.6)
plt.tight_layout()
plt.show()
