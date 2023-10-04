import json
import csv
import os
import pyproj

# Set some variables
limit = 1000000

def get_filter_params(filters, index):
    try:
        filter = filters[index]['parameter']
        return filter.get('ts_mean', ''), filter.get('ts15_slope1', ''), filter.get('ts25_slope1', '')
    except IndexError:
        return '', '', ''

# Load the file
with open('water-points.json') as f:
    data = json.load(f)

# Open a csv file for writing
with open('water-points.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header row
    header = ['well_id', 'latitude', 'longitude', 'maaiveld_nap']
    header += [f'filter_{i}_gemiddeld' for i in range(1, 6)]
    header += [f'filter_{i}_trend_15_jaar' for i in range(1, 6)]
    header += [f'filter_{i}_trend_25_jaar' for i in range(1, 6)]
    csv_writer.writerow(header)

    # Get the features
    features = data.get('features', [])
    if not features:
        print('No features found')
        exit()

    # Loop through the data and write each row to the csv file
    for index, item in enumerate(features):
        if index < limit:
            item_filters = item['properties'].get('screens', [])
            well_id = item['properties'].get('wellid', '')
            maaiveld_nap = item['properties'].get('slvl', '')

            filter_params = [get_filter_params(item_filters, i) for i in range(5)]

            # Set up a pyproj transformer from Rijkswaterstaat coordinates to WGS84
            transformer = pyproj.Transformer.from_crs(28992, 4326, always_xy=True)
            # Transform the coordinates
            longitude, latitude = transformer.transform(item['geometry']['coordinates'][0], item['geometry']['coordinates'][1])

            # Write the row to the csv file
            row = [well_id, latitude, longitude, maaiveld_nap]
            row += [param for params in filter_params for param in params]
            csv_writer.writerow(row)
