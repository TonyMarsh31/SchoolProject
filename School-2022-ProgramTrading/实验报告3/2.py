# Pandas 的数据结构DataFrame的使用
import pandas as pd
import matplotlib as plt

# a 定义一个二维价格序列数据 (Open High Low Close)
ohlc_data = [
    [16.45, 16.48, 16.31, 16.41],
    [16.30, 16.30, 15.70, 15.85],
    [15.75, 15.87, 15.63, 15.86],
    [15.89, 15.92, 15.55, 15.59]
]
# 定义行索引
data_index = ['2019-11-19', '2019-11-20', '2019-11-21', '2019-11-22']
# 定义列索引
ohlc_columns = ['Open', 'High', 'Low', 'Close']
# 创建一个DataFrame对象
df = pd.DataFrame(data=ohlc_data, index=data_index, columns=ohlc_columns)
# 输出dataframe
print(df)
print(df.loc['2019-11-19'])
print(df.loc['2019-11-19', 'Close'])
print(df.loc['2019-11-19':'2019-11-21'])
print(df.loc['2019-11-19':'2019-11-21', ['High', 'Low']])
print(df.loc[:, 'Close'])

# b 进行分组
group_df = df.groupby('Open')
# 输出每一组的各类属性
print(group_df.size())
print(group_df.mean())
print(group_df.count())
print(group_df.max())


