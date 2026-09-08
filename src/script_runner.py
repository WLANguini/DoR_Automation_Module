import pandas as pd
import numpy as np
import yfinance as yf
import os
from DoR_Automation_Module.src.data_cleaning import data_cleaning as clean_data
from DoR_Automation_Module.src.data_processing import processing_data

tick = "AAPL"
ticker = yf.Ticker(tick)

timeframes = {
    "Daily" : "1d",
    "Weekly" : "1wk",
    "Monthly" : "1mo",
    "Quarterly" : "3mo"
}

for name, interval in timeframes.items():
    data = ticker.history(period = "max", interval = interval)
    df = pd.DataFrame(data)
    df = df.reset_index()
    df = clean_data(df)
    df = processing_data(df)
    df.to_csv(f"DoR_Automation_Module/datasets/{tick}_DoR_{name}.csv", index=False)
    print(f"Fisier {tick}_DoR_{name} salvat")



