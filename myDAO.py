import mysql.connector
import dbConfigTemplate as cfg

class YourDAO:
    connection = ''
    cursor =     ''
    host =       ''
    user =       ''
    password =   ''
    database =   ''
    
    def __init__(self):
        self.host =     cfg.mysql['host']
        self.user =     cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host =      self.host,
            user =      self.user,
            password =  self.password,
            database =  self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()


    def order_food(self,foodname):   
            cursor = self.getcursor()
            sql = "select Dish from Menu where Dish like %s"
            values = (foodname, )
            cursor.execute(sql, values)
            result = cursor.fetchall()
            self.closeAll()
            return result


    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from Menu where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue    


    def convertToDictionary(self, result):
        columns = ['id','name','category', 'price']
        item = {}
        if result:
            for num, name in enumerate(columns):
                value = result[num]
                item[name] = value
        return item   


    def create(self, values):
       cursor = self.getcursor()
       sql="insert into Menu (Category,Dish,Price) values (%s,%s,%d)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       self.closeAll()
       return newid

        
    def select_dish(self,name):
        cursor = self.getcursor()
        sql="select Dish as order AND id as id from Menu where Dish like %s"
        values = (name, )
        cursor.execute(sql, values)
        result = cursor.fetchall()        
        self.closeAll()
        return result
       

    def convertToDictionary(self, result):
        pass
    '''
        colnames=['id','name','category', "price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
       '''

    def createtable(self):
        cursor = self.getcursor()
        sql = "CREATE TABLE Menu (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, Category varchar(50), Dish varchar(50), Price int)"
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()


    def createdatabase(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password   
        )
        self.cursor = self.connection.cursor()
        sql = "CREATE DATABASE "+ self.database
        self.cursor.execute(sql)
        self.connection.commit()
        self.closeAll()
        

class_instance = YourDAO()
class_instance.createdatabase()
class_instance.createtable()
class_instance.order_food("Lamb Balti, Boiled Rice")

