import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the tracking data from a CSV file into a pandas DataFrame
# df = pd.read_csv('tracking_data.csv')  # Replace 'tracking_data.csv' with your actual file name or data source
df = pd.read_csv('whale_tracker_test_data.csv')

# Extract the last known GPS coordinates and speed
last_latitude = df['Latitude'].iloc[-1]
last_longitude = df['Longitude'].iloc[-1]
speed = df['Speed'].iloc[-1]

# Determine the recent history of GPS coordinates
history_latitudes = df['Latitude'].iloc[-10:-5].to_numpy()
history_longitudes = df['Longitude'].iloc[-10:-5].to_numpy()

# Calculate the average change in latitude and longitude based on the recent history
avg_delta_latitude = np.mean(np.diff(history_latitudes))
avg_delta_longitude = np.mean(np.diff(history_longitudes))

# Calculate the next five possible GPS coordinates based on the recent history
next_latitudes = [last_latitude + (i+1) * avg_delta_latitude for i in range(5)]
next_longitudes = [last_longitude + (i+1) * avg_delta_longitude for i in range(5)]

# Plot the known coordinates, recent history, and next five possible coordinates
plt.scatter(df['Longitude'], df['Latitude'], color='red', alpha=0.7, s=50)
plt.scatter(history_longitudes, history_latitudes, color='orange', alpha=0.7, s=50)
plt.scatter(next_longitudes, next_latitudes, color='blue', alpha=0.7, s=50)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Estimated Route of Tracked Whale')
plt.legend(['Known Coordinates', 'Recent History', 'Next 5 Possible Coordinates'])
plt.show()
