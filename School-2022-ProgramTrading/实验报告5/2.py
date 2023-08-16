# 通过新浪财经API获取历史数据 【股票数据，期货数据】
from urllib import request
import json
import pandas as pd
import pandas_datareader as web


def get_stock_data(id, scale, data_len):
    # 拼接API的url
    url = 'http://quotes.sina.cn/cn/api/json_v2.php/CN_MarketDataService.getKLineData?symbol={0}&scale={1}&datalen={2}'.format(
        id, scale, data_len)
    # 发起请求
    req = request.Request(url)
    # 获取响应
    rsp = request.urlopen(req)
    # 读取响应结果
    res = rsp.read()
    # 将json序列转换为Python对象
    res_json = json.loads(res)
    # bar列表
    bar_list = []
    # 将结果逆序
    res_json.reverse()
    # 遍历列表
    for dict in res_json:
        bar = {}
        bar['date'] = dict['day']
        bar['open'] = float(dict['open'])
        bar['high'] = float(dict['high'])
        bar['low'] = float(dict['low'])
        bar['close'] = float(dict['close'])
        bar['vol'] = int(dict['volume'])
        bar_list.append(bar)
    # 将结果转换为DataFrame对象
    df = pd.DataFrame(data=bar_list)
    return df


def get_future_date(id, scale):
    # 拼接API的url
    url = 'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine{0}m?symbol={1}'.format(
        scale, id)
    # 发起请求
    req = request.Request(url)
    rsp = request.urlopen(req)
    res = rsp.read()
    res_json = json.loads(res)
    print(res_json)
    bar_list = []
    res_json.reverse()
    for line in res_json:
        bar = {}
        bar['date'] = line[0]
        bar['open'] = float(line[1])
        bar['high'] = float(line[2])
        bar['low'] = float(line[3])
        bar['close'] = float(line[4])
        bar['vol'] = int(line[5])
        bar_list.append(bar)
    df = pd.DataFrame(data=bar_list)
    return df


df = get_stock_data('sh000001', 5, 5)
print(df)

df = get_future_date('rb1910', 5)
print(df)
