import json
import urllib.request
import main
import models

with urllib.request.urlopen('https://cwwp2.dot.ca.gov/data/d4/cctv/cctvStatusD04.json') as url:
    camera_data = json.load(url)
    print('Adding camera images')
    for cctv in camera_data['data']:
        timestamp = cctv['cctv']['recordTimestamp']['recordDate'] + " " + cctv['cctv']['recordTimestamp']['recordTime']
        curr_data = models.Cameraimage(
            cameraId=cctv['cctv']['index'],
            timestamp=timestamp,
            url=cctv['cctv']['imageData']['static']['currentImageURL']
        )
        main.add_cameraimage(curr_data)
        print('Added camera image entry!')
