# Data Representation Module Project 
---
### Description:
A program that demonstrates creating and consuming RESTful APIs using Flask. The application should link to one or more MySQL databases, and web pages should be created that can consume the API, performing CRUD operations on the data.
- HTML
- CSS
- Python
- Flask 
- MySQL 

pip command must be used to install MySQL connector: "pip install mysql-connector-python"
import using:  "import mysql-connector"
connect using the ".connect()" method of the MySQL Connector class. On successful connection, it returns a "MySQLConnection" object
"host", "username", "password" and "database" must be provided. (If username is 'root', no password is needed).
use the ".cursor()" method on the MySQLConnection object to enable the user to do SQL operations on the data.
use "fetchall()", "fetchmany()" or "fetchone()" to read the query results.
CRUD operations (create, read, update, delete) can be performed on the data.
use "cursor.close()" and "connection.close()" methods to close open connections after you're done.

One can download Wampserver, and open the MySQL console to create a database there and connect to it using Python or a database can be created using Python code and then tables can be created inside the database to store information.

Flask is used to manipulate HTML templates using different 'routes', i.e. '@app.route()' in 'myserver.py' file.
