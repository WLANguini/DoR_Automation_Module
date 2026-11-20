import pandas as pd
import numpy as np
import openpyxl

df = pd.read_excel("DoR_Automation_Module/src/AAPL_DoR_Daily.xlsx")

def avg_returns_CC(df):
    returns = df["C-C Returns"]
    positive_returns = returns[returns > 0]
    negative_returns = returns[returns < 0]
    zero = returns[returns == 0 ]
    total = len(returns)
    
    summary = pd.DataFrame([
    {
        "Category": "Positive Data Points",
        "Average Returns": positive_returns.mean(),
        "Count": len(positive_returns),
        "Frequency": len(positive_returns)/total,
        "Frequency Adjusted Returns": positive_returns.mean()*(len(positive_returns)/total)
    },
    {
        "Category": "Negative Data Points",
        "Average Returns": negative_returns.mean(),
        "Count": len(negative_returns),
        "Frequency": len(negative_returns)/total,
        "Frequency Adjusted Returns": negative_returns.mean()*(len(negative_returns)/total)
    },
    {
        "Category": "Zero",
        "Average Returns": 0,
        "Count": len(zero),
        "Frequency": len(zero)/total,
        "Frequency Adjusted Returns": 0
    }
    ]).set_index("Category")
    
    return summary

def avg_returns_HL(df):
    returns = df["H-L Returns"]
    positive_returns = returns[returns > 0]
    zero = returns[returns == 0 ]
    total = len(returns)
    
    summary = pd.DataFrame([
    {
        "Category": "Positive Data Points",
        "Average Returns": positive_returns.mean(),
        "Count": len(positive_returns),
        "Frequency": len(positive_returns)/total,
        "Frequency Adjusted Returns": positive_returns.mean()*(len(positive_returns)/total)
    },
    
    {
        "Category": "Zero",
        "Average Returns": 0,
        "Count": len(zero),
        "Frequency": len(zero)/total,
        "Frequency Adjusted Returns": 0
    }
    ]).set_index("Category")
    
    return summary
    
df_avg_returns_CC = avg_returns_CC(df)
df_avg_returns_HL = avg_returns_HL(df)

def dataframe_writer(ws, df, start_row, start_col):
    ws.cell(row=start_row, column=start_col, value = df.index.name or "")
    for j, col in enumerate(df.columns):
        ws.cell(row=start_row, column=start_col + 1 + j, value = col)
    
    for i, (idx, row) in enumerate(df.iterrows()):
        ws.cell(row = start_row + 1 + i, column=start_col, value=idx)
        for j, val in enumerate(row):
            ws.cell(row = start_row + 1 + i, column=start_col + 1 + j, value = val)
        

