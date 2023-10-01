import pandas as pd
from prophet import Prophet

df = pd.read_csv('../stock_data.csv')
while True:
    stock = input("Enter the Stock Symbol: ")
    if df['SYMBOL'].isin([stock]).any():
        break
    else:
        print("Invalid Stock Symbol")

days = int(input("Enter the value for days: "))
df = df.transpose()
df.columns = df.iloc[0]
df = df[1:]
df = df.reset_index()
df = df.rename(columns={'index': 'ds', stock: 'y'})
df['ds'] = pd.to_datetime(df['ds'])

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=days)
prediction = model.predict(future)
prediction.to_csv("fbprophet_prediction.csv",index=False)