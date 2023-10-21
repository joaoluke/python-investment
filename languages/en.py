from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from connect_to_mt5 import mt5


def get_user_input_en():
    print("Welcome to our trading algorithm!")
    login = input("Enter your MetaTrader login: ")
    password = input("Enter your MetaTrader password: ")
    server = input("Enter the MetaTrader server: ")

    return int(login), password, server


def get_financial_information_en():
    print("Now we will need the asset information.")
    asset = input("Enter the asset you want (Example: USDJPY): ")
    timeframe = inquirer.select(
        message="Select chart time",
        choices=[
            Choice(mt5.TIMEFRAME_M1, name="1 minute"),
            Choice(mt5.TIMEFRAME_M5, name="5 minutes"),
            Choice(mt5.TIMEFRAME_M15, name="15 minutes"),
            Choice(mt5.TIMEFRAME_M30, name="30 minutes"),
            Choice(mt5.TIMEFRAME_H1, name="1 hour"),
            Choice(mt5.TIMEFRAME_H2, name="2 hours"),
            Choice(mt5.TIMEFRAME_H4, name="4 hours"),
        ],
        default=None,
    ).execute()

    return asset, timeframe
