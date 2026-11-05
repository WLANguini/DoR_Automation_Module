import pandas as pd
import numpy as np
import yfinance as yf
import os
from DoR_Automation_Module.src.data_cleaning import data_cleaning as clean_data, recleaning
from DoR_Automation_Module.src.data_preprocessing import processing_data, data_format
from DoR_Automation_Module.src.freq_table import CC_histogram_table, HL_histogram_table
from DoR_Automation_Module.src.desctiptive_statistics import add_descriptive_statistics

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
    df = CC_histogram_table(df, name)
    df = HL_histogram_table(df, name)
    df = add_descriptive_statistics(df)
    df = data_format(df)
    df = recleaning(df)
    df.to_excel(f"DoR_Automation_Module/datasets/{tick}_DoR_{name}.xlsx", index=False)
    print(f"Fisier {tick}_DoR_{name} salvat")



