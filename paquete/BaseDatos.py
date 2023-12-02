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
def iniciar():
    conn =mysqlconnect()
    cur = conn.cursor()
    cur.execute('select @@version')
    cur.execute('''CREATE DATABASE IF NOT EXISTS Miguel_Roberto ;''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS profesores
            (
            id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
            dni VARCHAR(9) UNIQUE NOT NULL,
            nombre VARCHAR(25) NOT NULL,
            direccion VARCHAR(25) NOT NULL
            );
            ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS cursos
            (
            id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(25) UNIQUE NOT NULL,
            descripcion VARCHAR(25) NOT NULL,
            id_profesor integer ,
            id_alumno_curso integer,
            FOREIGN KEY (id_profesor) REFERENCES profesores (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
            );
            ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS alumnos
            (
            id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(25) NOT NULL,
            apellidos VARCHAR(25) NOT NULL,
            telefono VARCHAR(25) NOT NULL,
            direccion VARCHAR(25) NOT NULL,
            f_nacimiento VARCHAR(25) NOT NULL,
            UNIQUE (nombre,apellidos)
            
            );
            ''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS alumno_curso
            (
            id_curso integer NOT NULL ,
            id_alumno integer NOT NULL ,
            PRIMARY KEY(id_curso,id_alumno),
            FOREIGN KEY (id_alumno) REFERENCES alumnos (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            FOREIGN KEY (id_curso) REFERENCES cursos (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
            );
            ''')
    cur.execute('''ALTER TABLE alumno_curso 
            ADD 
            ;
            ''')
    conn.commit()
    return 0

conn =mysqlconnect()
cur = conn.cursor()
cur.execute('USE Miguel_Roberto')





