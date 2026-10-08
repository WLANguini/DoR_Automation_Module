import pandas as pd
import numpy as np
import os

dataframe = pd.read_csv("DoR_Automation_Module/datasets/AAPL_DoR_Daily.csv")


def CC_histogram_table(df, timeframe):
    bins_CC = {
    "Daily" : list(np.arange(-6.0, 6.1, 1.5)),
    "Weekly" : list(np.arange(-12.0, 12.1, 3.0)),
    "Monthly" : list(np.arange(-30.0, 30.1, 6.0)),
    "Quarterly" : list(np.arange(-60.0, 60.1, 12.0))
    }
    
    bins = [-np.inf] + bins_CC[timeframe] + [np.inf]

    binned = pd.cut(df['C-C Returns'], bins=bins)  

    freq_table = binned.value_counts().sort_index().reset_index()
    freq_table.columns = ['Bin', 'Frequency']
    freq_table['Cumulative %'] = (freq_table['Frequency'].cumsum() / freq_table['Frequency'].sum() * 100).round(2)

    total_candele = df['C-C Returns'].count()
    freq_table['Probability %'] = ((freq_table['Frequency'] / total_candele) * 100).round(2)

    combined = pd.concat(
        [df.reset_index(drop=True), freq_table.reset_index(drop=True)], axis=1
    )
    
    return combined

print(CC_histogram_table(dataframe, "Daily"))

def HL_histogram_table(df, timeframe):
    
    bins_HL = {
    "Daily" : list(np.arange(0, 8.1, 1)),
    "Weekly" : list(np.arange(0, 20.1, 2.5)),
    "Monthly" : list(np.arange(0, 50.1, 5)),
    "Quarterly" : list(np.arange(0, 100.1, 10))
    }   
    
    bins = bins_HL[timeframe] + [np.inf]
    binned = pd.cut(df['C-C Returns'], bins=bins) 
    freq_table = binned.value_counts().sort_index().reset_index()
    freq_table.columns = ['Bin', 'Frequency']
    freq_table['Cumulative %'] = (freq_table['Frequency'].cumsum() / freq_table['Frequency'].sum() * 100).round(2)
    total_candele = df['H-L Returns'].count()
    freq_table['Probability %'] = ((freq_table['Frequency']/total_candele) * 100).round(2)
    
    return freq_table

print(HL_histogram_table(dataframe, "Daily"))

def OC_histogram_table(df):
    OC_bins_daily = [-np.inf] + list(np.arange(-6.0, 6.1, 1.5)) + [np.inf]
    df['Bin'] = pd.cut(df['O-C Returns'], bins=OC_bins_daily)
    freq_table = df['Bin'].value_counts().sort_index().reset_index()
    freq_table.columns = ['Bin', 'Frequency']
    freq_table['Cumulative %'] = (freq_table['Frequency'].cumsum() / freq_table['Frequency'].sum() * 100).round(2)
    total_candele = df['O-C Returns'].count()
    freq_table['Probability %'] = ((freq_table['Frequency']/total_candele) * 100).round(2)
    return freq_table
    