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