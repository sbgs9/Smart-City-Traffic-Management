from datetime import date, timedelta

import pems_api as pa
import pandas as pd
import main
import models

# Login to http://pems.dot.ca.gov
pa.PeMSConnection.initialize("satyabhaskaraganesh.susarla@sjsu.edu", "s@3E^funkw")

# Initializing a data handler
station_data_handler = pa.Station5MinDataHandler()
chp_data_handler = pa.CHPDailyIncidentDataHandler()

# Defining a start date, end date and a district_id
start_date, end_date, district_id = date.today() - timedelta(days=7), date.today() - timedelta(days=1), 4

# Downloading data between start date and end date from the 3rd district
# data_chunks = data_handler.load_between(from_date=start_date, to_date=end_date, district=district_id)
data_chunks = station_data_handler.load_between(from_date=start_date, to_date=end_date, district=district_id)
data_chunks_chp = chp_data_handler.load_between(from_date=start_date, to_date=end_date, district=district_id)

station_df = []
chp_df = []

for data in data_chunks:
    station_df.append(data)
station_df = pd.concat(station_df)

for data in data_chunks_chp:
    chp_df.append(data)
chp_df = pd.concat(chp_df)

chp_data = chp_df.to_dict(orient='records')


# for record in chp_data:
#     print(record['timestamp'].to_pydatetime().date())

def get_incidents_by_timestamp(timestamp):
    num_incidents = 0
    for record in chp_data:
        if record['timestamp'].to_pydatetime().date() == timestamp.to_pydatetime().date():
            num_incidents += 1
    return num_incidents


subset_df = station_df[['station_id', 'timestamp', 'total_flow', 'avg_occupancy', 'avg_speed']]
data = subset_df.to_dict(orient='records')
print('Adding to database!')
for record in data:
    curr_data = models.Iotanalytics(
        iotId=record['station_id'],
        timestamp=str(record['timestamp']),
        totalFlow=record['total_flow'],
        avgOccupancy=record['avg_occupancy'],
        avgSpeed=record['avg_speed'],
        incidents=get_incidents_by_timestamp(record['timestamp'])
    )
    main.add_iotanalytics(curr_data)
    print('Added entry!')
print('Finished adding to database!')

# subset_4000_df = subset_df.loc[subset_df['station_id'] == 400000]
# print(subset_4000_df.to_dict(orient='records'))
