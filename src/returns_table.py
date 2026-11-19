import pandas as pd
import numpy as np

df = pd.read_excel("DoR_Automation_Module/src/AAPL_DoR_Daily.xlsx")

def avg_returns_CC(df):
    returns = df["C-C Returns"]
    positive_returns = returns[returns > 0]
    negative_returns = returns[returns < 0]
    zero = returns[returns == 0 ]
    total = len(returns)
    
    rows = [
        [
            "Positive Data Points", positive_returns.mean(), len(positive_returns), len(positive_returns)/total, 
            positive_returns.mean()*(len(positive_returns)/total)
        ],
        
        [
            "Negative Data Points", negative_returns.mean(), len(negative_returns), len(negative_returns)/total,
            negative_returns.mean()*(len(negative_returns)/total)
        ],
        
        [
            "Zero", 0, len(zero), len(zero)/total, 0  
        ]
    ]
    return rows

def avg_returns_HL(df):
    returns = df[" Returns"]
    positive_returns = returns[returns > 0]
    zero = returns[returns == 0 ]
    total = len(returns)
    
    rows = [
        [
            "Positive Data Points", positive_returns.mean(), len(positive_returns), len(positive_returns)/total, 
            positive_returns.mean()*(len(positive_returns)/total)
        ],
        
        [
            "Zero", 0, len(zero), len(zero)/total, 0  
        ]
    ]
    return rows

print(avg_returns_CC(df))
