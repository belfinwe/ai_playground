import geopandas as gpd
from shapely.geometry import Point

# Create a GeoDataFrame to store tracking data
coordinates = [(40.7128, -74.0060), (40.7125, -74.0062)]
geometry = [Point(xy) for xy in coordinates]
tracking_data = gpd.GeoDataFrame(columns=['Timestamp', 'Depth', 'Speed'], geometry=geometry)

# Set the CRS (Coordinate Reference System) for the data
tracking_data.crs = 'EPSG:4326'  # Assuming WGS84 coordinate system

# Add data points to the GeoDataFrame
tracking_data.loc[0] = ['2023-06-17 10:00:00', 100, 5.7]
tracking_data.loc[1] = ['2023-06-17 10:01:00', 105, 6.2]
# ... add more data points

# Print the GeoDataFrame
print(tracking_data)
