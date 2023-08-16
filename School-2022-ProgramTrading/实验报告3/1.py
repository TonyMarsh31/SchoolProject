# Pandas的数据结构 Series的使用
import pandas as pd

# 创建一个Series对象
sr = pd.Series(data=[3700, 3705, 3710, 3715, 3710], index=['11/01', '11/02', '11/03', '11/04', '11/05'])
# print(sr)

# 创建一个字典
dict = {'11/01': 3700, '11/02': 3705, '11/03': 3710, '11/04': 3715, '11/05': 3710}
# 通过字典创建一个Series对象
sr = pd.Series(data=dict)
# print(sr)

# 指定Series的name和索引的name
sr.index.name = 'date'
sr.name = 'prices'
print(sr)

print("Series对象的切片索引(通过位置索引进行切片索引)")
print(sr[0:2])
print("Series对象的切片索引(通过标签索引进行切片索引)")
print(sr['11/01':'11/03'])

print("计算差分")
print(sr.diff())

# Series对象的拼接和删除 (append | drop) 略
