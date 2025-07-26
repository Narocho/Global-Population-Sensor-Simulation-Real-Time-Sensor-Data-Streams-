import pandas as pd
import matplotlib.pyplot as plt
import time

# Read your filtered_data CSV
filtered_data = pd.read_csv('filtered_data.csv')

# Replace 'Your Country Name' with the actual country name in your DataFrame
country_name = 'Spain'

# Filter data for the specified country
country_data = filtered_data[filtered_data['country'] == country_name]

country_data.loc[:, 'updated_datetime'] = pd.to_datetime(country_data['updated_datetime'])


# Set up the Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_title(f'Real-time Time Series Plot for Population Over Time - {country_name}')
ax.set_xlabel('Time')
ax.set_ylabel('Population')

# Define a function to update and display the plot
def update_plot(df):
    ax.clear()
    ax.plot(df['updated_datetime'], df['current_population'], marker='o', linestyle='-')
    ax.set_title(f'Real-time Time Series Plot for Population Over Time - {country_name}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Population')
    plt.pause(0.1)

# Create an empty DataFrame to store the streaming data
streaming_df = pd.DataFrame(columns=['iso_code', 'country', 'current_population', 'updated_datetime'])

# creating a loop to simulate a live stream of data.
for index, row in country_data.iterrows():
    # Remove commas from 'current_population' and convert to int
    row['current_population'] = int(row['current_population'].replace(',', ''))

    # Append the row to the streaming DataFrame
    streaming_df = pd.concat([streaming_df, pd.DataFrame([row])], ignore_index=True)

    # Update and display the plot with the streaming data
    update_plot(streaming_df)

    # Sleep to simulate real-time updates (adjust sleep duration as needed)
    time.sleep(3)

