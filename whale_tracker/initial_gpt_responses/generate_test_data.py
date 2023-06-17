"""
import random
import csv
import pandas as pd


columns = ['Timestamp', 'Latitude', 'Longitude', 'Depth', 'Speed']

# Generate test data
num_items = random.randint(50, 70)  # Random number of items between 20 and 50
tmp_list = list()

with open("whale_tracker_test_data.csv", "w") as data_file:
    # csv_writer = csv.writer(data_file, delimiter=",")
    csv_writer = csv.DictWriter(data_file, fieldnames=columns)
    csv_writer.writeheader()

    for _ in range(num_items):
        timestamp = pd.Timestamp.now()  # Current timestamp
        latitude = random.uniform(-90, 90)  # Random latitude between -90 and 90
        longitude = random.uniform(-180, 180)  # Random longitude between -180 and 180
        depth = random.uniform(0, 1000)  # Random depth between 0 and 1000
        speed = random.uniform(0, 10)  # Random speed between 0 and 10
        
        tmp_list = [timestamp, latitude, longitude, depth, speed]
        # data_file.write(f"{timestamp},{latitude},{longitude},{depth},{speed}\n")

        
        tmp_dict = {
            'Timestamp': timestamp,
            'Latitude': latitude,
            'Longitude': longitude,
            'Depth': depth,
            'Speed': speed
        }
        '''
        # tracking_data = tracking_data.append(, ignore_index=True)
        # tracking_data.loc[len(tracking_data)] = tmp_dict
        tmp_list.append(tmp_dict)
        '''

        csv_writer.writerow(tmp_dict)
        print(tmp_dict)
"""
import pandas as pd

# Generate test data
timestamps = pd.date_range(start='2023-06-01', periods=20, freq='H')
latitudes = [58.0, 58.2, 58.4, 58.6, 58.8, 59.0, 59.2, 59.4, 59.6, 59.8, 60.0, 60.2, 60.4, 60.6, 60.8, 61.0, 61.2, 61.4, 61.6, 61.8]
longitudes = [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5]
depths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
speeds = [2.5, 3.0, 2.8, 2.7, 3.2, 2.9, 2.6, 2.8, 2.7, 2.5, 2.4, 2.3, 2.1, 2.0, 2.2, 2.4, 2.6, 2.8, 2.9, 3.0]

# Create a DataFrame
data = {'Timestamp': timestamps,
        'Latitude': latitudes,
        'Longitude': longitudes,
        'Depth': depths,
        'Speed': speeds}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('tracking_data.csv', index=False)
