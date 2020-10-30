#Connection
#  Rod token
# token = '482ce88dc0ef662a1bc9c526a29ea4e8a71eddea'
# Arthur token
#token = '74ef7d725e19d53c9113702e7bde3cfdf485459a'
# Mouli token
token = 'be785a59a293b8e22b4a7bf70eaa3e9ac6436707'
con = None

#Main configuration
mode = None
print = None
customStrategy = None

#MainData
numberofcandles = 400
pricedata = None
heikenHashi = None
currency = None
period = None

#ContextualisationData
backPeriod = None
backdata = None
rangeDelta = 0.00035
inRange = False
trend = False
contextSignal = 0
signalLatency = 10
contextTrend = 0

# Money Management
baseAmount = 100
amount = 100
stop = -10
limit = 30

#EnterPositionIndicator
enterBollinger = False
enterEma = False
enterRsi = False
enterStock = False

#ClosePositionIndicator
closeBollinger = False
closeEma = False
closeRsi = False
closeStock = False

#HeikenAshi
traillingStop = None
openPrice = 0
marge = 0.0003
lastChange = 0

#Backtesting File
back_file = None
FullDataframe = None
MyPosition = None
TradeWin = 0
TradeLoss = 0
PipsProfit = 0