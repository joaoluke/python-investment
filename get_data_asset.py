import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta


def get_data_asset(symbol, timeframe):
    current_day = datetime.now().date()
    one_year_before = current_day - timedelta(days=340)

    bars = mt5.copy_rates_range(
        symbol, timeframe, current_day,  one_year_before)
    df = pd.DataFrame(bars)[['time', 'open', 'close', 'low', 'high']]
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df
