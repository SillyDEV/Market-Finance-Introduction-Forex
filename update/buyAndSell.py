import config
from other.colors import bcolors as bcolors


def enter(BuySell):
    if config.mode == 'live':
        direction = True
        if BuySell == "S":
            direction = False
        try:
            config.con.open_trade(symbol=config.currency, is_buy=direction, amount=config.amount,
                                  time_in_force='GTC', order_type='AtMarket', is_in_pips=True,
                                  limit=config.limit, stop=config.stop, trailing_step=10)
        except:
            print("	  Error Opening Trade.")
        else:
            print("	  Trade Opened Successfully.")
    else:
        direction = True
        if BuySell == "S":
            direction = False
        config.MyPosition = {"symbol": config.currency, "is_buy": BuySell,
                             "price": config.pricedata['bidclose'][len(config.pricedata['bidclose']) - 1]}
        print(bcolors.OKGREEN + "Trade Opened Successfully." + bcolors.ENDC)
        print("\t", end='')
        print(bcolors.OKGREEN + str(config.MyPosition) + bcolors.ENDC)



def exit(BuySell=None):
    if config.mode == 'live':
        openpositions = config.con.get_open_positions(kind='list')
        isbuy = True
        if BuySell == "S":
            isbuy = False
        for position in openpositions:
            if position['currency'] == config.currency:
                if BuySell is None or position['isBuy'] == isbuy:
                    print("	  Closing tradeID: " + position['tradeId'])
                    try:
                        closetrade = config.con.close_trade(trade_id=position['tradeId'], amount=position['amountK'])
                    except:
                        print("	  Error Closing Trade.")
                    else:
                        print("	  Trade Closed Successfully.")
    else:
        if config.MyPosition['is_buy'] == BuySell:
            print(bcolors.OKGREEN + "Trade Closed Successfully.")
            price = config.pricedata['bidclose'][len(config.pricedata['bidclose']) - 1]
            if BuySell == "S":
                config.PipsProfit += (config.MyPosition['price'] - price)
                print(bcolors.OKGREEN + "\tProfit: " + str(
                    int((config.MyPosition['price'] - price) * 100000)) + ' Pips' + bcolors.ENDC)
                if config.MyPosition['price'] - price >= 0:
                    config.TradeWin += 1
                else:
                    config.TradeLoss += 1
            else:
                config.PipsProfit += (price - config.MyPosition['price'])
                print(bcolors.OKGREEN + "\tProfit: " + str(
                    int((price - config.MyPosition['price']) * 100000)) + ' Pips' + bcolors.ENDC)
                if price - config.MyPosition['price'] >= 0:
                    config.TradeWin += 1
                else:
                    config.TradeLoss += 1
            print(bcolors.OKBLUE + '\nTotal Pips profit : ' + str(
                int(round(config.PipsProfit, 5) * 100000)) + bcolors.ENDC)
            print(bcolors.OKBLUE + 'Win trades : ' + str(config.TradeWin) + bcolors.ENDC)
            print(bcolors.OKBLUE + 'trades Loss : ' + str(config.TradeLoss) + '\n' + bcolors.ENDC)
            config.MyPosition = None


def countOpenTrades(BuySell=None):
    if config.mode == 'live':
        openpositions = config.con.get_open_positions(kind='list')
        isbuy = True
        counter = 0
        if BuySell == "S":
            isbuy = False
        for position in openpositions:
            if position['currency'] == config.currency:
                if BuySell is None or position['isBuy'] == isbuy:
                    counter += 1
        return counter
    else:
        if config.MyPosition == None:
            return 0
        return 1
