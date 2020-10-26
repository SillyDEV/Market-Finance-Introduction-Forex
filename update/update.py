import datetime as dt
import config
import update.buyAndSell as bas
from other.colors import bcolors as bcolors
from indicators.BollingerBand import bollingerIndicator
from indicators.RSI import rsiIndicator
from indicators.EMA_fastslow import emaIndicator
from indicators.Stochastic import stochasticIndicator


def Update():
    if (config.mode == 'live'):
        print(bcolors.HEADER +"================================================>"+ bcolors.ENDC)
        print(bcolors.OKGREEN +str(dt.datetime.now()) + " " + config.period + " Bar Closed - Running Update Function..."+ bcolors.ENDC)
        print(bcolors.OKBLUE + "Close Price: " + str(config.pricedata['bidclose'][len(config.pricedata) - 1]) + bcolors.ENDC)


def CustomStrategy():
    entercounter = 0
    entersignal = 0
    closeCounter = 0
    closeSignal = 0
    # Calculate Indicators
    if config.enterBollinger:
        bb = bollingerIndicator(config.pricedata)
        entercounter = entercounter + 1
        entersignal = entersignal + bb
        closeCounter = closeCounter + 1
        closeSignal = closeSignal + bb
    if config.enterRsi:
        rsi = rsiIndicator(config.pricedata)
        entercounter = entercounter + 1
        entersignal = entersignal + rsi
        closeCounter = closeCounter + 1
        closeSignal = closeSignal + rsi
    if config.enterEma:
        ema = emaIndicator(config.pricedata)
        entercounter = entercounter + 1
        entersignal = entersignal + ema
        closeCounter = closeCounter + 1
        closeSignal = closeSignal + ema
    if config.enterStock:
        stoch = stochasticIndicator(config.pricedata)
        entercounter = entercounter + 1
        entersignal = entersignal + stoch
        closeCounter = closeCounter + 1
        closeSignal = closeSignal + stoch

    if bas.countOpenTrades("B") == 0 and bas.countOpenTrades("S") == 0:
        if entersignal == entercounter or entersignal * -1 == entercounter:
            if entersignal > 0:
                bas.enter("B")
            if entersignal < 0:
                bas.enter("S")

    if bas.countOpenTrades("B") > 0 or bas.countOpenTrades("S") > 0:
        if closeSignal == closeCounter or closeSignal * -1 == closeCounter:
            if entersignal > 0:
                bas.exit("S")
            if entersignal < 0:
                bas.exit("B")
