from pyti.relative_strength_index import relative_strength_index as rsi
from other.colors import bcolors as bcolors
import config

# Relative Strength Index Settings
rsiLowLimit = 32
rsiHighLimit = 68
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
        result = 1
    elif RSI[len(RSI) - 1] > rsiHighLimit:
        result = -1
    else:
        result = 0
    return result