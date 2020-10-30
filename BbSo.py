import fxcmpy
import config
import update.liveLoop as live
import update.backTestLoop as test
from other.colors import bcolors as bcolors
from ignition.ignition import init


def Prepare():
    init()
    if config.mode == "L" or config.mode == "l":
        config.con = fxcmpy.fxcmpy(access_token=config.token, log_level="error", log_file=None)
        config.mode = "live"
        print(bcolors.OKGREEN + "Requesting Initial Price Data..." + bcolors.ENDC)
        config.pricedata = config.con.get_candles(config.currency, period=config.period, number=config.numberofcandles)
        config.backdata = config.con.get_candles(config.currency, period=config.backPeriod, number=config.numberofcandles)
        print(bcolors.OKGREEN + "Initial Price Data Received..." + bcolors.ENDC)
    elif config.mode == "B" or config.mode == "b":
        config.mode = "test"
        print(bcolors.OKGREEN + "BACKTEST MODE" + bcolors.ENDC)
    else:
        print("Wrong input")
        exit(0)


def main():
    Prepare()
    if config.mode == "live":
        live.liveLoop()
    elif config.mode == "test":
        test.testLoop()


if __name__ == '__main__':
    main()
