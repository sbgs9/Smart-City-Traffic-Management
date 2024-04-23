import json
import urllib.request
import main
import models

with urllib.request.urlopen('https://cwwp2.dot.ca.gov/data/d4/cctv/cctvStatusD04.json') as url:
    camera_data = json.load(url)
    print('Adding cameras')
    for cctv in camera_data['data']:
        curr_data = models.Camera(
            id=cctv['cctv']['index'],
            name=cctv['cctv']['location']['locationName'],
            latitude=cctv['cctv']['location']['latitude'],
            longitude=cctv['cctv']['location']['longitude'],
            inService='true' if cctv['cctv']['inService'] == 'true' else 'false',
            streamingUrl=cctv['cctv']['imageData']['streamingVideoURL']
        )
        main.add_camera(curr_data)
        print('Added camera entry!')
