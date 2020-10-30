import datetime as dt
import config
from other.colors import bcolors as bcolors
from indicators.Heiken_hashi import Heiken_hashi as HA
from strategies.custom import CustomStrategy
import update.buyAndSell as bas

def rangeCondition():
    config.enterRsi = True
    config.closeRsi = True

def heikenAchiStrat():
    HA()
    rangeCondition()
    print(str(config.contextTrend))

    if bas.countOpenTrades("B") == 0 and bas.countOpenTrades("S") == 0:
        if config.contextTrend == 0:
            CustomStrategy()
        if config.contextTrend > 0:
            upTrendHA()
        if config.contextTrend < 0:
            downTrendHA()
    if bas.countOpenTrades("B") > 0 or bas.countOpenTrades("S") > 0:
        if config.contextTrend != 0:
            exitTrade()

def upTrendHA():
    print("Uptrend")
    if config.heikenHashi["color"][len(config.heikenHashi) - 1] == "green" and config.heikenHashi["color"][len(config.heikenHashi) - 2] == "green":
        print("Uptrend1")
        bas.enter("B")
        config.traillingStop = None
        config.openPrice = config.pricedata["bidclose"][len(config.pricedata) - 1]

def downTrendHA():
    print("DOWNtrend")
    if config.heikenHashi["color"][len(config.heikenHashi) - 1] == "red" and config.heikenHashi["color"][len(config.heikenHashi) - 2] == "red":
        print("downtrend1")
        config.traillingStop = None
        config.openPrice = config.pricedata["bidclose"][len(config.pricedata) - 1]
        bas.enter("S")

def exitTrade():
    traillingStop()
    if bas.countOpenTrades("B") > 0:
        if config.traillingStop is not None:
            if config.pricedata["bidclose"][len(config.pricedata) - 1] < config.traillingStop:
                bas.exit("B")
                print("exit3")
        if config.heikenHashi["color"][len(config.heikenHashi) - 1] == "red" and config.heikenHashi["color"][len(config.heikenHashi) - 2] == "red" and config.heikenHashi["color"][len(config.heikenHashi) - 3] == "red" and config.heikenHashi["color"][len(config.heikenHashi) - 4] == "red":
            bas.exit("B")
            print("exit4")
    if bas.countOpenTrades("S") > 0:
        if config.traillingStop is not None:
            if config.pricedata["bidclose"][len(config.pricedata) - 1] > config.traillingStop:
                print("exit5")
                bas.exit("S")
        if config.heikenHashi["color"][len(config.heikenHashi) - 1] == "green" and config.heikenHashi["color"][len(config.heikenHashi) - 2] == "green" and config.heikenHashi["color"][len(config.heikenHashi) - 3] == "green" and config.heikenHashi["color"][len(config.heikenHashi) - 4] == "green":
            print("exit6")
            bas.exit("S")

def traillingStop():
    if bas.countOpenTrades("B") > 0:
        print(str(config.traillingStop))
        if config.pricedata["bidclose"][len(config.pricedata) - 1] > config.openPrice + config.marge:
            config.traillingStop = config.heikenHashi["bidopen"][len(config.heikenHashi) - 2]
            print("Buy trailling stop :" + str(config.traillingStop))
            print("exit1")
    if bas.countOpenTrades("S") > 0:
        if config.pricedata["bidclose"][len(config.pricedata) - 1] < config.openPrice - config.marge:
            config.traillingStop = config.heikenHashi["bidclose"][len(config.heikenHashi) - 2]
            print("Sell trailling stop :" + str(config.traillingStop))