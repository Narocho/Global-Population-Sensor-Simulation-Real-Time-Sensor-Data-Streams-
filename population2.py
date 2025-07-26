import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('timeseries_population_count.csv')  # Replace 'your_file.csv' with the actual file name

# Convert the 'updated_datetime' column to datetime format
df['updated_datetime'] = pd.to_datetime(df['updated_datetime'])

# Specify the date range
start_date = '2023-12-01'
end_date = '2023-12-10'

# Filter data for the specified date range
filtered_data = df[(df['updated_datetime'] >= start_date) & (df['updated_datetime'] <= end_date)]

# Save the filtered data to a new CSV file
filtered_data.to_csv('filtered_data.csv', index=False)  # Replace 'filtered_data.csv' with your desired output file name
# Load the filtered data
filtered_data = pd.read_csv('filtered_data.csv')

