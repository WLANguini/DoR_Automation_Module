import pandas as pd
import numpy as np
import yfinance as yf

def data_cleaning(dataframe):
    dataframe = dataframe.drop(columns= ["Volume", "Dividends", "Stock Splits"])
    dataframe = dataframe.sort_values(by="Date", ascending=False)
    
    return dataframe

