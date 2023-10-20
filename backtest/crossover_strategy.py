import pandas as pd
from position import Position


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
