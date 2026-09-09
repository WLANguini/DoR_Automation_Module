import pandas as pd
import numpy as np

dataframe = pd.read_csv("DoR_Automation_Module/datasets/AAPL_DoR_Daily.csv")

def histogram_table(df):
    bins = [-np.inf] + list(np.arange(-6.0, 6.1, 1.5)) + [np.inf]
    df['Bin'] = pd.cut(df['C-C Returns'], bins=bins)
    freq_table = df['Bin'].value_counts().sort_index().reset_index()
    freq_table.columns = ['Bin', 'Frequency']
    freq_table['Cumulative %'] = (freq_table['Frequency'].cumsum() / freq_table['Frequency'].sum() * 100).round(2)
    total_candele = df['C-C Returns'].count()
    freq_table['Probability %'] = (freq_table['Frequency']/total_candele) * 100
    return freq_table

print(histogram_table(dataframe))

