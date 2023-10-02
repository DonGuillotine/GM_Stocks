import pandas as pd
import os

def momentum_genric_total(filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Get the last column name (assuming it's the last column in the DataFrame)
    last_column_name = df.columns[-1]

    # Get user input for days and weights
    user_input = []
    while True:
        try:
            days, weight = map(int, input("Enter days and weight (e.g., 10, 30): ").split(","))
            user_input.append((days, weight))
        except ValueError:
            break

    # Calculate the new combined column based on user input
    momentum_total = 0
    for days, weight in user_input:
        last_Days_name=df.columns[-days]
     
        momentum_total += (df[last_column_name] / (df[last_Days_name])) * weight
        print(momentum_total)
    # print(momentum_total)

   # Format the values in the new_combined_column to three decimal places
    df['momentum_total'] = momentum_total


    # Create a new DataFrame with only 'SYMBOL' and 'momentum_total ' columns
    result_df = df[['SYMBOL', 'momentum_total']]

    # Sort the DataFrame in descending order based on 'momentum_total'
    result_df = result_df.sort_values(by='momentum_total', ascending=False)

    # Save the sorted DataFrame to the CSV file
    result_df.to_csv('result.csv', index=False)

# Usage example:
momentum_genric_total(os.path.join('..', 'stock_data.csv'))
