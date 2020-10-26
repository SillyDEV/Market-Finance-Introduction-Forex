import config
from other.colors import bcolors as bcolors

from update.update import Update


def testLoop():
    start_df = 0
    end_df = config.numberofcandles
    percentage = int((len(config.FullDataframe) - end_df) / 100)
    print(bcolors.HEADER + "RUNNING..." + bcolors.ENDC)
    while end_df < len(config.FullDataframe) + 1:
        if start_df % percentage == 0:
            print(bcolors.WARNING + str((start_df / percentage)) + '%' + ' of file done' + bcolors.ENDC)
        config.pricedata = config.FullDataframe.iloc[start_df:end_df]
        config.pricedata = config.pricedata.reset_index()
        config.pricedata = config.pricedata.set_index('date')
        end_df += 1
        start_df += 1
        Update()
    print(bcolors.HEADER + "DONE" + bcolors.ENDC)
    print(bcolors.OKBLUE + 'Pips profit : ' + str(int(round(config.PipsProfit, 4) * 100000)) + bcolors.ENDC)
    print(bcolors.OKGREEN + 'Win trades : ' + str(config.TradeWin) + bcolors.ENDC)
    print(bcolors.FAIL + 'trades Loss : ' + str(config.TradeLoss) + bcolors.ENDC)
