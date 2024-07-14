import math
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

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

df_winners = pd.merge(left=winners,right=df,on='Index')
df_winners = df_winners[['Day','Weekday','Race Number','Post Position','M/L Odds','Final Odds','Change In Odds',
                       'Distance','FieldSize','Favorite','HalfMileTime','FinalTime','WinnersTrainer',
                       'WinnersJockey','ExactaPayout','SuperfectaPayout','TrifectaPayout']]
print(df_winners.head())
df_winners['Final Odds'] = df_winners['Final Odds'].astype('Float64')
print(df_winners.convert_dtypes().dtypes)

df_winners.to_csv("merged_data_sets.csv")

winning_post_positions = df_winners['Post Position'].value_counts()
print(winning_post_positions)
winning_jockey = df_winners['WinnersJockey'].value_counts()
print(winning_jockey)
winning_trainer = df_winners['WinnersTrainer'].value_counts()
print(winning_trainer)
number_of_scratches = len(df_main[df_main["Finish"]=='S'])
print(number_of_scratches)

average_field_size_by_weekday = df_winners.groupby("Weekday")["FieldSize"].mean()
print(average_field_size_by_weekday)
average_halfmile_by_distance = df_winners.groupby("Distance")["HalfMileTime"].mean()
print(average_halfmile_by_distance)
average_finaltime_by_distance = df_winners.groupby("Distance")["FinalTime"].mean()
print(average_finaltime_by_distance)
average_winner_mlodds = df_winners["M/L Odds"].mean()
print(average_winner_mlodds)
average_winner_finalodds = df_winners["Final Odds"].mean()
print(average_winner_finalodds)
average_winner_oddschange = average_winner_finalodds - average_winner_mlodds
print(average_winner_oddschange)

df_main_no_scratches = df_main[df_main["Finish"] != "S"]
df_main_no_scratches['Final Odds'] = df_main_no_scratches['Final Odds'].astype('Float64')
df_main_no_scratches['Finish'] = df_main_no_scratches['Finish'].astype('Int64')
df_main_no_scratches['Change In Odds'] = np.abs(df_main_no_scratches['Change In Odds'])
print(df_main_no_scratches.convert_dtypes().dtypes)
print(df_main_no_scratches.head(20))

#M/L odds model
X = np.array(df_main_no_scratches['M/L Odds']).reshape(-1, 1)
y = np.array(df_main_no_scratches['Finish']).reshape(-1, 1)
ml_model = LinearRegression().fit(X,y)
print ('Intercept: ',ml_model.intercept_)    
print ('Coefficients: ', ml_model.coef_[0])
# MSE
y_pred = ml_model.predict(X)
mse = mean_squared_error(y, y_pred)
print(mse)
y.mean() 
y.std() 
# RMSE
print(np.sqrt(mse))
# MAE
print(mean_absolute_error(y, y_pred))
# R2 Score
print(ml_model.score(X, y))

#Final Odds model
X = np.array(df_main_no_scratches['Final Odds']).reshape(-1, 1)
f_model = LinearRegression().fit(X,y)
print ('Intercept: ',f_model.intercept_)    
print ('Coefficients: ', f_model.coef_[0])
# MSE
y_pred = f_model.predict(X)
mse = mean_squared_error(y, y_pred)
print(mse)
y.mean() 
y.std() 
# RMSE
print(np.sqrt(mse))
# MAE
print(mean_absolute_error(y, y_pred))
# R2 Score
print(f_model.score(X, y))

#change in odds model
X = np.array(df_main_no_scratches['Change In Odds']).reshape(-1, 1)
cio_model = LinearRegression().fit(X,y)
print ('Intercept: ',cio_model.intercept_)    
print ('Coefficients: ', cio_model.coef_[0])
# MSE
y_pred = cio_model.predict(X)
mse = mean_squared_error(y, y_pred)
print(mse)
y.mean() 
y.std() 
# RMSE
print(np.sqrt(mse))
# MAE
print(mean_absolute_error(y, y_pred))
# R2 Score
print(cio_model.score(X, y))

#compare models