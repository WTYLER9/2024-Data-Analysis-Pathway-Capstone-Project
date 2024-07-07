import math
import numpy as np
import pandas as pd
import sklearn

df = pd.read_csv("Keeneland Race Data Since Oct-2006.csv")
df = df[df["RaceMeet"] == "Spring 2024"]
df['Index'] = np.arange(len(df))
print(df.head())
print(len(df))

df_main = pd.read_csv("Keeneland April 2024 Data for Capstone Project.csv")
print(df_main.isnull().values.any())
winners = df_main[df_main["Finish"] == "1"]
winners['Index'] = np.arange(len(winners))
print(df_main.head(20))
print(winners.head(15))
print(len(winners))

df_merged = pd.merge(left=winners,right=df,on='Index')
print(df_merged.head())

df_merged.to_csv("merged_data_sets.csv")
