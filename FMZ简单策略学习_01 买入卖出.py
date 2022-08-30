#交易所交易对
#获取当前的行情   "获取行情ticker、获取深度depth、获取K线records、获取成交记录trades"
# 获取K线
#获取账户

#买入
#卖出


'''backtest
start: 2022-08-26 10:00     #开始时间
end:   2022-08-26 15:00     #结束时间
period: 1h                   #周期
exchanges: [
    {"eid":"Bitfinex","currency":"BTC_USD"},   #平台和币种的信息
]
'''

#获取当前的行情
ticker = exchange.GetTicker()         #	High: 21557.001 Low: 21556.999 Sell: 21557.001 Buy: 21556.999 Last: 21557.0 Volume: 0.0
Log(
    "High:",ticker["High"],
    "Low:", ticker["Low"],
    "Sell:", ticker["Sell"], 
    "Buy:", ticker["Buy"],
    "Last:", ticker["Last"],
    "Volume:", ticker["Volume"]
    )
#获取深度depth
depth = exchange.GetDepth()
buyprice = depth["Bids"][0]["Price"]
sellprice = depth["Asks"][0]["Price"]
Log("买一价为:", buyprice,"卖一价为:", sellprice)
# 获取K线
records = exchange.GetRecords(PERIOD_H1)
Log("第一根k线数据为，Time:", records[0]["Time"], "Open:", records[0]["Open"], "High:", records[0]["High"])
# 获取账户进行交易
account = exchange.GetAccount()
Log(account)    #{'Balance': 50000.0, 'FrozenBalance': 0.0, 'Stocks': 3.0, 'FrozenStocks': 0.0}

#下买单
while True:
    ticker = exchange.GetTicker()
    price = ticker.Sell
    if price >= 21556.999:
        exchange.Buy(_N(price + 5, 2), 1, 'BTC_USD')
        break

Sleep(3000)  # Sleep3000ms
Log('买入完成啦')
#下卖单
while True:
    ticker = exchange.GetTicker()
    price = ticker.Sell
    if price >= 21557.001:
        exchange.Sell(_N(price + 5, 2), 1, 'BTC_USD')
        break

Log('卖出完成啦')

