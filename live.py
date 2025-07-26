import pandas as pd
import matplotlib.pyplot as plt
import time

# Read your filtered_data CSV
filtered_data = pd.read_csv('filtered_data.csv')

# Set up the Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Real-time Population Visualization')
ax.set_xlabel('Timestamp')
ax.set_ylabel('Population')

# Define a function to update and display the plot
def update_plot(df):
    ax.clear()
    ax.plot(df['updated_datetime'], df['current_population'], marker='o')
    ax.set_title('Real-time Population Visualization')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Population')
    plt.pause(0.1)

# Create an empty DataFrame to store the streaming data
streaming_df = pd.DataFrame(columns=['iso_code', 'country', 'current_population', 'updated_datetime'])

# creating a loop to simulate a live stream of data.
for index, row in filtered_data.iterrows():
    current_date = pd.to_datetime(row['updated_datetime'])

    # Check if the date is within the specified range (December 1st to December 10th, 2023)
    if pd.to_datetime('2023-12-01') <= current_date <= pd.to_datetime('2023-12-10'):
        # Remove commas from 'current_population' and convert to int
        row['current_population'] = int(row['current_population'].replace(',', ''))

        # Concatenate the row to the streaming DataFrame
        streaming_df = pd.concat([streaming_df, pd.DataFrame([row])], ignore_index=True)

        # Update and display the plot with the streaming data
        update_plot(streaming_df)

        # Sleep to simulate real-time updates (adjust sleep duration as needed)
        time.sleep(3)
