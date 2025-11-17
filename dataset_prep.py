import pandas as pd

df = pd.read_csv("weatherAUS.csv");

req_cols = ['MinTemp','MaxTemp', 'Rainfall','Humidity9am'
            ,'Humidity3pm', 'RainToday', 'RainTomorrow']

df = df[req_cols]

df['RainToday'] = df['RainToday'].map({'Yes':1, 'No': 0})
df['RainTomorrow'] = df['RainTomorrow'].map({'Yes':1, 'No':0})


df = df.dropna()
df.to_csv("weatherDataset.csv",index=False)

