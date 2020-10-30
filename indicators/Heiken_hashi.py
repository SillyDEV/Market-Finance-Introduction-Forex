import config
import pandas as pd

def Heiken_hashi():
    df = config.pricedata.iloc[len(config.pricedata) - 50:]

    heikin_ashi_df = pd.DataFrame(index=df.index.values, columns=['bidopen', 'bidclose', "bidhigh", "bidlow", "color"])

    heikin_ashi_df['bidclose'] = (df['bidopen'] + df['bidhigh'] + df['bidlow'] + df['bidclose']) / 4

    for i in range(len(df)):
        if i == 0:
            heikin_ashi_df.iat[0, 0] = df['bidopen'].iloc[0]
        else:
            heikin_ashi_df.iat[i, 0] = (heikin_ashi_df.iat[i - 1, 0] + heikin_ashi_df.iat[i - 1, 1]) / 2

    for i in range(len(df)):
        if heikin_ashi_df.iat[i, 1] - heikin_ashi_df.iat[i, 0] > 0:
            heikin_ashi_df.iat[i, 4] = "green"
        else:
            heikin_ashi_df.iat[i, 4] = "red"

    heikin_ashi_df['bidhigh'] = heikin_ashi_df.loc[:, ['bidopen', 'bidclose']].join(df['bidhigh']).max(axis=1)
    heikin_ashi_df['bidlow'] = heikin_ashi_df.loc[:, ['bidopen', 'bidclose']].join(df['bidlow']).min(axis=1)
    config.heikenHashi = heikin_ashi_df
