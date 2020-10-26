from pyti.relative_strength_index import relative_strength_index as rsi
from other.colors import bcolors as bcolors
import config

# Relative Strength Index Settings
rsiLowLimit = 31
rsiHighLimit = 69
rsiBuyStop = 60
rsiSellStop = 40
rsiPeriod = 14

def rsiIndicator(data):
    result = 0
    RSI = rsi(data["bidclose"], rsiPeriod)

    if config.mode == 'live' and config.print == "y":
        print(bcolors.HEADER + "=====================RSI============================>")
        print(bcolors.OKBLUE + "RSI: " + str(RSI[len(RSI) - 1]))
    if RSI[len(RSI) - 1] < rsiLowLimit:
        if config.mode == 'live':
            print(bcolors.OKGREEN + "Buy Signal!" + bcolors.ENDC)
        result = 1
    elif RSI[len(RSI) - 1] > rsiHighLimit:
        if config.mode == 'live':
            print(bcolors.WARNING + "Sell Signal!" + bcolors.ENDC)
        result = -1
    else:
        if config.mode == 'live':
            print(bcolors.BOLD + "No Signal!" + bcolors.ENDC)
        result = 0
    return result