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
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    latitude VARCHAR(255) NOT NULL,
    longitude VARCHAR(255) NOT NULL,
    stationType VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);