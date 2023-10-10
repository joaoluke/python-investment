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
    timeframe = input("Agora precisamos do tempo grafico (Exemplo 5m para 5 minutos ou 1h para 1 hora): ")

    return asset, timeframe