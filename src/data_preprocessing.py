import pandas as pd
import numpy as np
import yfinance as yf
import os

def processing_data(df):
    df["O-C Returns"] = ((df["Close"] - df["Open"])/df["Open"])*100
    df["H-L Returns"] = ((df["High"] - df["Low"])/df["Low"])*100
    df['C-C Returns'] = df['Close'].pct_change() * 100
    df = df.dropna()
    return df
