import pandas as pd
import numpy as np

def add_descriptive_statistics(df):
    statistics = df["C-C Returns"].describe()
    statistics = pd.DataFrame(statistics)
    statistics = statistics.reset_index()
    statistics.rename(columns={"C-C Returns": "Value", "index": "Statistic"}, inplace=True)
    kurtosis = df["C-C Returns"].kurt()
    skewness = df["C-C Returns"].skew()

    new_rows = pd.DataFrame([
        {"Statistic": "kurtosis", "Value": kurtosis},
        {"Statistic": "skewness", "Value": skewness}
    ])
    statistics = pd.concat([statistics, new_rows], ignore_index=True)
    df["Statistic"] = statistics["Statistic"]
    df["Value"] = statistics["Value"]
    return df