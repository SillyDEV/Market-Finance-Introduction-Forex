from pyti.stochastic import percent_d as pd
from other.colors import bcolors as bcolors
import config

# Stochastic
StockPeriods = 5
StockBuy = 0.20
StockSell = 0.80


def stochasticIndicator(data):
    result = 0
    StockD = pd(data["bidclose"], StockPeriods)

    if config.mode == 'live' and config.print == "y":
        print(bcolors.HEADER + "=====================Stochastic=======================>")
        print(bcolors.OKBLUE + "Stockastic: " + str(StockD[len(StockD) - 1]))
    if StockD[len(StockD) - 1] < 0.20:
        if config.mode == 'live':
            print(bcolors.OKGREEN + "Buy Signal!" + bcolors.ENDC)
        result = 1
    elif StockD[len(StockD) - 1] > 0.80:
        if config.mode == 'live':
            print(bcolors.WARNING + "Sell Signal!" + bcolors.ENDC)
        result = -1
    else:
        if config.mode == 'live':
            print(bcolors.BOLD + "No Signal!" + bcolors.ENDC)
        result = 0
    return result
