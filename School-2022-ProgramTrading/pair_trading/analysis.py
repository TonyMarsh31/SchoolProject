# 数据分析模块
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.tsa.stattools import adfuller, coint


# 显示各种品种的相关性图
def showCorr(df):
    sns.heatmap(df.corr(), annot=True, square=True)
    plt.show()


# ADF平稳性检验
def ADFtest(data):
    result = adfuller(data)
    t_statistic = result[0]
    p_value = result[1]
    critical_values = result[4]
    print('t statistic value:', t_statistic)
    print('p value:', p_value)
    print('critical_values:', critical_values)
    if t_statistic < critical_values['1%']:
        print('在1%置信程度下拒绝原假设，序列数据平稳')
    elif t_statistic > critical_values['10%']:
        print('在10%置信程度下不能拒绝原假设，序列数据不平稳')


# 协整检验
def CorrIntest(dataA, dataB):
    result = coint(dataA, dataB)
    t_statistic = result[0]
    p_value = result[1]
    critical_values = result[2]
    print('t statistic value:', t_statistic)
    print('p value:', p_value)
    print('critical_values:', critical_values)
    if t_statistic < critical_values[0]:
        print('在1%置信程度下拒绝原假设，两序列数据协整')
    elif critical_values[0] < t_statistic and critical_values[1] > t_statistic:
        print('在5%置信程度下拒绝原假设，两序列数据协整')
    elif critical_values[1] < t_statistic and critical_values[2] > t_statistic:
        print('在10%置信程度下拒绝原假设，两序列数据协整')
    elif t_statistic > critical_values[2]:
        print('在10%置信程度下不能拒绝原假设，两序列数据不协整')


if __name__ == '__main__':
    df_all = pd.read_csv('six_data.csv')
    # ADF检验
    ADFtest(np.diff(df_all['RB2001']))
    ADFtest(np.diff(df_all['RB2002']))
    # 协整检验
    CorrIntest(df_all['RB2001'], df_all['RB2002'])
