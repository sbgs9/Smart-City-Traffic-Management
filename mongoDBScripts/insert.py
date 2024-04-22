import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/", username='user', password='cmpe-281')
db = client["smartCity"]

iotAnalytics = db["iotAnalytics"]

iotList = [
    {"iotId": 1, "timestamp": "22:18:47-2023-08-23", "totalFlow": 27.0, "avgOccupancy": 0.005, "avgSpeed": 70, "incidents": 147},
    {"iotId": 2, "timestamp": "22:18:47-2023-08-23", "totalFlow": 24.0, "avgOccupancy": 0.0001, "avgSpeed": 80, "incidents": 500},
    {"iotId": 3, "timestamp": "22:18:47-2023-08-23", "totalFlow": 22.0, "avgOccupancy": 0.04, "avgSpeed": 63, "incidents": 250},
    {"iotId": 4, "timestamp": "22:18:47-2023-08-23", "totalFlow": 18.0, "avgOccupancy": 0.1, "avgSpeed": 65, "incidents": 600}
]

iotInsert = iotAnalytics.insert_many(iotList)

cameraImage = db["cameraImage"]

cameraList = [
    {"cameraId": 1, "timestamp": "22:18:47-2023-08-23", "url": "https:\/\/cwwp2.dot.ca.gov\/data\/d4\/cctv\/image\/tvc60i880us101\/tvc60i880us101.jpg"},
    {"cameraId": 2, "timestamp": "20:15:40-2023-08-23", "url": "https:\/\/cwwp2.dot.ca.gov\/data\/d4\/cctv\/image\/tvc60i880us101\/tvc60i880us101.jpg"},
    {"cameraId": 3, "timestamp": "18:15:59-2023-08-23", "url": "https:\/\/cwwp2.dot.ca.gov\/data\/d4\/cctv\/image\/tvc60i880us101\/tvc60i880us101.jpg"},
    {"cameraId": 4, "timestamp": "16:15:22-2023-08-23", "url": None}
]

cameraInsert = cameraImage.insert_many(cameraList)
