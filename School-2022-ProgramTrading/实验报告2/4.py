# 股票收盘价的收益率、10日和20日均线的计算

import numpy as np

# 定义价格序列
close_price = np.array([10.90, 10.91, 10.23, 10.24, 10.12, 10.13, 10.22])
# 计算简单收益率
sim_return_rate = np.diff(close_price)
print(sim_return_rate)


# 定义滑动窗口
def cal_sliding_window(series, size):
    # 定义一个数组存储每个滑动窗口
    windows_arr = np.zeros(shape=(len(series) - size + 1, size))
    # 遍历序列
    for i in range(len(series) - size + 1):
        # 截取窗口
        window = series[i: i + size]
        windows_arr[i] = window
    return windows_arr


# 调用函数
windows = cal_sliding_window(close_price, 3)
print(windows)


# 计算均线
def cal_MA(series, period=10):
    # 定义数据存储MA
    ma_arr = np.zeros(shape=len(series) - period + 1)
    # 将数据转换为滑动窗口
    windows = cal_sliding_window(series, period)
    for i in range(len(windows)):
        ma_arr[i] = np.mean(windows[i])
    return ma_arr


# 定义价格序列
price = np.random.normal(loc=10, scale=1, size=20)
# 计算MA
ma_arr = cal_MA(price)
print(ma_arr)
