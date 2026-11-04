import pandas as pd
import numpy as np
import yfinance as yf
import os

def processing_data(df):
    df["O-C Returns"] = ((df["Close"] - df["Open"])/df["Open"])*100
    df["H-L Returns"] = ((df["High"] - df["Low"])/df["Low"])*100
    df['C-C Returns'] = ((df['Close'] - df['Close'].shift(-1)) / df['Close'].shift(-1))*100
    return df

def data_format(df):
    cols = ["Open", "High", "Low", "Close", "O-C Returns", "H-L Returns", "C-C Returns"]
    for col in cols:
        if col == "Open" or col == "High" or col == "Low" or col == "Close":
            df[col] = df[col].map(lambda x: f"{x:.3f}")
        elif col == "O-C Returns" or col == "H-L Returns" or col == "C-C Returns":
            df[col] = df[col].map(lambda x: f"{x:.3f}%")
    return df