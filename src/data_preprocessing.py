import pandas as pd
import numpy as np
import yfinance as yf
import os

def processing_data(df):
    df["O-C Returns"] = ((df["Close"] - df["Open"])/df["Open"])*100
    df["H-L Returns"] = ((df["High"] - df["Low"])/df["Low"])*100
    df['C-C Returns'] = ((df['Close'] - df['Close'].shift(-1)) / df['Close'].shift(-1))*100 #*100 to convert our returns to percentage BUT WITHOUT THE "%"
    return df

def data_format(df):
    cols = ["Open", "High", "Low", "Close", "O-C Returns", "H-L Returns", "C-C Returns", "Cumulative %", "Probability %"]
    for col in cols:
        if col == "Open" or col == "High" or col == "Low" or col == "Close":
            df[col] = df[col].map(lambda x: f"{x:.3f}")
        """elif col == "O-C Returns" or col == "H-L Returns" or col == "C-C Returns" or col == "Cumulative %" or col == "Probability %":
            df[col] = df[col].map(lambda x: f"{x:.3f}%") # This will add the "%" - SOULD USE as the last step
        else:
            pass"""
    df['Date'] = pd.to_datetime(df['Date']).dt.tz_convert(None)
    return df