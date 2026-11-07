import pandas as pd
import numpy as np

def add_descriptive_statistics_for_CC(df):
    statistics = df["C-C Returns"].describe()
    statistics = pd.DataFrame(statistics)
    statistics = statistics.reset_index()
    statistics.rename(columns={"C-C Returns": "Value", "index": "Statistic"}, inplace=True)
    kurtosis = df["C-C Returns"].kurt()
    skewness = df["C-C Returns"].skew()
    standard_error = df["C-C Returns"].sem()
    sample_variance = df["C-C Returns"].var()
    range = df["C-C Returns"].max() - df["C-C Returns"].min()

    new_rows = pd.DataFrame([
        {"Statistic": "kurtosis", "Value": kurtosis},
        {"Statistic": "skewness", "Value": skewness},
        {"Statistic": "standard error", "Value": standard_error},
        {"Statistic": "sample variance", "Value": sample_variance},
        {"Statistic": "range", "Value": range}
    ])
    useless_statistics = ["75%", "50%", "25%"]
    for i in useless_statistics:
        statistics = statistics[statistics["Statistic"] != i]
    statistics = pd.concat([statistics, new_rows], ignore_index=True)
    df["Statistic C-C Returns"] = statistics["Statistic"]
    df["Value C-C Returns"] = statistics["Value"]
    
    return df

def add_descriptive_statistics_for_HL(df):
    statistics = df["H-L Returns"].describe()
    statistics = pd.DataFrame(statistics)
    statistics = statistics.reset_index()
    statistics.rename(columns={"H-L Returns": "Value", "index": "Statistic"}, inplace=True)
    kurtosis = df["H-L Returns"].kurt()
    skewness = df["H-L Returns"].skew()
    standard_error = df["H-L Returns"].sem()
    sample_variance = df["H-L Returns"].var()
    range = df["H-L Returns"].max() - df["H-L Returns"].min()

    new_rows = pd.DataFrame([
        {"Statistic": "kurtosis", "Value": kurtosis},
        {"Statistic": "skewness", "Value": skewness},
        {"Statistic": "standard error", "Value": standard_error},
        {"Statistic": "sample variance", "Value": sample_variance},
        {"Statistic": "range", "Value": range}
    ])
    useless_statistics = ["75%", "50%", "25%"]
    for i in useless_statistics:
        statistics = statistics[statistics["Statistic"] != i]
    statistics = pd.concat([statistics, new_rows], ignore_index=True)
    df["Statistic H-L Returns"] = statistics["Statistic"]
    df["Value H-L Returns"] = statistics["Value"]
    
    return df


