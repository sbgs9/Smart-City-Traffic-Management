import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/", username='user', password='cmpe-281')
db = client["smartCity"]
iotAnalytics = db["iotAnalytics"]
cameraImage = db["cameraImage"]

for i in iotAnalytics.find():
    print(i)
for i in cameraImage.find():
    print(i)