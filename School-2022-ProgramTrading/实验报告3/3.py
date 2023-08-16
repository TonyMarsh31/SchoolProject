import pandas as pd
import numpy as np


def cal_RSI(close, periods):
    # 序列的长度
    length = len(close)
    print(length)
    # 定义序列
    rsies = [np.nan] * length
    if length <= periods:
        return rsies
    # 平均上涨幅度
    up_avg = 0
    # 平均下降幅度
    down_avg = 0
    # 计算第一个周期内的RSI指标
    first_t = close[:periods + 1]
    for i in range(1, len(first_t)):
        if first_t[i] >= first_t[i - 1]:
            up_avg += first_t[i] - first_t[i - 1]
        else:
            down_avg += first_t[i - 1] - first_t[i]
    up_avg = up_avg / periods
    down_avg = down_avg / periods
    rs = up_avg / down_avg
    rsies[periods] = 100 - 100 / (1 + rs)

    # 计算后面的RSI指标
    for j in range(periods + 1, length):
        if close[j] >= close[j - 1]:
            up = close[j] - close[j - 1]
            down = 0
        else:
            up = 0
            down = close[j - 1] - close[j]
        up_avg = (up_avg * (periods - 1) + up) / periods
        down_avg = (down_avg * (periods - 1) + down) / periods
        rs = up_avg / down_avg
        rsies[j] = 100 - 100 / (1 + rs)
    return pd.Series(rsies)


df = pd.read_csv('./000001_Daily_2006_2018.csv')
df['RSI'] = cal_RSI(df['Close'], 5)
print(df[0:30])
