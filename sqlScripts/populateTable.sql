
INSERT INTO smartCity.camera (id, name, latitude, longitude, inService, streamingUrl) VALUES
(1, 'TVC74 -- US-101 : North 1st Street Loop Onramp', '37.372054', '-121.916917', TRUE, 'https:\/\/wzmedia.dot.ca.gov\/D4\/N101_at_N_1st_St.stream\/playlist.m3u8'),
(2, 'TVC55 -- I-880 : The Alameda', '37.34504', '-121.92384', TRUE, 'https:\/\/wzmedia.dot.ca.gov\/D4\/S880_JNO_The_Alameda.stream\/playlist.m3u8'),
(3, 'TVC83 -- SR-87 : Capitol Expressway', '37.274115', '-121.863716', TRUE, NULL);

INSERT INTO smartCity.iotStation (id, name, location, stationType, sensorType, speedLimit) VALUES
(402294, '4A5324 Loc 1', 'US101-N', 'Mainline', 'magnetometers', 65),
(409869, 'N of Old Monterey Rd UC', 'US101-N', 'Mainline', 'Loop', 65),
(409875, 'SR 25 off', 'US101-N', 'Off Ramp', 'Loop', 65);