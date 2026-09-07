import pandas as pd
import numpy as np
import yfinance as yf
import os
from DoR_Automation_Module.src.data_cleaning import data_cleaning as clean_data
from DoR_Automation_Module.src.data_processing import processing_data

tick = "AAPL"
ticker = yf.Ticker(tick)
data = ticker.history(period = "max")
df = pd.DataFrame(data)
df = df.reset_index()

df.to_csv("DoR_Automation_Module/datasets/AAPL_DoR_Daily")

DATASET_PATH = "DoR_Automation_Module/datasets"

for ds in os.listdir(DATASET_PATH):
    DATA_PATH = f"DoR_Automation_Module/datasets/{ds}"
    df = pd.read_csv(DATA_PATH)
    df = clean_data(df)
    df = processing_data(df)

df.to_csv("DoR_Automation_Module/datasets/AAPL_DoR_Daily")