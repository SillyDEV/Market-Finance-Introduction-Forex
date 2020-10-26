import config
from other.colors import bcolors as bcolors
import backtesting.ParseFile as backParsing
import os

currency_list = ['AUD/CAD', 'AUD/CHF', 'AUD/JPY', 'AUD/NZD', 'AUD/USD', 'CAD/CHF', 'CAD/JPY', 'CHF/JPY', 'EUR/AUD',
                 'EUR/CAD',
                 'EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'EUR/NOK', 'EUR/NZD', 'EUR/SEK', 'EUR/TRY', 'EUR/USD', 'GBP/AUD',
                 'GBP/CAD',
                 'GBP/CHF', 'GBP/JPY', 'GBP/NZD', 'GBP/USD', 'NZD/CAD', 'NZD/CHF', 'NZD/JPY', 'NZD/USD', 'TRY/JPY',
                 'USD/CAD',
                 'USD/CNH', 'USD/HKD', 'USD/JPY', 'USD/MXN', 'USD/NOK', 'USD/SEK', 'USD/TRY', 'USD/ZAR', 'XAG/USD',
                 'XAU/USD',
                 'ZAR/JPY', 'USD/ILS', 'BTC/USD', 'BCH/USD', 'ETH/USD', 'LTC/USD', 'XRP/USD', 'EOS/USD', 'XLM/USD',
                 'USD/CHF']

periods_list = ['m1', 'm5', 'm15', 'm30', 'H1', 'H2', 'H3', 'H4', 'H6', 'H8', 'D1', 'W1', 'M1']


def init():
    modeSelector()
    if config.customStrategy == "c":
        print(bcolors.OKGREEN + "PREBUILD STRATEGY SELECTED" + bcolors.ENDC)
        openConditionSelector()
        closePositionSelector()
    if config.customStrategy == "p":
        print(bcolors.OKGREEN + "PREBUILD STRATEGY SELECTED not allready done!" + bcolors.ENDC)

def modeSelector():
    # MODE + CURRENCY + PERIOD CONFIGURATION
    while config.mode is None:
        config.mode = input(
            bcolors.OKBLUE + "Select your mode: [b]BackTest | [l]Live : " + bcolors.ENDC)
        if config.mode != 'b' and config.mode != 'l':
            print(bcolors.WARNING + "Invalid mode selected '" + str(config.mode) + "' not recognized" + bcolors.ENDC)
            config.mode = None
    while config.customStrategy is None:
        config.customStrategy = input(
            bcolors.OKBLUE + "Select your strategy: [c]Custom | [p]Prebuild : " + bcolors.ENDC)
        if config.customStrategy != 'c' and config.customStrategy != 'p':
            print(bcolors.WARNING + "Invalid strategy selected '" + str(config.mode) + "' not recognized" + bcolors.ENDC)
            config.customStrategy = None
    if config.mode == "l" or "L":
        while config.print is None:
            config.print = input(
                bcolors.OKBLUE + "Full print mode: [y] | [n]" + bcolors.ENDC)
            if config.print != 'y' and config.print != 'n':
                print(bcolors.WARNING + "Invalid mode selected '" + str(config.print) + "' not recognized" + bcolors.ENDC)
                config.print = None
    while config.currency is None:
        config.currency = input(
            bcolors.OKBLUE + "Type 'help' to get the currencies list. Enter your Symbol:" + bcolors.ENDC)
        if config.currency == 'help':
            print(bcolors.OKGREEN + 'All currencies supported :' + bcolors.ENDC)
            print(currency_list)
            config.currency = None
        if config.currency not in currency_list:
            print(bcolors.FAIL + "Invalid currency selected '" + str(config.currency) + "'\nType help to get the "
                                                                                        "currencies list" +
                  bcolors.ENDC)
            config.currency = None
    while config.period is None:
        config.period = input(bcolors.OKBLUE + "Enter your Period:" + bcolors.ENDC)
        if config.period not in periods_list:
            print(bcolors.FAIL + "Invalid period selected '" + str(config.period) + "'." + bcolors.ENDC)
            config.period = None
    validate_file = False
    if config.mode == "b":
        while not validate_file:
            config.back_file = input(bcolors.OKGREEN + "Type 'help' to have a link to download one\nEnter the path to "
                                                       "your file (.csv): " + bcolors.ENDC)
            if config.back_file == 'help':
                print(bcolors.OKGREEN + 'https://eaforexacademy.com/software/forex-historical-data/' + bcolors.ENDC)
                config.back_file = None
            else:
                if os.path.isfile('./' + config.back_file) is False or '.csv' not in config.back_file:
                    print(bcolors.FAIL + 'File does not exists or not a .csv file' + bcolors.ENDC)
                    config.back_file = None
                else:
                    print(bcolors.OKGREEN + "Parsing your file..." + bcolors.ENDC)
                    if backParsing.check_file():
                        print(bcolors.OKGREEN + "File Sucessfully read !" + bcolors.ENDC)
                        validate_file = True
                    else:
                        print(bcolors.FAIL + 'Error while parsing the file' + bcolors.ENDC)


def openConditionSelector():
    # OPENING POSITION
    print(bcolors.OKGREEN + "\nOPENING POSITION CONFIGURATION:" + bcolors.ENDC)
    res = None
    while res != 'y' and res != 'n':
        res = input(bcolors.OKBLUE + "Do you want to use Bollinger Signal as openSignal: [y] | [n]" + bcolors.ENDC)
    if res == "y":
        config.enterBollinger = True
        print(bcolors.OKGREEN + "Bollinger Activated" + bcolors.ENDC)
    else:
        config.enterBollinger = False
    res = None
    while res != 'y' and res != 'n':
        res = input(bcolors.OKBLUE + "Do you want to use RSI Signal as openSignal: [y] | [n]" + bcolors.ENDC)
    if res == "y":
        config.enterRsi = True
        print(bcolors.OKGREEN + "RSI Activated" + bcolors.ENDC)
    else:
        config.enterRsi = False
    res = None
    while res != 'y' and res != 'n':
        res = input(bcolors.OKBLUE + "Do you want to use Ema Signal as openSignal: [y] | [n]" + bcolors.ENDC)
    if res == "y":
        config.enterEma = True
        print(bcolors.OKGREEN + "EMA Activated" + bcolors.ENDC)
    else:
        config.enterEma = False
    res = None
    while res != 'y' and res != 'n':
        res = input(bcolors.OKBLUE + "Do you want to use Stockastic Signal as openSignal: [y] | [n]" + bcolors.ENDC)
    if res == "y":
        config.enterStock = True
        print(bcolors.OKGREEN + "Stochastic Activated" + bcolors.ENDC)
    else:
        config.enterStock = False


def closePositionSelector():
    # CLOSING CONDITIONS

    print(bcolors.OKGREEN + "\nCLOSING POSITION CONFIGURATION:" + bcolors.ENDC)
    res = None
    while res != 'y' and res != 'n':
        res = input(bcolors.OKBLUE + "Do you want to use Bollinger Signal as CloseSignal: [y] | [n]" + bcolors.ENDC)
    if res == "y":
        config.closeBollinger = True
        print(bcolors.OKGREEN + "Bollinger Activated" + bcolors.ENDC)
    else:
        config.closeBollinger = False
    res = None
    while res != 'y' and res != 'n':
        res = input(bcolors.OKBLUE + "Do you want to use RSI Signal as CloseSignal: [y] | [n]" + bcolors.ENDC)
    if res == "y":
        config.closeRsi = True
        print(bcolors.OKGREEN + "RSI Activated" + bcolors.ENDC)
    else:
        config.closeRsi = False
    res = None
    while res != 'y' and res != 'n':
        res = input(bcolors.OKBLUE + "Do you want to use Ema Signal as CloseSignal: [y] | [n]" + bcolors.ENDC)
    if res == "y":
        config.closeEma = True
        print(bcolors.OKGREEN + "EMA Activated" + bcolors.ENDC)
    else:
        config.closeEma = False
    res = None
    while res != 'y' and res != 'n':
        res = input(bcolors.OKBLUE + "Do you want to use Stockastic Signal as CloseSignal: [y] | [n]" + bcolors.ENDC)
    if res == "y":
        config.closeStock = True
        print(bcolors.OKGREEN + "Stochastic Activated" + bcolors.ENDC)
    else:
        config.closeStock = False
