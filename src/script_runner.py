import pandas as pd
import numpy as np
import yfinance as yf
import os
import openpyxl
from DoR_Automation_Module.src.data_cleaning import data_cleaning as clean_data, recleaning
from DoR_Automation_Module.src.data_preprocessing import processing_data, data_format
from DoR_Automation_Module.src.freq_table import CC_histogram_table, HL_histogram_table
from DoR_Automation_Module.src.desctiptive_statistics import add_descriptive_statistics_for_CC, add_descriptive_statistics_for_HL
from DoR_Automation_Module.src.returns_table import avg_returns_CC, avg_returns_HL, dataframe_writer

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
    df = add_descriptive_statistics_for_CC(df)
    df = HL_histogram_table(df, name)
    df = add_descriptive_statistics_for_HL(df)
    cc_summary = avg_returns_CC(df)
    hl_summary = avg_returns_HL(df)
    df = data_format(df)
    df = recleaning(df)
    
    FILE_PATH = f"DoR_Automation_Module/datasets/{tick}_DoR_{name}.xlsx"
    df.to_excel(FILE_PATH, index=False)
    
    wb = openpyxl.load_workbook(FILE_PATH)
    ws = wb.active
    
    dataframe_writer(ws, cc_summary, start_row=13, start_col=9)
    dataframe_writer(ws, hl_summary, start_row=13, start_col=15)
    
    wb.save(FILE_PATH)
    
    print(f"Fisier {tick}_DoR_{name} creat")
    



