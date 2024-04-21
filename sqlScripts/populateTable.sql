
INSERT INTO smartCity.camera (id, name, latitude, longitude, inService, streamingUrl) VALUES
(1, 'TVC74 -- US-101 : North 1st Street Loop Onramp', '37.372054', '-121.916917', TRUE, 'https:\/\/wzmedia.dot.ca.gov\/D4\/N101_at_N_1st_St.stream\/playlist.m3u8'),
(2, 'TVC55 -- I-880 : The Alameda', '37.34504', '-121.92384', TRUE, 'https:\/\/wzmedia.dot.ca.gov\/D4\/S880_JNO_The_Alameda.stream\/playlist.m3u8'),
(3, 'TVC83 -- SR-87 : Capitol Expressway', '37.274115', '-121.863716', TRUE, NULL);

INSERT INTO smartCity.iotStation (id, name, latitude, longitude, stationType) VALUES
(402294, '4A5324 Loc 1', '37.372054', '-121.916917', 'ML'),
(409869, 'N of Old Monterey Rd UC', '37.34504', '-121.92384', 'ML'),
(409875, 'SR 25 off', '37.274115', '-121.863716', 'FR');

INSERT INTO smartCity.serviceRequest (date, service, description, deviceType, deviceId) VALUES
('2023-04-21', 'Camera Maintenance', 'Clean camera lens', 'camera', 1),
('2023-04-20', 'IoT Station Repair', 'Replace faulty sensor', 'iotStation', 402294),
('2023-04-19', 'Camera Upgrade', 'Install new camera firmware', 'camera', 2),
('2023-04-18', 'IoT Station Inspection', 'Routine maintenance check', 'iotStation', 409869);
