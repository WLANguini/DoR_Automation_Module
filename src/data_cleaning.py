import pandas as pd
import numpy as np
import yfinance as yf

def data_cleaning(dataframe):
    dataframe = dataframe.drop(columns= ["Volume", "Dividends", "Stock Splits"])
    dataframe = dataframe.sort_values(by="Date", ascending=False)
    
    return dataframe

def recleaning(df):
    cols = ["Open", "High", "Low", "Close", "O-C Returns", "H-L Returns", "C-C Returns", "Cumulative %", "Probability %"]
    for col in cols:
        df[col] = df[col].replace("nan%", "")
    return df
