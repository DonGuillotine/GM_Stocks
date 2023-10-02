import pandas as pd
import os

def momentum_generic_simple(input_csv_file, output_csv_file, num_days):
    try:
        # Read the input CSV file into a DataFrame
        df = pd.read_csv(input_csv_file)
        
        # Calculate the new column values for all rows by dividing the last column by num_days columns back
        df['New_Column'] = df.iloc[:, -1] / df.iloc[:, -num_days]
        
        # Round the new column values to three decimal places
        df['New_Column'] = df['New_Column'].round(3)
        
        # Sort the DataFrame in descending order based on the new column
        df_result_sorted = df.sort_values(by='New_Column', ascending=False)
        
        # Take the top row of the sorted DataFrame
        top_row = df_result_sorted.iloc[0]
        
        # Create a new DataFrame with the top row's symbol and new column value
        df_result = pd.DataFrame({'SYMBOL': [top_row['SYMBOL']], 'New_Column': [top_row['New_Column']]})
        
        # Save the resulting DataFrame to the specified output CSV file
        df_result.to_csv(output_csv_file, index=False)
        
        return True
    except Exception as e:
        return False

# Define the fixed input CSV file path
input_csv_file = os.path.join('..', 'stock_data.csv')

# Ask the user to input the number of days
num_days = int(input("Enter the number of days: "))

# Specify the desired output CSV file name
output_csv_file = "result.csv"

if momentum_generic_simple(input_csv_file, output_csv_file, num_days):
    print(f"Top row saved to {output_csv_file}.")
else:
    print("Error processing the CSV file.")
