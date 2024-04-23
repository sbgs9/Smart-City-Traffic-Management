# Database Instructions

## MySQL Setup

Set up MySQL through Docker. First download the latest MySQL Docker image.

```
docker pull mysql:latest
```

Then create the container with the following command:

```
docker run --name cmpe281-mysql -e MYSQL_ROOT_PASSWORD=cmpe-281 -p 3306:3306 -v "cmpe281-mysql-data:<path of local folder>" -d mysql
```

After that, connect through IDE or install mysql and connect with:

```
mysql --host=127.0.0.1 --port=3307 -u root -p
```

For sample data, you can run the commands `createTables.sql` and `populateTable.sql` in sqlScripts.

## MongoDB Setup

We will also be setting up MongoDB through Docker. First download the latest MongoDB Docker image:

```
docker pull mongodb/mongodb-community-server:latest
```

Then create the container with the following:

```
docker run --name cmpe281-mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=user -e MONGO_INITDB_ROOT_PASSWORD=cmpe-281 -v "mongodb-data:<path of local folder>" -d mongodb/mongodb-community-server:latest
```

For sample data, run the files in mongoDBScripts in order of `insert.py`, `get.py`, and if you want to delete the collections run `dropCollections.py`

## API Server

Make sure you are in the overarching `Project` directory.

Build the Docker container with the following command:

```
docker build -t smartcity .
```

Run the following command to start the container (make sure you put your IP address of your computer):

```
docker run -d --name smartcity -p 8000:8000 -e HOST_IP=<your-host-ip> smartcity
```



