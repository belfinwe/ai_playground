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

# Calculate the change in latitude and longitude based on speed and direction
distance = speed * 5  # Assuming time interval of 5 units
direction = np.arctan2(df['Latitude'].diff().iloc[-1], df['Longitude'].diff().iloc[-1])
delta_latitude = distance * np.sin(direction)
delta_longitude = distance * np.cos(direction)

# Calculate the next five possible GPS coordinates
next_latitudes = [last_latitude + i * delta_latitude for i in range(1, 6)]
next_longitudes = [last_longitude + i * delta_longitude for i in range(1, 6)]

# Plot the next five possible GPS coordinates
plt.scatter(df['Longitude'], df['Latitude'], color='red', alpha=0.7, s=50)
plt.scatter(next_longitudes, next_latitudes, color='blue', alpha=0.7, s=50)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Estimated Route of Tracked Whale')
plt.legend(['Known Coordinates', 'Next 5 Possible Coordinates'])
plt.show()
