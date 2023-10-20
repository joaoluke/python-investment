import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta


def get_data_asset(symbol, timeframe):
    bars = mt5.copy_rates_from_pos(symbol, timeframe, 0, 60000)
    df = pd.DataFrame(bars)[['time', 'open', 'close', 'low', 'high']]
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df
