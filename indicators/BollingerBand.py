from pyti.bollinger_bands import lower_bollinger_band as lb
from pyti.bollinger_bands import middle_bollinger_band as mb
from pyti.bollinger_bands import upper_bollinger_band as ub
from other.colors import bcolors as bcolors
import config

# BOLLINGER BANDS SETTINGS
bollingerPeriod = 20
StandardDev = 2


def bollingerIndicator(data):
    result = 0

    UpperBand = ub(data["bidclose"], bollingerPeriod, StandardDev)
    MiddleBand = mb(data["bidclose"], bollingerPeriod, StandardDev)
    LowerBand = lb(data["bidclose"], bollingerPeriod, StandardDev)

    if config.mode == 'live' and config.print == "y":
        print(bcolors.HEADER + "================BOLLINGER BAND==============>" + bcolors.ENDC)
        print(bcolors.OKBLUE + "UpperBand: " + str(UpperBand[len(UpperBand) - 1]) + bcolors.ENDC)
        print(bcolors.OKBLUE + "MiddleBand: " + str(MiddleBand[len(MiddleBand) - 1]) + bcolors.ENDC)
        print(bcolors.OKBLUE + "LowerBand: " + str(LowerBand[len(LowerBand) - 1]) + bcolors.ENDC)
    if data["bidclose"][len(data) - 1] < LowerBand[len(LowerBand) - 1]:
        if config.mode == 'live':
            print(bcolors.OKGREEN + "Buy Signal!" + bcolors.ENDC)
        result = 1
    elif data["bidclose"][len(data) - 1] > UpperBand[len(UpperBand) - 1]:
        if config.mode == 'live':
            print(bcolors.WARNING + "Sell Signal!" + bcolors.ENDC)
        result = -1
    else:
        if config.mode == 'live':
            print(bcolors.OKBLUE + bcolors.BOLD + "No break trough bollinger bands!" + bcolors.ENDC)
        result = 0
    return result
