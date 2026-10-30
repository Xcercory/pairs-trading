import yfinance as yf
import pandas as pd
def fetch_pair_data(ticker1:str,ticker2:str,start_date:str,end_date:str)->pd.DataFrame:
    #Скачиваем исторические данные двух тикеров и возвращаем DataFrame с закрытием ticker1(Выбранная акция 1) и ticker2(Выбранная акция 2) где#
    data=yf.download([ticker1,ticker2],start=start_date,end=end_date)
    if data.empty:
        return pd.DataFrame()
    if isinstance(data.columns,pd.MultiIndex):
        df = data["Close"]
    else:
        df = data
    df = df[[ticker1,ticker2]].dropna()
    return df
