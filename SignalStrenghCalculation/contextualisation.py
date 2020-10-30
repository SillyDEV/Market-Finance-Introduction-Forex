import config
from other.colors import bcolors as bcolors
from indicators.BollingerBand import bollingerIndicator
from indicators.RSI import rsiIndicator
from pyti.exponential_moving_average import exponential_moving_average as ema


def rangeDetector():
    counter = 3
    highest = 0
    lowest = 2
    while counter != 0:
        if config.backdata["bidclose"][len(config.backdata) - counter] < lowest:
            lowest = config.backdata["bidclose"][len(config.backdata) - counter]
        if config.backdata["bidopen"][len(config.backdata) - counter] < lowest:
            lowest = config.backdata["bidopen"][len(config.backdata) - counter]
        if config.backdata["bidopen"][len(config.backdata) - counter] > highest:
            highest = config.backdata["bidopen"][len(config.backdata) - counter]
        if config.backdata["bidclose"][len(config.backdata) -counter] > highest:
            highest = config.backdata["bidclose"][len(config.backdata) - counter]
        counter = counter - 1

    delta = highest - lowest
    if delta >= config.rangeDelta:
        mainTrend()
    else:
        config.contextTrend = 0
        config.signalLatency = 10


def SignalFinder():
    bb = bollingerIndicator(config.backdata)
    rsi = rsiIndicator(config.backdata)

    total = bb + rsi
    if total == 2:
        config.contextSignal = 2
        config.signalLatency = 0
    elif total == -2:
        config.contextSignal = -2
        config.signalLatency = 0
    else:
        config.contextSignal = 0
        config.signalLatency = config.signalLatency + 1

def mainTrend():
    if config.signalLatency < 3:
        config.contextTrend = config.contextSignal
        config.signalLatency = config.signalLatency + 1
    if config.signalLatency >= 3:
        SignalFinder()
        SEma = ema(config.backdata["bidclose"], 4)
        FEma = ema(config.backdata["bidclose"], 2)
        if FEma[len(FEma) - 1] > SEma[len(SEma) - 1]:
            config.contextTrend = 1
        else:
            config.contextTrend = -1

