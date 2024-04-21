# Database Instructions

## MySQL Setup

Set up MySQL through Docker. First download the latest MySQL Docker image.

```
docker pull mysql:latest
```

Then create the container with the following command:

```
docker run --name cmpe281-mysql -e MYSQL_ROOT_PASSWORD=cmpe-281 -p 3307:3306 -v "cmpe281-mysql-data:<path of local folder>" -d mysql
```

After that, connect through IDE or install mysql and connect with:

```
mysql --host=127.0.0.1 --port=3307 -u root -p
```

Then install this package:

```
pip install mysqlclient
```

For sample data, you can run the commands createTables.sql and populateTable.sql in sqlScripts.

## MongoDB Setup

We will also be setting up MongoDB through Docker. First download the latest MongoDB Docker image:

```
docker pull mongodb/mongodb-community-server:latest
```

Then create the container with the following:

```
docker run --name cmpe281-mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=user -e MONGO_INITDB_ROOT_PASSWORD=cmpe-281 -v "mongodb-data:<path of local folder>" -d mongodb/mongodb-community-server:latest
```

Please download the following import:

```
pip install pymongo
```

For sample data, run the files in mongoDBScripts in order of insert.py, get.py, and if you want to delete the collections run dropCollections.py

## Host APIs
To host the api's locally, install the following:

```
pip install "uvicorn[standard]"
pip install fastapi
```

Then run the following command in the app directory:

```
uvicorn main:app --reload
```



