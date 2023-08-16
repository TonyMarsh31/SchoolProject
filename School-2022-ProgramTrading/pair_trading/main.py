# 用于测试整体框架
import pandas as pd
from strategy import Strategy
from record import Position

if __name__ == '__main__':
    # 读取文件
    df = pd.read_csv('six_data.csv')
    price_A = df['RB2001'].values
    price_B = df['RB2002'].values
    # 初始化策略以及仓位类
    s = Strategy()
    position = Position()
    for i in range(len(price_A)):
        a = price_A[i]
        b = price_B[i]
        # 获取交易指令
        cmd = s.feed(a, b, position)
        # print(cmd)
        if cmd == "openAshortBlong":
            position.hold_A_price = a
            position.hold_B_price = b
            position.state = -1
            position.hold = True
            position.tradeNum += 1
        elif cmd == "stopAshortBlong":
            profit_A = position.hold_A_price - a
            profit_B = b - position.hold_B_price
            position.profit += profit_A
            position.profit += profit_B
            position.state = 0
            position.hold = False
            position.lossNum += 1
        elif cmd == "closeAshortBlong":
            profit_A = position.hold_A_price - a
            profit_B = b - position.hold_B_price
            position.profit += profit_A
            position.profit += profit_B
            position.state = 0
            position.hold = False
            position.winNum += 1
        elif cmd == "openAlongBshort":
            position.hold_A_price = a
            position.hold_B_price = b
            position.state = 1
            position.hold = True
            position.tradeNum += 1
        elif cmd == "stopAlongBshort":
            profit_A = a - position.hold_A_price
            profit_B = position.hold_B_price - b
            position.profit += profit_A
            position.profit += profit_B
            position.state = 0
            position.hold = False
            position.lossNum += 1
        elif cmd == "closeAlongBshort":
            profit_A = a - position.hold_A_price
            profit_B = position.hold_B_price - b
            position.profit += profit_A
            position.profit += profit_B
            position.state = 0
            position.hold = False
            position.winNum += 1
        elif cmd == 0:
            pass
        position.append_profit(position.profit)

# 打印回测结果
position.printResult()
# 可视化结果
position.showTradeRecord(s.mspread_list, s.open_threshold_list, s.stop_threshold_list)
