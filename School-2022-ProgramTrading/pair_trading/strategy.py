# 主体策略模块
import numpy as np
from collections import deque


# 配对交易策略主体
class Strategy():
    # 初始化
    def __init__(self, window_len=50, k_open=2, k_stop=3):
        # 滑动窗口
        self.window_len = window_len
        # 开平仓阈值
        self.k_open = k_open
        self.k_stop = k_stop
        # 两种数据的滑动窗口
        self.A_buffer_queue = deque(maxlen=self.window_len)
        self.B_buffer_queue = deque(maxlen=self.window_len)
        # 价差列表
        self.mspread_list = []
        # 开仓止损阈值列表
        self.open_threshold_list = []
        self.stop_threshold_list = []

    # 记录数据
    def store_data(self, mspread, open_threshold, stop_threshold):
        self.mspread_list.append(mspread)
        self.open_threshold_list.append(open_threshold)
        self.stop_threshold_list.append(stop_threshold)

    # 传入新数据，返回对新数据的操作指令
    def feed(self, price_A, price_B, position):
        if len(self.A_buffer_queue) < self.window_len:
            self.A_buffer_queue.append(price_A)
            self.B_buffer_queue.append(price_B)
            return 0
        self.A_buffer_queue.append(price_A)
        self.B_buffer_queue.append(price_B)
        A_buffer_array = np.array(self.A_buffer_queue)
        B_buffer_array = np.array(self.B_buffer_queue)
        # 计算滑动窗口内的价差以及阈值
        spread = A_buffer_array - B_buffer_array
        mspread = spread - np.mean(spread)
        sigma = np.std(mspread)
        open_threshold = self.k_open * sigma
        stop_threshold = self.k_stop * sigma
        # 记录数据
        self.store_data(mspread[-1], open_threshold, stop_threshold)
        # 如果持仓
        if position.hold:
            # 如果持仓状态是 A空B多
            if position.state == -1:
                # 平仓
                if mspread[-1] <= 0:
                    return "closeAshortBlong"
                # 止损
                elif mspread[-1] > stop_threshold:
                    return "stopAshortBlong"
                else:
                    return 0
            # 如果持仓状态是 A多B空
            elif position.state == 1:
                # 平仓
                if mspread[-1] >= 0:
                    return "closeAlongBshort"
                # 止损
                elif mspread[-1] < -stop_threshold:
                    return "closeAlongBshort"
                else:
                    return 0
            else:
                return 0
        # 如果没有持仓
        else:
            # 开仓 A空B多
            if mspread[-1] > open_threshold:
                return "openAshortBlong"
            # 开仓 A多B空
            elif mspread[-1] < -open_threshold:
                return "openAlongBshort"
            # 无操作
            else:
                return 0


if __name__ == '__main__':
    s = Strategy()
