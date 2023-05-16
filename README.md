# Data Representation Module Project 
---
### Description:
A program that demonstrates creating and consuming RESTful APIs using Flask. The application should link to one or more MySQL databases, and web pages should be created that can consume the API, performing CRUD operations on the data.
- HTML
- JavaScript
- Python
- Flask 
- MySQL 
- Ajax

## Requirements/how to run:
pip command must be used to install MySQL connector: 
```python 
pip install mysql-connector-python
```
import using:  
```python 
import mysql-connector
```
1.Get a MySQL database running.<br>
2.You can copy the relevant files, or clone the repository and run it on your own machine.<br>
3.Type 'python myServer.py' on you command line and copy and paste the localhost web address provided. ('http://127.0.0.1:5000' for example) and click enter.<br>
4.Add on the API (Application Program Interface) endpoints contained in the templates folder to the localhost adress e.g. 'myMenuViewer.html' and click refresh to interact with the menu. 
<br>
**Set up a virtual environment** (windows command prompt or cmder)
Create the virtual environment:
```python
python3 -m venv virtualenvironmentname
```
Run the virtual environment from windows:
```python
.\venv\scrips\activate.bat
```
Show the packages:
```python
pip freeze
```
```python
pip install flask
```
Save packages to a file:
```python
pip freeze > requirements.txt
```
Shows the packages and their versions:
```python
cat requirements.txt
```
### Further information:
Connect using the **'.connect()'** method of the MySQL Connector class. On successful connection, it returns a **'MySQLConnection'** object.<br>
**'host'**, **'username'**, **'password'** and **'database'** must be provided. (If username is 'root', no password is needed).
<br>
Use the **'.cursor()'** method on the MySQLConnection object to enable the user to do SQL operations on the data.
Use **'fetchall()'**, **'fetchmany()'** or **'fetchone()'** to read the query results.
CRUD operations (create, read, update, delete) can be performed on the data.
Use **'cursor.close()'** and **'connection.close()'** methods to close open connections after you're done.
<br>
One can download Wampserver, and open the MySQL console to create a database there and connect to it using Python or, provided you have successfully established a connection to MySQL; a database can be created using Python code and then tables can be created inside the database to store information.
<br>
Flask is used to manipulate HTML templates using different 'routes', i.e. **'@app.route()'** in 'myserver.py' file.


                        
