import matplotlib.pyplot as plt
import tushare as ts
import talib
import pandas as pd
import mpl_finance as mpf
import numpy as np

ts.set_token('2d5b6f14449879f880fcdfe28604b95da06a6fd22485769a032056f9')
ts_pro = ts.pro_api()
df = ts_pro.daily(ts_code='000008.SZ', start_date='20190801', end_data='20191201',
                  fields='ts_code,trade_date,open,high,low,close,vol')
df = df.reindex(index=df.index[::-1])
df.to_csv('000008.SZ.csv', index=None)
print(df)
