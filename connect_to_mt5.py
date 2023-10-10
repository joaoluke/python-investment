import MetaTrader5 as mt5

def connect_to_mt5(login, password, server, language):
    conection = mt5.initialize(login=login, server=server, password=password)

    if language == '1':
        if not conection:
            print("Houve o seguinte erro ao se conectar: ", mt5.last_error())
            quit()

        print(f'''
            -------------------------------------------------------
            ✹ Sucesso ao se conectar, aqui estão algumas informações:
            -------------------------------------------------------
            {mt5.terminal_info()}
            -------------------------------------------------------
            Versão do MetaTrader:
            {mt5.version()}
        ''')
    
    if language == '2':
        if not conection:
            print("There was the following error when connecting: ", mt5.last_error())
            quit()

        print(f'''
            -------------------------------------------------------
            ✹ Success connecting, here is some information:
            -------------------------------------------------------
            {mt5.terminal_info()}
            -------------------------------------------------------
            MetaTrader Version:
            {mt5.version()}
        ''')