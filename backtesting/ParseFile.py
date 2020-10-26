import csv
import config
import pandas as pd

def check_file():
    with open('./' + config.back_file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    if len(data) > config.numberofcandles and len(data[0]) == 6:
        config.FullDataframe = pd.DataFrame(data, columns=['date', 'bidopen',  'bidhigh', 'bidlow', 'bidclose', 'tickqty'])
        config.FullDataframe['bidclose'] = config.FullDataframe['bidclose'].astype(float)
        config.FullDataframe['bidopen'] = config.FullDataframe['bidopen'].astype(float)
        config.FullDataframe['bidhigh'] = config.FullDataframe['bidhigh'].astype(float)
        config.FullDataframe['bidlow'] = config.FullDataframe['bidlow'].astype(float)
        config.FullDataframe = config.FullDataframe.set_index('date')
        return (True)
    else:
        return (False)