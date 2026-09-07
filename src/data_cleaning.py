import pandas as pd
import numpy as np
import yfinance as yf

df = pd.read_csv("DoR_Automation_Module/datasets/AAPL_DoR")

def data_cleaning(dataframe):
    dataframe = dataframe.drop(columns= "Volume")
    dataframe = dataframe.drop(columns= "Dividends")
    dataframe = dataframe.drop(columns= "Stock Splits")
    dataframe = dataframe.sort_values(by="Date", ascending=False)
    
    return dataframe


print(data_cleaning(df))