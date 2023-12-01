
import pymysql



'''
Created on 1 dic 2023

@author: Miguel_Gonzalez y Roberto_Castilla
'''


def mysqlconnect():
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        #db=' Database',
        port=3307
        )
    
    return conn
conn =mysqlconnect()
cur = conn.cursor()
cur.execute('select @@version')
cur.execute('''CREATE DATABSE IF NOT EXISTS Miguel_Roberto ;''')
cur.execute('''CREATE TABLE IF NOT EXISTS profesores
         (ID int NOT NULL PRIMARY KEY,
         Dni VARCHAR(9) NOT NULL,
         Nombre VARCHAR(25) NOT NULL,
         Direccion VARCHAR(25) NOT NULL,
         );

cur.execute('USE Miguel_Roberto')