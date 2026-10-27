# Creating a tuple for geographic coordinates (latitude, longitude)
gps_coordinates = (40.7128, -74.0060)

# Accessing items works just like lists
print(gps_coordinates[0])  # Output: 40.7128

# Trying to change an item will cause an error!
print(type(gps_coordinates))

x, y = gps_coordinates
print(f"Latitude: {x}, Longitude: {y}")

# tuples with one item need a trailing comma
single_item_tuple = (42,)
# no new line at end of file
