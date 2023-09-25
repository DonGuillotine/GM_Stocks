import csv
import os
import pandas as pd

# Define the input and output file paths
input_file = os.path.join('..', 'stock_data.csv')
output_file = os.path.join('result.csv')

def find_breakout_stocks(data_file, percentage_threshold):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data_file)

    # Initialize an empty list to store breakout stocks
    breakout_stocks = []

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        symbol = row['SYMBOL']
        prices = row[1:]  # Exclude the 'SYMBOL' column
        all_time_high = max(prices[-60:])
        current_price = prices[-1]

        # Calculate the percentage increase from the previous all-time high
        percentage_increase = ((current_price - all_time_high) / all_time_high) * 100

        # Check if the percentage increase is greater than the threshold
        if percentage_increase <= 1 and percentage_increase >= 0 :
            breakout_stocks.append(symbol)

    return breakout_stocks

# Example usage:
data_file = input_file
percentage_threshold = 5  # You can change this threshold as needed
breakout_stocks = find_breakout_stocks(data_file, percentage_threshold)

# Save the results to an output CSV file
with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Breakout Stocks'])
    csv_writer.writerows(breakout_stocks)

print("Breakout Stocks ({}% above all-time high):".format(percentage_threshold))
print(breakout_stocks)
