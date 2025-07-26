import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

# Read your filtered_data CSV
filtered_data = pd.read_csv('filtered_data.csv')

# Set up the Matplotlib figure and axis
plt.figure(figsize=(15, 10))
plt.title('Real-time Heatmap for Population Changes Over Time')
plt.xlabel('Time')
plt.ylabel('Country')



# Get unique countries
unique_countries = filtered_data['country'].unique()

# Create an empty DataFrame to store the streaming data
streaming_df = pd.DataFrame(columns=['iso_code', 'country', 'current_population', 'updated_datetime'])

# creating a loop to simulate a live stream of data.
for index, row in filtered_data.iterrows():
    # Remove commas from 'current_population' and convert to int
    row['current_population'] = int(row['current_population'].replace(',', ''))

    # Append the row to the streaming DataFrame
    streaming_df = pd.concat([streaming_df, pd.DataFrame([row])], ignore_index=True)

    # Convert 'current_population' to numeric
    streaming_df['current_population'] = pd.to_numeric(streaming_df['current_population'], errors='coerce')

    # Pivot the streaming DataFrame for heatmap visualization
    heatmap_data = streaming_df.pivot(index='country', columns='updated_datetime', values='current_population')

    # Create the heatmap
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='g', cbar_kws={'label': 'Population'})

    # Display the heatmap
    plt.pause(0.1)

    # Clear the plot for the next iteration
    plt.clf()

    # Sleep to simulate real-time updates (adjust sleep duration as needed)
    time.sleep(3)
