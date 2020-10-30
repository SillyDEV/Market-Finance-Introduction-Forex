import config
from pyti.exponential_moving_average import exponential_moving_average as ema

def rangeDetector(data):
    SEma = ema(data["bidclose"], 55)
    FEma = ema(data["bidclose"], 21)

    delta = SEma[len(SEma) - 1] - FEma[len(FEma) - 1]
    if delta < 0:
        delta = delta * -1
    if delta > config.rangeDelta:
        config.inRange = False
        mainTrend(data)
        config.amount = config.baseAmount * (delta * 0.5)
    else:
        config.amount = config.baseAmount
        config.inRange = True
        config.trend = None
    print("trend: " + str(config.trend) + "Range: " + str(config.inRange))

def mainTrend(data):
    SEma = ema(data["bidclose"], 55)
    FEma = ema(data["bidclose"], 21)

    delta = SEma[len(SEma) - 1] - FEma[len(FEma) - 1]
    if delta > 0:
        config.trend = False
    else:
        config.trend = True