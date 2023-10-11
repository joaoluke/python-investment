from connect_to_mt5 import connect_to_mt5
from languages.en import get_financial_information_en, get_user_input_en
from languages.pt import get_financial_information_ptbr, get_user_input_ptbr

settings = {}


def get_user_input(language):
    if language in ['1', 'en']:
        return get_user_input_en()
    elif language in ['2', 'pt']:
        return get_user_input_ptbr()
    else:
        print("Language not supported.")
        return None, None, None


def get_financial_information(language):
    if language in ['1', 'en']:
        return get_financial_information_en()
    elif language in ['2', 'pt']:
        return get_financial_information_ptbr()


def main():
    print('''
        ----------------------------------------------------------------
        Please choose your language (1 for English or 2 for Portuguese): 
        Por favor escolha seu idioma (1 para ingles ou 2 pra portugues):
        ----------------------------------------------------------------
    ''')

    language = input()

    login, password, server = get_user_input(language)
    if login is None:
        return

    settings["login"] = login
    settings["password"] = password
    settings["server"] = server

    connect_to_mt5(login, password, server, language)

    asset, timeframe = get_financial_information(language)
    settings["asset"] = asset
    settings["timeframe"] = timeframe

    get_data_asset()

if __name__ == "__main__":
    main()

    
