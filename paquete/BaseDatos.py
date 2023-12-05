import pymysql
import configparser 



'''
Created on 1 dic 2023

@author: Miguel_Gonzalez y Roberto_Castilla
'''
def iniciarFicheroConfiguracion():
    config = configparser.ConfigParser()
    config['SERVER'] = {'host': 'localhost',
                         'user': 'root',
                         'password': 'my-secret-pw',
                         'port':'3306'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    return 0

def checkFileExistance(filePath):
    try:
        with open(filePath, "r") as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def conectarse():
    cur = conn.cursor()
    cur.execute('USE Miguel_Roberto')
    return cur
def deconectarse(conn):
    conn.commit()
    conn.close()

    return 0
def mysqlconnect():
    config = configparser.ConfigParser()
    config.read('config.ini')
    host_variable=str(config['SERVER']['host'])
    user_variable=str(config['SERVER']['user'])
    password_variable=str(config['SERVER']['password'])
    port_variable=int(config['SERVER']['port'])
    conn=pymysql.connect(
        host=host_variable,
        user=user_variable,
        password=password_variable,
        port=port_variable
        )
    
    return conn
def iniciar():
    if(checkFileExistance("config.ini")==False):
        iniciarFicheroConfiguracion()
    conn =mysqlconnect()
    cur = conn.cursor()
    cur.execute('select @@version')
    cur.execute('''CREATE DATABASE IF NOT EXISTS miguel_roberto ;''')
    cur.execute('USE Miguel_Roberto')
    
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
    
    conn.commit()
    cur.close()
    return 0
def alta(tabla,campo1,campo2,campo3,campo4,campo5):
    cur=conectarse()
    if(tabla=='cursos'):
        print('Se supone que esto es un curso')
        cur.execute('''INSERT INTO cursos(nombre,descripcion)
            VALUES(' '''+str(campo1)+''' ',' '''+str(campo2)+''' '
            );''')
        conn.commit()
    elif(tabla=='profesores'):
        print('Se supone que esto es un profesor')
        cur.execute('''INSERT INTO profesores(dni,nombre,direccion,telefono)
            VALUES(' '''+str(campo1)+''' ',' '''+str(campo2)+''' ',' '''+str(campo3)+''',' '''+str(campo4)+''' '
            );''')
        conn.commit()
    elif(tabla=='alumnos'):
        print('Se supone que esto es un alumno')
        cur.execute('''INSERT INTO alumnos(nombre,apellidos,telefono,direccion,f_nacimiento)
            VALUES(' '''+str(campo1)+''' ',' '''+str(campo2)+''' ',' '''+str(campo3)+''' ',' '''+str(campo4)+''' ',' '''+str(campo5)+''' '
            );''')
        conn.commit()
    
    cur.close()
    return 0
def baja(tabla,campo1,campo2):
    cur=conectarse()
    if(tabla=='cursos'):
        print('Se supone que esto es un curso')
        cur.execute('''DELETE FROM cursos
            WHERE nombre = ' '''+str(campo1)+''' '
            ;''')
    elif(tabla=='profesores'):
        print('Se supone que esto es un profesor')
        cur.execute('''DELETE FROM profesores
            WHERE dni = ' '''+str(campo1)+''' '
            ;''')
    elif(tabla=='alumnos'):
        print('Se supone que esto es un alumno')
        cur.execute('''DELETE FROM alumnos
            WHERE nombre = ' '''+str(campo1)+''' ' AND apellidos= ' '''+str(campo2)+''' ' 
            ;''')
    conn.commit()
    cur.close()
    return 0
def modificar(tabla,idValor,campoMod,valorNew):
    cur=conectarse()
    if(tabla=='cursos'):
        print('Se supone que esto es un curso')
        cur.execute('''ALTER TABLE cursos SET '''+str(campoMod)+''' = ' '''+str(valorNew)+''' ' WHERE id= ' '''+str(idValor)+''' ' 
        ;''')
    elif(tabla=='profesores'):
        print('Se supone que esto es un profesor')
        cur.execute('''ALTER TABLE profesores SET '''+str(campoMod)+''' = ' '''+str(valorNew)+''' ' WHERE id= ' '''+str(idValor)+''' ' 
        ;''')
    elif(tabla=='alumnos'):
        print('Se supone que esto es un alumno')
        cur.execute('''ALTER TABLE alumnos SET '''+str(campoMod)+''' = ' '''+str(valorNew)+''' ' WHERE id= ' '''+str(idValor)+''' ' 
        ;''')
    conn.commit()
    cur.close()
    return 0
def buscar(tabla,campo1,campo2):
    cur=conectarse()
    if(tabla=='cursos'):
        print('Se supone que esto es un curso')
        cur.execute('''SELECT * FROM cursos
            WHERE nombre = ' '''+str(campo1)+''' '
            ;''')
    elif(tabla=='profesores'):
        print('Se supone que esto es un profesor')
        cur.execute('''SELECT * FROM profesores
            WHERE dni = ' '''+str(campo1)+''' '
            ;''')
    elif(tabla=='alumnos'):
        print('Se supone que esto es un alumno')
        cur.execute('''SELECT * FROM alumnos
            WHERE nombre = ' '''+str(campo1)+''' ' AND apellidos= ' '''+str(campo2)+''' ' 
            ;''')
    out=cur.fetchall();
    lista=list(out)
    if( len(lista)==0):
        print(tabla+' : '+campo1+' '+campo2+' no ha sido encontrado')
        return None
    else:
        for x in lista:
            print(x)
        return lista
    conn.commit()
    cur.close()
    return None
def mostrarTodos(tabla):
    cur=conectarse()
    if(tabla=='cursos'):
        print('Se supone que esto es un curso')
        cur.execute('''SELECT cursos.* FROM cursos ;''')
    elif(tabla=='profesores'):
        print('Se supone que esto es un profesor')
        cur.execute('''SELECT profesores.* FROM profesores ;''')
    elif(tabla=='alumnos'):
        print('Se supone que esto es un alumno')
        cur.execute('''SELECT alumnos.* FROM alumnos ;''')
    out=cur.fetchall();
    lista=list(out)
    if(len(lista)==0):
        print('La tabla '+tabla+' esta vacia')
    else:
        for x in lista:
            print(x)
    conn.commit()
    cur.close()
    return 0
def matricularAlumno(idAlumno,idCurso):
    cur=conectarse()
    cur.execute('''INSERT INTO alumno_curso(id_curso,id_alumno)
            VALUES(' '''+str(idCurso)+''' ',' '''+str(idAlumno)+''' '
            );''')
    conn.commit()
    cur.close()
    return 0
def desmatricularAlumno(idAlumno,idCurso):
    cur=conectarse()
    cur.execute('''DELETE FROM alumno_curso
            WHERE id_alumno = ' '''+str(idAlumno)+''' ' AND id_curso= ' '''+str(idCurso)+''' ' 
            ;''')
    conn.commit()
    cur.close()
    return 0
conn='';



