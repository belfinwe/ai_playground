import pandas as pd
import random

# Create a dataframe to store tracking data
# tracking_data = pd.DataFrame(columns=['Timestamp', 'Latitude', 'Longitude', 'Depth', 'Speed'])

# Generate test data
num_items = random.randint(20, 50)  # Random number of items between 20 and 50
tmp_list = list()

for _ in range(num_items):
    timestamp = pd.Timestamp.now()  # Current timestamp
    latitude = random.uniform(-90, 90)  # Random latitude between -90 and 90
    longitude = random.uniform(-180, 180)  # Random longitude between -180 and 180
    depth = random.uniform(0, 1000)  # Random depth between 0 and 1000
    speed = random.uniform(0, 10)  # Random speed between 0 and 10
    
    tmp_dict = {
        'Timestamp': timestamp,
        'Latitude': latitude,
        'Longitude': longitude,
        'Depth': depth,
        'Speed': speed
    }

    # tracking_data = tracking_data.append(, ignore_index=True)
    # tracking_data.loc[len(tracking_data)] = tmp_dict
    tmp_list.append(tmp_dict)

tracking_data = pd.DataFrame(tmp_list, columns=['Timestamp', 'Latitude', 'Longitude', 'Depth', 'Speed'])

# Print the dataframe
print(tracking_data)
