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
df_merged = df_merged[['Day','Weekday','Race Number','Post Position','M/L Odds','Final Odds','Distance','FieldSize',
                       'Favorite','HalfMileTime','FinalTime','WinnersTrainer','WinnersJockey','ExactaPayout',
                       'SuperfectaPayout','TrifectaPayout']]
print(df_merged.head())
df_merged['Final Odds'] = df_merged['Final Odds'].astype('Float64')
print(df_merged.convert_dtypes().dtypes)

#df_merged.to_csv("merged_data_sets.csv")

winning_post_positions = df_merged['Post Position'].value_counts()
print(winning_post_positions)
winning_jockey = df_merged['WinnersJockey'].value_counts()
print(winning_jockey)
winning_trainer = df_merged['WinnersTrainer'].value_counts()
print(winning_trainer)
number_of_scratches = len(df_main[df_main["Finish"]=='S'])
print(number_of_scratches)
#use merged
#average_field_size_by_weekday = 
#average_halfmile_by_distance = 
#average_finaltime_by_distance =
#average_mlodds = 
#average_finalodds = 

#use main
#calculate change in odds
#M/L odds model
#Final Odds model
#change in odds model
#compare models