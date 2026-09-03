import numpy as np
import pandas as pd
data=pd.read_csv('Dataset.csv')
print(data.head())
print(data.tail())
print(data.info())
print(data.shape)
data.dropna(inplace=True)
print(data.describe())
# Sleep_hours column has wrong values, we will replace them with the mean of the column
mode_sleep_hours = data['Sleep_hours'].mode()[0]
print(f"Mode of Sleep_hours: {mode_sleep_hours}")
for i in data.index:
    if data.loc[i, 'Sleep_hours'] > 7:
        data.loc[i, 'Sleep_hours'] = mode_sleep_hours
print(data.describe()) 
print(data.info())
# we saw some object type values in attendance column, we will replace them with thier corresponding integer values
print(data['Attendance'].to_string())
data['Attendance'] = pd.to_numeric(data['Attendance'] , errors='coerce')
data.fillna({'Attendance': data['Attendance'].median()} , inplace=True)
# print(data['Attendance'].to_string())
#lets check for duplicated rows
print(data.duplicated().to_string()) 
data.drop_duplicates(inplace=True)
print(data.info())
data.to_csv('Cleaned_Dataset.csv', index=False)
