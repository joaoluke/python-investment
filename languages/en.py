from connect_to_mt5 import mt5
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.validator import EmptyInputValidator


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


def get_periods_en():
    return


def get_account_information_en():
    print('Now lets simulate the strategy in the past tense')
    balance = inquirer.number(
        message="What is your margin?",
        min_allowed=1,
        validate=EmptyInputValidator(),
    ).execute()
    contract = inquirer.number(
        message="How many contracts do you want to simulate?",
        min_allowed=1,
        validate=EmptyInputValidator(),
    ).execute()

    return int(balance), int(contract)


def show_result_ptbr(probability):
    print(f'The probability of success is: {round(probability, 2)}%')
