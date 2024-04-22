import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["smartCity"]
iotAnalytics = db["iotAnalytics"]
cameraImage = db["cameraImage"]

deleteIot = iotAnalytics.delete_many({})

print(deleteIot.deleted_count, " documents deleted from iotAnalytics")

deleteCamera = cameraImage.delete_many({})

print(deleteCamera.deleted_count, " document deleted from cameraImage")