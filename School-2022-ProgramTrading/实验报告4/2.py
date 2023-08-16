# Matplotlib库对图像信息的基本设置及子图创建
# 注意：前两句代码 是来设置中文编码

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf

df = pd.read_csv('./000001_Daily_2006_2018.csv')[:50]

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(df['Close'], c='r', linestyle='-', marker='o', label='Close price')
plt.plot(df['High'], c='g', linestyle='--', marker='*', label='High price')
plt.plot(df['Low'], c='c', linestyle='-.', marker='^', label='Low price')
plt.plot(df['Open'], c='y', linestyle=':', marker='D', label='Open price')
plt.title('000001 收盘价')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)
ax1.plot(df['Close'], c='r', linestyle='-', marker='o')
ax2.plot(df['High'], c='g', linestyle='--', marke='*')
ax3.plot(df['Low'], c='c', linestyle='-.', marker='^')
ax4.plot(df['Open'], c='y', linestyle=':', marker='D')
ax1.set_title('Close price')
ax1.set_xLabel('Time')
ax1.set_ylabel('Price')
ax1.grid(True)
plt.tight_layout()
plt.show()
