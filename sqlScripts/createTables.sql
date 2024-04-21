CREATE DATABASE IF NOT EXISTS smartCity;

CREATE TABLE IF NOT EXISTS smartCity.camera
(
    id INT unsigned NOT NULL,
    name VARCHAR(255) NOT NULL,
    latitude VARCHAR(255) NOT NULL,
    longitude VARCHAR(255) NOT NULL,
    inService BOOLEAN NOT NULL,
    streamingUrl VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS smartCity.iotStation
(
    id INT unsigned NOT NULL,
    name VARCHAR(255) NOT NULL,
    latitude VARCHAR(255) NOT NULL,
    longitude VARCHAR(255) NOT NULL,
    stationType VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS smartCity.serviceRequest
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    date VARCHAR(225) NOT NULL,
    service VARCHAR(225) NOT NULL,
    description VARCHAR(225) NOT NULL,
    deviceType VARCHAR(225) NOT NULL,
    deviceId INT unsigned NOT NULL
);

