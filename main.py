from connect_to_mt5 import connect_to_mt5, mt5
from languages.en import get_financial_information_en, get_user_input_en, get_periods_en
from languages.pt import get_financial_information_ptbr, get_user_input_ptbr, get_periods_ptbr
from get_data_asset import get_data_asset
from strategy.crossing_averages import finding_crossovers
from utils.timeframe import convertTimeFrame
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy import prompt

settings = {}


def get_user_input(language):
    if language == 'English':
        return get_user_input_en()
    elif language == 'Português':
        return get_user_input_ptbr()
    else:
        print("Language not supported.")
        return None, None, None


def get_financial_information(language):
    if language == 'English':
        return get_financial_information_en()
    elif language == 'Português':
        return get_financial_information_ptbr()


def get_periods(language):
    if language == 'English':
        return get_periods_en()
    elif language == 'Português':
        return get_periods_ptbr()


def main():
    print('-------------------------------------------------')
    print('Bem-vindo ao algoritmo de negociação de day-trade')
    print('Welcome to the day-trade trading algorithm       ')
    print('-------------------------------------------------')

    language = inquirer.select(
        message="Selecione seu idioma/Select your language:",
        choices=[
            "English",
            "Português",
        ],
        default=None,
    ).execute()

    login, password, server = get_user_input(language)
    if login is None:
        return

    settings["login"] = login
    settings["password"] = password
    settings["server"] = server

    connect_to_mt5(login, password, server, language)

    asset, timeframe = get_financial_information(language)
    settings["asset"] = asset
    settings["timeframe"] = convertTimeFrame(timeframe)

    data = get_data_asset(asset, timeframe)

    ssma_period, fsma_period = get_periods(language)
    finding_crossovers(data, ssma_period, fsma_period)

    print(data)


if __name__ == "__main__":
    main()
