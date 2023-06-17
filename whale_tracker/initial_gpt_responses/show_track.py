import pandas as pd
import matplotlib.pyplot as plt

# Read the tracking data from a CSV file into a pandas DataFrame
# df = pd.read_csv('whale_tracker_test_data.csv')  # Replace 'tracking_data.csv' with your actual file name or data source
df = pd.read_csv('tracking_data.csv')  # Replace 'tracking_data.csv' with your actual file name or data source
print(df)

# Calculate distance between consecutive points
df['Distance'] = ((df['Latitude'].diff())**2 + (df['Longitude'].diff())**2)**0.5

# Plot the estimated route on a scatter plot
plt.scatter(df['Longitude'], df['Latitude'], color='red', alpha=0.7, s=50)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Estimated Route of Tracked Whale')
plt.show()

# Analyze the trajectory
total_distance = df['Distance'].sum()
avg_speed = total_distance / df['Timestamp'].nunique()
max_speed = df['Speed'].max()
# Perform other analysis as needed

# Print summary statistics
print("Total Distance Traveled: {:.2f} units".format(total_distance))
print("Average Speed: {:.2f} units per timestamp".format(avg_speed))
print("Maximum Speed: {:.2f} units per timestamp".format(max_speed))
# Print other analysis results as needed
