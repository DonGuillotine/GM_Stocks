import pandas as pd
from prophet import Prophet

# Read stock data from a CSV file
df = pd.read_csv('../stock_data.csv')

# Enter a loop to input a valid stock symbol
while True:
    stock = input("Enter the Stock Symbol: ")
    if df['SYMBOL'].isin([stock]).any(): # Check if the entered stock symbol exists in the dataframe
        break
    else:
        print("Invalid Stock Symbol")

# Input the number of days for future prediction
days = int(input("Enter the value for days: "))

# Transpose the DataFrame, set the first row as column names, and reset the index
df = df.transpose()
df.columns = df.iloc[0]
df = df[1:]
df = df.reset_index()

# Rename the columns to 'ds' for dates and 'y' for the stock symbol
df = df.rename(columns={'index': 'ds', stock: 'y'})

# Convert the 'ds' column to datetime format
df['ds'] = pd.to_datetime(df['ds'])

# Create a Prophet model
model = Prophet()

# Fit the model with the DataFrame containing historical stock data
model.fit(df)

# Create a DataFrame for future dates for prediction
future = model.make_future_dataframe(periods=days)

# Make predictions using the Prophet model
prediction = model.predict(future)

# Save the prediction results to a CSV file without including the index column
prediction.to_csv("fbprophet_prediction.csv",index=False)