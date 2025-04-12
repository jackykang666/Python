class Stock:
    def __init__(self, symbol, name):
        self.__symbol = symbol             # 股票代號（私有）
        self.__name = name                 # 股票名稱（私有）
        self.__previousClosingPrice = 0.0  # 初始預設值
        self.__currentPrice = 0.0          # 初始預設值

    # 取得股票代號
    def getSymbol(self):
        return self.__symbol

    # 取得股票名稱
    def getName(self):
        return self.__name

    # 取得前一次收盤價格
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice

    # 設定前一次收盤價格
    def setPreviousClosingPrice(self, price):
        self.__previousClosingPrice = price

    # 取得目前價格
    def getCurrentPrice(self):
        return self.__currentPrice

    # 設定目前價格
    def setCurrentPrice(self, price):
        self.__currentPrice = price

    # 計算價格變動百分比
    def getChangePercent(self):
        if self.__previousClosingPrice == 0:
            return 0
        return ((self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice) * 100


# 測試程式
# 建立 Stock 物件
stock = Stock("TaiwanTech", "National Taiwan University of Science and Technology")

# 設定前一次收盤價與目前價格
stock.setPreviousClosingPrice(20.5)
stock.setCurrentPrice(20.35)

# 顯示股票資訊與價格變動百分比
print(f"股票代號：{stock.getSymbol()}")
print(f"股票名稱：{stock.getName()}")
print(f"前一次收盤價：{stock.getPreviousClosingPrice()}")
print(f"新的股票現價：{stock.getCurrentPrice()}")
print(f"價格變動百分比：{stock.getChangePercent():.2f}%")

    