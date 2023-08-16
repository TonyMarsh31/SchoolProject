# Matplotlib库绘制常见图像,如:折线图、柱状图等

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf

df = pd.read_csv('./000001_Daily_2006_2018.csv')[:50]
fig = plt.figure()
plt.plot(df['Close'])
plt.show()

plt.plot(df['Open'])
plt.show()

y = np.array([1000, 1001, 1003, 1006, 1002, 1006])
y2 = np.array([1003, 1006, 1002, 1006, 1002, 1008])
x = range(len(y))
x2 = range(len(y2))
plt.plot(x, y)
plt.plot(x2, y2)
plt.show()

plt.hist(df['Close'])
plt.show()

plt.hist(df['Close'], bins=5)
plt.show()

plt.bar(df['date'], df['Vol'])
plt.show()

plt.scatter(df['Close'], df['Open'])
plt.show()

x = [30, 20, 10, 40]
label = ['A', 'B', 'C', 'D']
plt.pie(x, labels=label, autopct='%1.1f%%')
plt.show()
