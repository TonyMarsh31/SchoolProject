# 数据获取模块
import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


# 数据获取函数
def get_data(ids, start_date, end_date, path):
    # 初始化接口
    ts_pro = ts.pro_api('2d5b6f14449879f880fcdfe28604b95da06a6fd22485769a032056f9')
    # 用于合并所有数据
    all_df = pd.DataFrame()
    # 获取历史数据
    for id in ids:
        # 拼接接口为ts_code格式
        ts_code = id + '.SHF'
        # 调用接口
        df = ts.pro_bar(ts_code=ts_code, start_date=start_date, end_date=end_date, asset='FT', freqs='5min')
        # 逆序
        df = df.reindex(index=df.index[::-1])
        # 获取收盘价
        df = df[['trade_time', 'close']]
        df.columns = ['trade_time', 'id']
        df = df.set_index('trade_time')
        # 合并DataFrame
        all_df = pd.concat((all_df, df), axis=1)
        # 暂停进程5s
        time.sleep(5)
    # 保存到本地
    all_df.to_csv(path)


if __name__ == '__main__':
    # 螺纹钢期货id
    ids = ['Rb1911', 'Rb1912', 'Rb2001', 'Rb2002', 'Rb2003', 'Rb2004']
    # 起止日期
    start_date = '20191020'
    end_date = '20191030'
    # 调用函数
    get_data(ids, start_date, end_date, 'six_data.csv')
