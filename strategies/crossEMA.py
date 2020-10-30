import config
import update.buyAndSell as bas
from indicators.EMA_fastslow import emaIndicator
from indicators.BollingerBand import bollingerIndicator
from SignalStrenghCalculation.crossEMAcontext import rangeDetector
from pyti.exponential_moving_average import exponential_moving_average as ema

def modeSelector():
    config.contextSignal = config.inRange
    rangeDetector(config.backdata)
    if config.inRange != config.contextSignal:
        bas.exit("S")
        bas.exit("B")
        config.lastChange = 0

    if config.inRange is True:
        print("inBoll")
        bollinger()
    elif config.inRange is False:
        print("inCross")
        crossEMA()

def bollinger():
    bb = bollingerIndicator(config.pricedata)
    if bb == 1 and bas.countOpenTrades("B") == 0:
        config.traillingStop = None
        print("inBollBuy")
        bas.enter("B")
    elif bb == -1 and bas.countOpenTrades("S") == 0:
        config.traillingStop = None
        print("inBollSell")
        bas.enter("S")
    exitBollinger()

def exitBollinger():
    SEMA = ema(config.pricedata["bidclose"], 55)
    if bas.countOpenTrades("B"):
        if config.pricedata["bidclose"][len(config.pricedata) - 1] > SEMA[len(SEMA) - 1]:
            print("inBollEXITBUY")
            bas.exit("B")
    if bas.countOpenTrades("S"):
        if config.pricedata["bidclose"][len(config.pricedata) - 1] < SEMA[len(SEMA) - 1]:
            print("inBollEXITSELL")
            bas.exit("S")
    exitTrade()

def crossEMA():
    signal = 0
    value = emaIndicator(config.pricedata)
    if value != config.lastChange:
        signal = value
        config.lastChange = value
    print(str(value))
    if signal == 1:
        if bas.countOpenTrades("S") > 0:
            bas.exit("S")
        config.openPrice = config.pricedata["bidclose"][len(config.pricedata) - 1]
        config.traillingStop = None
        print("inCROSSEXITBUY")
        bas.enter("B")
    # If Fast SMA crosses under Slow SMA, Open Sell Trade
    if signal == -1:
        if bas.countOpenTrades("B") > 0:
            bas.exit("B")
        config.traillingStop = None
        config.openPrice = config.pricedata["bidclose"][len(config.pricedata) - 1]
        print("inCROSSEXITSELL")
        bas.enter("S")
    print(config.openPrice)
    exitTrade()

def exitTrade():
    traillingStop()
    if bas.countOpenTrades("B") > 0:
        if config.traillingStop is not None:
            if config.pricedata["bidclose"][len(config.pricedata) - 1] < config.traillingStop:
                bas.exit("B")
                print("exit3")
    if bas.countOpenTrades("S") > 0:
        if config.traillingStop is not None:
            if config.pricedata["bidclose"][len(config.pricedata) - 1] > config.traillingStop:
                print("exit5")
                bas.exit("S")

def traillingStop():
    if bas.countOpenTrades("B") > 0:
        if config.pricedata["bidclose"][len(config.pricedata) - 1] > config.openPrice + config.marge:
            if config.traillingStop is None:
                config.traillingStop = config.pricedata["bidclose"][len(config.pricedata) - 1] - config.marge
            elif config.traillingStop < config.pricedata["bidclose"][len(config.pricedata) - 1] + config.marge:
                config.traillingStop = config.pricedata["bidclose"][len(config.pricedata) - 1] - config.marge
                print("Buy trailling stop :" + str(config.traillingStop))
    if bas.countOpenTrades("S") > 0:
        if config.pricedata["bidclose"][len(config.pricedata) - 1] < config.openPrice - config.marge:
            if config.traillingStop is None:
                config.traillingStop = config.pricedata["bidclose"][len(config.pricedata) - 1] + config.marge
            elif config.traillingStop > config.pricedata["bidclose"][len(config.pricedata) - 1] - config.marge:
                config.traillingStop = config.pricedata["bidclose"][len(config.pricedata) - 1] + config.marge
                print("Sell trailling stop :" + str(config.traillingStop))