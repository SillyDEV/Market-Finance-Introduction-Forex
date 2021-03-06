from pyti.exponential_moving_average import exponential_moving_average as ema
from other.colors import bcolors as bcolors
import config

# Ema Settings
FastEma = 8
SlowEma = 21


def emaIndicator(data):
    result = 0

    SEma = ema(data["bidclose"], SlowEma)
    FEma = ema(data["bidclose"], FastEma)

    if config.mode == 'live' and config.print == "y":
        print(bcolors.HEADER + "============Exponential Strengh Index===============>" + bcolors.ENDC)
        print(bcolors.OKBLUE + "FastEMA: " + str(FEma[len(FEma) - 1]) + bcolors.ENDC)
        print(bcolors.OKBLUE + "SlowEMA: " + str(SEma[len(SEma) - 1]) + bcolors.ENDC)
    if FEma[len(FEma) - 1] > SEma[len(SEma) - 1]:
        result = 1
    else:
        result = -1
    return result
