from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from connect_to_mt5 import mt5


def get_user_input_ptbr():
    print("Bem-vindo ao nosso algoritmo de negociação!")
    print("Precisamos fazer o login no MetaTrade 5")
    login = input("Digite seu login do MetaTrader: ")
    password = input("Digite sua senha do MetaTrader: ")
    server = input("Digite o servidor do MetaTrader: ")

    return int(login), password, server


def get_financial_information_ptbr():
    print("Agora vamos precisar das informações do ativo.")
    asset = input("Digite o ativo que voce deseja (Exemplo: USDJPY): ")
    timeframe = inquirer.select(
        message="Selecione o tempo do gráfico",
        choices=[
            Choice(mt5.TIMEFRAME_M1, name="1 minuto"),
            Choice(mt5.TIMEFRAME_M5, name="5 minutos"),
            Choice(mt5.TIMEFRAME_M15, name="15 minutos"),
            Choice(mt5.TIMEFRAME_M30, name="30 minutos"),
            Choice(mt5.TIMEFRAME_H1, name="1 hora"),
            Choice(mt5.TIMEFRAME_H2, name="2 horas"),
            Choice(mt5.TIMEFRAME_H4, name="4 horas"),
        ],
        default=None,
    ).execute()

    return asset, timeframe
