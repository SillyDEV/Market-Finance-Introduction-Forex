import datetime as dt
import config
import update.buyAndSell as bas
from other.colors import bcolors as bcolors
from strategies.custom import CustomStrategy
from strategies.crossEMA import modeSelector

def Update():
    if (config.mode == 'live'):
        print(bcolors.HEADER +"================================================>"+ bcolors.ENDC)
        print(bcolors.OKGREEN +str(dt.datetime.now()) + " " + config.period + " Bar Closed - Running Update Function..."+ bcolors.ENDC)
        print(bcolors.OKBLUE + "Close Price: " + str(config.pricedata['bidclose'][len(config.pricedata) - 1]) + bcolors.ENDC)
    if config.customStrategy == "c":
        CustomStrategy()
    if config.customStrategy == "p":
        modeSelector()






