from urllib import request
import json
import pandas as pd
import tushare as ts
import pandas_datareader as web

ts.set_token('2d5b6f14449879f880fcdfe28604b95da06a6fd22485769a032056f9')
ts_pro = ts.pro_api()

df = ts_pro.daily(ts_code='600848.SH', start_date='20191101', end_date='20191201')
print(df)

df = ts_pro.daily(ts_code='600848.SH', start_date='20191101', end_date='20191201'
                  , fields='ts_code,trade_date,open,high,low,close')
print(df)
