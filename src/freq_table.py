import pandas as pd
import numpy as np

dataframe = pd.read_csv("DoR_Automation_Module/datasets/AAPL_DoR_Daily.csv")

def CC_histogram_table_daily(df):
    CC_bins_daily = [-np.inf] + list(np.arange(-6.0, 6.1, 1.5)) + [np.inf]
    df['Bin'] = pd.cut(df['C-C Returns'], bins=CC_bins_daily)
    freq_table = df['Bin'].value_counts().sort_index().reset_index()
    freq_table.columns = ['Bin', 'Frequency']
    freq_table['Cumulative %'] = (freq_table['Frequency'].cumsum() / freq_table['Frequency'].sum() * 100).round(2)
    total_candele = df['C-C Returns'].count()
    freq_table['Probability %'] = ((freq_table['Frequency']/total_candele) * 100).round(2)
    return freq_table


freq_table = CC_histogram_table_daily(dataframe)  
dataframe = dataframe.drop(columns="Bin")
combined = pd.concat(
    [dataframe.reset_index(drop=True), freq_table.reset_index(drop=True)],
    axis=1
)
print(combined)

def HL_histogram_table_daily(df):
    HL_bins_daily =list(np.arange(0, 8.1, 1)) + [np.inf]
    df['Bin'] = pd.cut(df['H-L Returns'], bins=HL_bins_daily)
    freq_table = df['Bin'].value_counts().sort_index().reset_index()
    freq_table.columns = ['Bin', 'Frequency']
    freq_table['Cumulative %'] = (freq_table['Frequency'].cumsum() / freq_table['Frequency'].sum() * 100).round(2)
    total_candele = df['H-L Returns'].count()
    freq_table['Probability %'] = ((freq_table['Frequency']/total_candele) * 100).round(2)
    return freq_table



def OC_histogram_table_daily(df):
    OC_bins_daily = [-np.inf] + list(np.arange(-6.0, 6.1, 1.5)) + [np.inf]
    df['Bin'] = pd.cut(df['O-C Returns'], bins=OC_bins_daily)
    freq_table = df['Bin'].value_counts().sort_index().reset_index()
    freq_table.columns = ['Bin', 'Frequency']
    freq_table['Cumulative %'] = (freq_table['Frequency'].cumsum() / freq_table['Frequency'].sum() * 100).round(2)
    total_candele = df['O-C Returns'].count()
    freq_table['Probability %'] = ((freq_table['Frequency']/total_candele) * 100).round(2)
    return freq_table
    
