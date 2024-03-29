from connect_to_mt5 import connect_to_mt5

from languages.en import get_financial_information_en, get_user_input_en, get_periods_en, get_account_information_en, show_result_en
from languages.pt import get_financial_information_ptbr, get_user_input_ptbr, get_periods_ptbr, get_account_information_ptbr, show_result_ptbr
from get_data_asset import get_data_asset
from probability_calculation import weighted_probability
from strategy.crossing_averages import finding_crossovers
from utils.timeframe import convertTimeFrame
from InquirerPy import inquirer
from backtest.crossover_strategy import Strategy
from analyze_data import visualize_dashboard

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


def get_account_information(language):
    if language == 'English':
        return get_account_information_en()
    elif language == 'Português':
        return get_account_information_ptbr()


def show_result(language, probability):
    if language == 'English':
        return show_result_en(probability)
    elif language == 'Português':
        return show_result_ptbr(probability)


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
    df_cross = finding_crossovers(data, ssma_period, fsma_period)
    visualize_dashboard(df_cross)
    balance, contract = get_account_information(language)

    sma_crossover_strategy = Strategy(df_cross, balance, contract)
    result = sma_crossover_strategy.run()
    print('result', result)
    results = [1 if x > 0 else 0 for x in result['profit']][::-1]
    probability = weighted_probability(results)

    show_result(language, probability)


if __name__ == "__main__":
    main()
