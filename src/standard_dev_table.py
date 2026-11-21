import pandas as pd
import numpy as np
import openpyxl

df = pd.read_excel("DoR_Automation_Module/src/AAPL_DoR_Daily.xlsx")

def add_std_table_CC(df):
    cc_returns = df["C-C Returns"]
    mean = cc_returns.mean()
    standard_deviation = cc_returns.std()
    total = len(cc_returns)
    
    rows = []
    
    for i in [1,2,3]:
        mask = (cc_returns < mean + (i * standard_deviation)) & (cc_returns > mean - (i * standard_deviation))
        actual_count = mask.sum()
        rows.append({
            "Standard deviation" : i,
            "Upper Bound": mean + (i * standard_deviation),
            "Lower Bound": mean - (i * standard_deviation),
            "Actual Count": actual_count,
            "Actual % Count": actual_count/total
            })
        summary = pd.DataFrame(rows)
        summary["Normal % Count"] = {
            0: "68.27%",
            1: "95.45%",
            2: "99.73%"
        }
        
    return summary

def add_std_table_CC(df):
    hl_returns = df["H-L Returns"]
    mean = hl_returns.mean()
    standard_deviation = hl_returns.std()
    total = len(hl_returns)
    
    rows = []
    
    for i in [1,2,3]:
        mask = (hl_returns < mean + (i * standard_deviation)) & (hl_returns > mean - (i * standard_deviation))
        actual_count = mask.sum()
        rows.append({
            "Standard deviation" : i,
            "Upper Bound": mean + (i * standard_deviation),
            "Lower Bound": mean - (i * standard_deviation),
            "Actual Count": actual_count,
            "Actual % Count": actual_count/total
            })
        summary = pd.DataFrame(rows)
        summary["Normal % Count"] = {
            0: "68.27%",
            1: "95.45%",
            2: "99.73%"
        }
        
    return summary

def std_df_writer(ws, df, start_row, start_col):
    ws.cell(row=start_row, column= start_col, value=df.index.name or "")
    for j, col in enumerate(df.columns):
        ws.cell(row=start_row, column = start_col + 1 + j,  value = col)
        
    for i, (idx, row) in enumerate(df.iterrows()):
        ws.cell(row = start_row + 1 + i, column = start_col, value = idx)
        for j, val in enumerate(row):
            ws.cell(row = start_row + 1 + i, column = start_col + 1 + j, value = val)
            
        
    

print(add_std_table_CC(df))
