import MetaTrader5 as mt5

def convertTimeFrame(timeframe):  
    match timeframe:
        case "5m":
            return mt5.TIMEFRAME_M5
        case "15m":
            return mt5.TIMEFRAME_M15
        case "30m":
            return mt5.TIMEFRAME_M30
        case "1h":
            return mt5.TIMEFRAME_H1
        case "2h":
            return mt5.TIMEFRAME_H2
    return False