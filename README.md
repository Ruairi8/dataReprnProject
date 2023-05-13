# Data Representation Module Project 
---
### Description:
A program that demonstrates creating and consuming RESTful APIs using Flask. The application should link to one or more MySQL databases, and web pages should be created that can consume the API, performing CRUD operations on the data.
- HTML
- CSS
- Python
- Flask 
- MySQL 

pip command must be used to install MySQL connector: 
```python 
pip install mysql-connector-python
```
import using:  
```python 
import mysql-connector
```

Connect using the <mark>".connect()"</mark> method of the MySQL Connector class. On successful connection, it returns a <mark>"MySQLConnection"<mark> object.
  <mark>"host"</mark>, <mark>"username"</mark>, <mark>"password"</mark> and <mark>"database"</mark> must be provided. (If username is 'root', no password is needed).
Use the ".cursor()" method on the MySQLConnection object to enable the user to do SQL operations on the data.
Use "fetchall()", "fetchmany()" or "fetchone()" to read the query results.
CRUD operations (create, read, update, delete) can be performed on the data.
Use "cursor.close()" and "connection.close()" methods to close open connections after you're done.

One can download Wampserver, and open the MySQL console to create a database there and connect to it using Python or a database can be created using Python code and then tables can be created inside the database to store information.

Flask is used to manipulate HTML templates using different 'routes', i.e. <mark>'@app.route()'</marl> in 'myserver.py' file.
