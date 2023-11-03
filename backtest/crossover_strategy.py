import pandas as pd


class Position:
    def __init__(self, open_datetime, open_price, order_type, volume, sl, tp):
        self.open_datetime = open_datetime
        self.open_price = open_price
        self.order_type = order_type
        self.volume = volume
        self.sl = sl
        self.tp = tp
        self.close_datetime = None
        self.close_price = None
        self.profit = None
        self.status = 'open'

    def close_position(self, close_datetime, close_price):
        self.close_datetime = close_datetime
        self.close_price = close_price
        self.profit = (self.close_price - self.open_price) * self.volume if self.order_type == 'buy' \
            else (self.open_price - self.close_price) * self.volume
        self.status = 'closed'

    def _asdict(self):
        return {
            'open_datetime': self.open_datetime,
            'open_price': self.open_price,
            'order_type': self.order_type,
            'volume': self.volume,
            'sl': self.sl,
            'tp': self.tp,
            'close_datetime': self.close_datetime,
            'close_price': self.close_price,
            'profit': self.profit,
            'status': self.status,
        }


class Strategy:
    def __init__(self, df, starting_balance, volume):
        self.starting_balance = starting_balance
        self.volume = volume
        self.positions = []
        self.data = df

    def get_positions_df(self):
        df = pd.DataFrame([position._asdict() for position in self.positions])
        df['pnl'] = df['profit'].cumsum() + self.starting_balance
        return df

    def add_position(self, position):
        self.positions.append(position)

        return True

    # logic
    def run(self):
        for i, data in self.data.iterrows():

            if data.crossover == 'bear':
                for position in self.positions:
                    if position.status == 'open':
                        position.close_position(data.time, data.close)

            if data.crossover == 'bull':
                self.add_position(
                    Position(data.time, data.close, 'buy', self.volume, 0, 0))

        return self.get_positions_df()
