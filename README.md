# Database Instructions

`docker pull mysql:latest`

`docker run --name cmpe281-mysql -e MYSQL_ROOT_PASSWORD=cmpe-281 -v "cmpe281-mysql-data:<path of local folder>" -d mysql`

docker run --name cmpe281-mysql -e MYSQL_ROOT_PASSWORD=cmpe-281 -p 3307:3306 -v "cmpe281-mysql-data:/Users/sahusnulu/Code/SJSU \Courses/CMPE-281/Projects/Project/mySQL" -d mysql

connect through IDE or install mysql and connect with

`mysql --host=127.0.0.1 --port=3307 -u root -p`

You can then run the commands in createTables.sql.


To local host, install the following:

`pip install "uvicorn[standard]"`

Then run the following command in the app directory:

`uvicorn main:app --reload`


