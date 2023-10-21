import MetaTrader5 as mt5
import pandas as pd
import numpy as np


def get_finantial_information(df, ssma_period, fsma_period):
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['slow_sma'] = df['close'].rolling(ssma_period).mean()
    df['fast_sma'] = df['close'].rolling(fsma_period).mean()

    return df.dropna(inplace=True)


def finding_crossovers(df, ssma_period, fsma_period):
    df = get_finantial_information(df, ssma_period, fsma_period)

    df['prev_fast_sma'] = df['fast_sma'].shift(1)

    def find_crossovers(slow_sma, fast_sma, prev_fast_sma):
        if slow_sma < fast_sma and prev_fast_sma < slow_sma:
            return 'bull'
        elif slow_sma > fast_sma and prev_fast_sma > slow_sma:
            return 'bear'
        else:
            return None

    df['crossover'] = np.vectorize(find_crossovers)(
        df['slow_sma'], df['fast_sma'], df['prev_fast_sma'])

    signal = df[df['crossover'] == 'bull'].copy()
    return signal
