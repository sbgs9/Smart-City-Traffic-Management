from datetime import date, timedelta

import pems_api as pa
import pandas as pd
import main
import models

# Login to http://pems.dot.ca.gov
pa.PeMSConnection.initialize("satyabhaskaraganesh.susarla@sjsu.edu", "s@3E^funkw")

# Initializing a data handler
station_data_handler = pa.StationMetaDataHandler()

# Defining a start date, end date and a district_id
start_date, end_date, district_id = date.today() - timedelta(days=1), date.today() - timedelta(days=1), 4

# Downloading data between start date and end date from the 3rd district
data_chunks = station_data_handler.load_between(from_date=start_date, to_date=end_date, district=district_id)

station_df = []

for data in data_chunks:
    station_df.append(data)
station_df = pd.concat(station_df)

subset_df = station_df[['id', 'name', 'latitude', 'longitude', 'type']]
data = subset_df.to_dict(orient='records')

print('Adding to database!')
for record in data:
    iot_stations = main.get_iotstation_list()
    curr_data = models.Iotstation(
        id=record['id'],
        name=str(record['name']),
        latitude=str(record['latitude']),
        longitude=str(record['longitude']),
        stationType=str(record['type'])
    )
    if curr_data not in iot_stations:
        main.add_iotstation(curr_data)
    print('Added station!')
print('Finished adding to database!')