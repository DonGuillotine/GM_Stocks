import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Read stock data from a CSV file
df = pd.read_csv('../stock_data.csv')

# Enter a loop to input a valid stock symbol
while True:
    stock = input("Enter the Stock Symbol: ")
    if df['SYMBOL'].isin([stock]).any(): # Check if the entered stock symbol exists in the dataframe
        break
    else:
        print("Invalid Stock Symbol")

# Transpose the DataFrame, set the first row as column names, and reset the index
df = df.transpose()
df.columns = df.iloc[0]
df = df[1:]
df = df.reset_index()

# Rename the columns to 'ds' for dates and 'y' for the stock symbol
df = df.rename(columns={'index': 'ds', stock: 'y'})

# Convert the 'ds' column to datetime format
df['ds'] = pd.to_datetime(df['ds'])

# Input the number of days for future prediction
days = int(input("Enter the value for days: "))

# Ask the user if they want to perform a backtest
backtest_option = input("Do you want to perform a backtest? (yes/no): ")

if backtest_option.lower() == "yes":
    # Input a start date for backtesting
    start_date = input("Enter the start date for backtesting (YYYY-MM-DD): ")

    # Filter the DataFrame for the backtest period
    backtest_df = backtest_df = df[df['ds'] >= start_date].head(days)

    training_df = df[(df['ds'] < start_date)]
    # Create a Prophet model
    model = Prophet()

    # Fit the model with the DataFrame containing historical stock data for backtesting
    model.fit(training_df)

    # Create a DataFrame for future dates for prediction
    future = model.make_future_dataframe(periods=days)

    # Make predictions using the Prophet model
    prediction = model.predict(future)

    # Extract actual values for the backtest period
    actual_values = backtest_df['y'].values

    # Extract predicted values for the backtest period
    predicted_values = prediction[prediction['ds'] >= start_date]['yhat'].values

    # Calculate Mean Absolute Error (MAE) as a performance metric
    mae = mean_absolute_error(actual_values, predicted_values)

    # Calculate Mean Squared Error (MSE) as a performance metric
    mse = mean_squared_error(actual_values, predicted_values)

    print(predicted_values)
    print(actual_values)

    # Print the performance metrics
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")

else:
    # Create a Prophet model
    model = Prophet()

    # Fit the model with the DataFrame containing historical stock data
    model.fit(df)

    # Create a DataFrame for future dates for prediction
    future = model.make_future_dataframe(periods=days)

    # Make predictions using the Prophet model
    prediction = model.predict(future)

    # Save the prediction results to a CSV file without including the index column
    prediction.to_csv("fbprophet_prediction.csv", index=False)
