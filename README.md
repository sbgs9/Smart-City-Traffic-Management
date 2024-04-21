# Database Instructions

## MySQL Setup

Set up MySQL through Docker. First download the latest MySQL Docker image.

`docker pull mysql:latest`

Then create the container with the following command:

`docker run --name cmpe281-mysql -e MYSQL_ROOT_PASSWORD=cmpe-281 -p 3307:3306 -v "cmpe281-mysql-data:<path of local folder>" -d mysql`

After that, connect through IDE or install mysql and connect with:

`mysql --host=127.0.0.1 --port=3307 -u root -p`

You can then run the commands in createTables.sql and populateTable.sql.

## Host APIs
To host the api's locally, install the following:

`pip install "uvicorn[standard]"`
`pip install fastapi`
`pip install mysqlclient`

Then run the following command in the app directory:

`uvicorn main:app --reload`


