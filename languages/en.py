def get_user_input_en():
    print("Welcome to our trading algorithm!")
    login = input("Enter your MetaTrader login: ")
    password = input("Enter your MetaTrader password: ")
    server = input("Enter the MetaTrader server: ")

    return int(login), password, server

def get_financial_information_en():
    print("Now we will need the asset information.")
    asset = input("Enter the asset you want (Example: USDJPY): ")
    timeframe = input("Now we need the graphical time (Example 5m for 5 minutes or 1h for 1 hour): ")

    return asset, timeframe