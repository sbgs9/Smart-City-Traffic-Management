# generated by fastapi-codegen:
#   filename:  smartCity.yaml
#   timestamp: 2024-04-21T21:49:43+00:00

from __future__ import annotations

import os
from typing import List, Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import (
    Camera,
    Cameraimage,
    ErrorModel,
    Iotanalytics,
    Iotstation,
    Servicerequest,
)

import MySQLdb
import pymongo

db_config = {
    'host': os.environ.get("HOST_IP"),
    'user': 'root',
    'passwd': 'cmpe-281',
    'db': 'smartCity',
    'port': 3306
}

conn = MySQLdb.connect(**db_config)

mongodbUrl = "mongodb://%s:27017/" % (os.environ.get("HOST_IP"))
client = pymongo.MongoClient(mongodbUrl, username='user', password='cmpe-281')
db = client["smartCity"]

iotAnalytics = db["iotAnalytics"]
cameraImage = db["cameraImage"]

app = FastAPI(
    version='1.0.0',
    title='CCTV Cameras',
    description='API for CCTV Cameras and IOT Stations',
    contact={'name': 'Sahus Nulu', 'email': 'sahus.nulu@sjsu.edu'},
)

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


@app.post(
    '/camera',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def add_camera(body: Camera) -> Union[None, ErrorModel]:
    cursor = conn.cursor()
    query = "INSERT INTO camera (id, name, latitude, longitude, inService, streamingUrl) VALUES (%s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (body.id, body.name, body.latitude, body.longitude, body.inService, body.streamingUrl))
    conn.commit()
    cursor.close()


@app.get(
    '/cameras',
    response_model=List[Camera],
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def get_camera_list() -> Union[List[Camera], ErrorModel]:
    cursor = conn.cursor()
    query = "SELECT * FROM camera;"
    cursor.execute(query)
    items = cursor.fetchall()
    cursor.close()

    if items is None:
        return ErrorModel(code=404, message="CCTVs not found")

    cameras = []
    for item in items:
        camera = Camera(
            id=item[0],
            name=item[1],
            latitude=item[2],
            longitude=item[3],
            inService=bool(item[4]),
            streamingUrl=item[5]
        )
        cameras.append(camera)

    return cameras


@app.get(
    '/camera/{id}',
    response_model=Camera,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def find_camera_byid(id: str) -> Union[Camera, ErrorModel]:
    cursor = conn.cursor()
    query = "SELECT * FROM camera WHERE id = %s;"
    cursor.execute(query, [id])
    item = cursor.fetchone()
    cursor.close()
    if item is None:
        return ErrorModel(code=404, message="CCTV not found")
    return Camera(id=item[0], name=item[1], latitude=item[2], longitude=item[3], inService=bool(item[4]),
                  streamingUrl=item[5])


@app.delete(
    '/camera/{id}',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def delete_camera(id: str) -> Union[None, ErrorModel]:
    cursor = conn.cursor()
    query = "DELETE FROM camera WHERE id=%s"
    cursor.execute(query, id)
    conn.commit()
    cursor.close()

@app.put(
    '/camera/{id}',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def update_camera(id: str, body: Camera = ...) -> Union[None, ErrorModel]:
    cursor = conn.cursor()
    query = "UPDATE camera SET name=%s, latitude=%s, longitude=%s, inService=%s, streamingUrl=%s WHERE id=%s"
    cursor.execute(query, (body.name, body.latitude, body.longitude, body.inService, body.streamingUrl, id))
    conn.commit()
    cursor.close()


@app.post(
    '/cameraimage',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def add_cameraimage(body: Cameraimage) -> Union[None, ErrorModel]:
    try:
        cameraImageData = body.dict()
        result = cameraImage.insert_one(cameraImageData)
        if not result.inserted_id:
            return ErrorModel(code=500, message="Failed to add Camera Image data")
    except Exception as e:
        return ErrorModel(code=500, message=str(e))


@app.get(
    '/cameraimage/{id}',
    response_model=Cameraimage,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def find_cameraimage_byid(id: str) -> Union[Cameraimage, ErrorModel]:
    cameraData = cameraImage.find_one({"cameraId": int(id)})
    if cameraData:
        cameraimage = Cameraimage(
            cameraId=cameraData['cameraId'],
            timestamp=cameraData['timestamp'],
            url=cameraData['url']
        )
        return cameraimage
    else:
        return ErrorModel(code=404, message="No Camera Image found")


@app.delete(
    '/cameraimage/{id}',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def delete_cameraimage(id: str) -> Union[None, ErrorModel]:
    """
    Deletes cameraimage by id
    """
    pass


@app.put(
    '/cameraimage/{id}',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def update_cameraimage(id: str, body: Cameraimage = ...) -> Union[None, ErrorModel]:
    """
    Updates cameraimage by id
    """
    pass


@app.get(
    '/cameraimages',
    response_model=List[Cameraimage],
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def get_cameraimage_list() -> Union[List[Cameraimage], ErrorModel]:
    cameraimages = []
    for i in cameraImage.find():
        cameraimage = Cameraimage(
            cameraId=i["cameraId"],
            timestamp=i["timestamp"],
            url=i["url"]
        )
        cameraimages.append(cameraimage)
    if not cameraimages:
        return ErrorModel(code=404, message="No Camera Images found")
    return cameraimages


@app.post(
    '/iotanalytics',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def add_iotanalytics(body: Iotanalytics) -> Union[None, ErrorModel]:
    try:
        iotData = body.dict()
        result = iotAnalytics.insert_one(iotData)
        if not result.inserted_id:
            return ErrorModel(code=500, message="Failed to add IoT analytics data")
    except Exception as e:
        return ErrorModel(code=500, message=str(e))


@app.get(
    '/iotanalytics/{id}',
    response_model=Iotanalytics,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def find_iotanalytics_byid(id: str) -> Union[Iotanalytics, ErrorModel]:
    data = iotAnalytics.find_one({"iotId": int(id)})
    if data is None:
        return ErrorModel(code=404, message="No IOT Analytics found")

    iot = Iotanalytics(
        iotId=data['iotId'],
        timestamp=data['timestamp'],
        totalFlow=data['totalFlow'],
        avgOccupancy=data['avgOccupancy'],
        avgSpeed=data['avgSpeed'],
        incidents=data['incidents']
    )

    return iot



@app.delete(
    '/iotanalytics/{id}',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def delete_iotanalytics(id: str) -> Union[None, ErrorModel]:
    """
    Deletes iotanalytics by id
    """
    pass


@app.put(
    '/iotanalytics/{id}',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def update_iotanalytics(id: str, body: Iotanalytics = ...) -> Union[None, ErrorModel]:
    try:
        iotData = body.dict(exclude_unset=True)
        result = iotAnalytics.update_one(
            {"_id": id},
            {"$set": iotData}
        )
    except Exception as e:
        return ErrorModel(code=500, message=str(e))


@app.get(
    '/iotanalyticss',
    response_model=List[Iotanalytics],
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def get_iotanalytics_list() -> Union[List[Iotanalytics], ErrorModel]:
    iotanalytics = []
    for i in iotAnalytics.find():
        iot = Iotanalytics(
            iotId=i["iotId"],
            timestamp=i["timestamp"],
            totalFlow=i["totalFlow"],
            avgOccupancy=i["avgOccupancy"],
            avgSpeed=i["avgSpeed"],
            incidents=i["incidents"]
        )
        iotanalytics.append(iot)

    if not iotanalytics:
        return ErrorModel(code=404, mesage="No IOT Analytics found")
    return iotanalytics


@app.post(
    '/iotstation',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def add_iotstation(body: Iotstation) -> Union[None, ErrorModel]:
    try:
        cursor = conn.cursor()
        query = "INSERT INTO iotStation (id, name, latitude, longitude, stationType) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (body.id, body.name, body.latitude, body.longitude, body.stationType))
        conn.commit()
        cursor.close()
    except Exception as e:
        return ErrorModel(code=500, message=str(e))


@app.get(
    '/iotstation/{id}',
    response_model=Iotstation,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def find_iotstation_byid(id: str) -> Union[Iotstation, ErrorModel]:
    cursor = conn.cursor()
    query = "SELECT * FROM iotStation WHERE id = %s;"
    cursor.execute(query, [id])
    item = cursor.fetchone()
    cursor.close()
    if item is None:
        return ErrorModel(code=404, message="IOT Station not found")
    return Iotstation(id=item[0], name=item[1], latitude=item[2], longitude=item[3], stationType=item[4])


@app.delete(
    '/iotstation/{id}',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def delete_iotstation(id: str) -> Union[None, ErrorModel]:
    """
    Deletes iotstation by id
    """
    pass


@app.put(
    '/iotstation/{id}',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def update_iotstation(id: str, body: Iotstation = ...) -> Union[None, ErrorModel]:
    """
    Updates iotstation by id
    """
    pass


@app.get(
    '/iotstations',
    response_model=List[Iotstation],
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def get_iotstation_list() -> Union[List[Iotstation], ErrorModel]:
    cursor = conn.cursor()
    query = "SELECT * FROM iotStation;"
    cursor.execute(query)
    items = cursor.fetchall()
    cursor.close()

    if items is None:
        return ErrorModel(code=404, message="IOT Stations not found")

    iotStations = []
    for item in items:
        iotStation = Iotstation(
            id=item[0], name=item[1], latitude=item[2], longitude=item[3], stationType=item[4]
        )
        iotStations.append(iotStation)

    return iotStations


@app.post(
    '/servicerequest',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def add_servicerequest(body: Servicerequest) -> Union[None, ErrorModel]:
    try:
        cursor = conn.cursor()
        query = "INSERT INTO serviceRequest (id, date, service, description, deviceType, deviceId) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (body.id, body.date, body.service, body.description, body.deviceType, body.deviceId))
        conn.commit()
        cursor.close()
    except Exception as e:
        return ErrorModel(code=500, message=str(e))


@app.get(
    '/servicerequest/{id}',
    response_model=Servicerequest,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def find_servicerequest_byid(id: str) -> Union[Servicerequest, ErrorModel]:
    cursor = conn.cursor()
    query = "SELECT * FROM serviceRequest WHERE id = %s;"
    cursor.execute(query, [id])
    item = cursor.fetchone()
    cursor.close()
    if item is None:
        return ErrorModel(code=404, message="Service Request not found")
    return Servicerequest(id=item[0],
                          date=item[1],
                          service=item[2],
                          description=item[3],
                          deviceType=item[4],
                          deviceId=item[5])


@app.delete(
    '/servicerequest/{id}',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def delete_servicerequest(id: str) -> Union[None, ErrorModel]:
    """
    Deletes servicerequest by id
    """
    pass


@app.put(
    '/servicerequest/{id}',
    response_model=None,
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '404': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def update_servicerequest(
        id: str, body: Servicerequest = ...
) -> Union[None, ErrorModel]:
    """
    Updates servicerequest by id
    """
    pass


@app.get(
    '/servicerequests',
    response_model=List[Servicerequest],
    responses={
        '400': {'model': ErrorModel},
        '401': {'model': ErrorModel},
        '500': {'model': ErrorModel},
    },
)
def get_servicerequest_list() -> Union[List[Servicerequest], ErrorModel]:
    cursor = conn.cursor()
    query = "SELECT * FROM serviceRequest;"
    cursor.execute(query)
    items = cursor.fetchall()
    cursor.close()

    if items is None:
        return ErrorModel(code=404, message="Service Requests not found")

    requests = []
    for item in items:
        servicerequest = Servicerequest(
            id=item[0],
            date=item[1],
            service=item[2],
            description=item[3],
            deviceType=item[4],
            deviceId=item[5]
        )
        requests.append(servicerequest)

    return requests
