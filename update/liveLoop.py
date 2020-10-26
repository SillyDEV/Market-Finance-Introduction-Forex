import time
import datetime as dt
import config
from other.colors import bcolors as bcolors
from update.update import Update

def getLatestPriceData():

    # Normal operation will update config.pricedata on first attempt
    new_pricedata = config.con.get_candles(config.currency, period=config.period, number=config.numberofcandles)
    if new_pricedata.index.values[len(new_pricedata.index.values) - 1] != config.pricedata.index.values[
        len(config.pricedata.index.values) - 1]:
        config.pricedata = new_pricedata
        return True

    # If data is not available on first attempt, try up to 3 times to update config.pricedata
    counter = 0
    while new_pricedata.index.values[len(new_pricedata.index.values) - 1] == config.pricedata.index.values[
        len(config.pricedata.index.values) - 1] and counter < 3:
        print(bcolors.HEADER +"No updated prices found, trying again in 10 seconds..."+ bcolors.ENDC)
        counter += 1
        time.sleep(10)
        new_pricedata = config.con.get_candles(config.currency, period=config.period, number=config.numberofcandles)
    if new_pricedata.index.values[len(new_pricedata.index.values) - 1] != config.pricedata.index.values[
        len(config.pricedata.index.values) - 1]:
        config.pricedata = new_pricedata
        return True
    else:
        return False

def liveLoop():
    while True:
        currentTime = dt.datetime.now()
        if config.period == "m1" and currentTime.second == 0 and getLatestPriceData():
            Update()
        elif config.period == "m5" and currentTime.second == 0 and currentTime.minute % 5 == 0 and getLatestPriceData():
            Update()
            time.sleep(240)
        elif config.period == "m15" and currentTime.second == 0 and currentTime.minute % 15 == 0 and getLatestPriceData():
            Update()
            time.sleep(840)
        elif config.period == "m30" and currentTime.second == 0 and currentTime.minute % 30 == 0 and getLatestPriceData():
            Update()
            time.sleep(1740)
        elif currentTime.second == 0 and currentTime.minute == 0 and getLatestPriceData():
            Update()
            time.sleep(3540)
        time.sleep(1)