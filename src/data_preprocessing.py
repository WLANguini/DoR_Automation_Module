import pandas as pd
import numpy as np
import yfinance as yf
import os

def processing_data(df):
    df["Open"] = df["Open"].round(3)
    df["High"] = df["High"].round(3)
    df["Low"] = df["Low"].round(3)
    df["Close"] = df["Close"].round(3)
    df["O-C Returns"] = (((df["Close"] - df["Open"])/df["Open"])*100).round(3)
    df["H-L Returns"] = (((df["High"] - df["Low"])/df["Low"])*100).round(3)
    df['C-C Returns'] = ((df['Close'] - df['Close'].shift(-1)) / df['Close'].shift(-1) * 100).round(3)
    df = df.dropna()
    return df
