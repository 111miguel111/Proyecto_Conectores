import pymysql
import configparser 
import sys


'''
Created on 1 dic 2023

@author: Miguel_Gonzalez y Roberto_Castilla
'''

def escanerNumerico():
    '''
    Metodo para escanear una cadena con solo numeros
    :return Si la cadena es valida devuelve la cadena, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 5 intentos
    intentos=0
    while(intentos<5):
        scan=input()
        #Se introduce la cadena y si solo hay letras se devuelve
        if(scan.isspace()==False and scan.isnumeric() and (scan=='1' or scan=='2') ):
            return scan
        intentos+=1
        print('Porfavor introduce numeros no decimales')
    print("Has superado el numero de intentos")
    return None
def iniciarFicheroConfiguracion():
    '''
    Funcion que se encarga de crear el fichero de configuracion con valores predeterminados
    '''
    config = configparser.ConfigParser()
    config['SERVER'] = {'host': 'localhost',
                         'user': 'root',
                         'password': 'my-secret-pw',
                         'port':'3306'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    return 0

def checkFileExistance(filePath):
    '''
    Comprueba que el fichero de configuracion existe
    :param filePath: El nombre del fichero
    '''
    
    try:
        with open(filePath, "r") as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
def checkConfigBien(filePath):
    '''
    Funcion encargada de comprobar que el fichero de configuracion esta completo y no tenga errores
    :param filePath: El nombre del fichero
    '''
    campo=''
    try:
        config = configparser.ConfigParser()
        config.read(filePath)
        campo='host'
        host_variable=str(config['SERVER']['host'])
        if(host_variable.isspace()):
            print("El campo "+campo+" no puede estar vacio")
            return False
        campo='user'
        user_variable=str(config['SERVER']['user'])
        if(user_variable.isspace()):
            print("El campo "+campo+" no puede estar vacio")
            return False
        campo='password'
        password_variable=str(config['SERVER']['password'])
        if(password_variable.isspace()):
            print("El campo "+campo+" no puede estar vacio")
            return False
        campo='port'
        port_variable=int(config['SERVER']['port'])
        if(str(port_variable).isspace()):
            print("El campo "+campo+" no puede estar vacio")
            return False
        return True
    except FileNotFoundError as e:
        print("El campo "+campo+" falta o esta mal")
        return False
    except IOError as e:
        return False

def conectarse():
    '''
    Funcion encargada de conectarse a la base de datos y devolver un cursor
    '''
    cur = conn.cursor()
    cur.execute('USE miguel_roberto')
    return cur
def deconectarse():
    '''
    Funcion encargada de desconectarse de la la base de datos y cerrar la conexion
    :param conn:
    '''
    conn.commit()
    conn.close()
    return 0
def mysqlconnect(): 
    '''
    Funcion encargada de realizar la conexion 
    '''
    
    try:
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
    except :
        salir=True
        while(salir):
            print("Hay un error en el fichero de configuracion que impiede conectarse \n1.Quieres restablecer el fichero con los valores por defecto \n2.Quieres cerrar el programa ")
            opcion=escanerNumerico()
            if (opcion=='1'):
                salir=False
                print("El fichero de configuracion sera restablecido")
                iniciarFicheroConfiguracion()
                print('Si quieres hacer cambios en la conexion mire el archivo de configuracion "config.ini" ')
                sys.exit()
            elif(opcion=='2'):
                salir=False
                print("El programa se cerrara")
                sys.exit()
            else:
                salir=True
                print("Valor no valido")
    
def iniciar():
    '''
    Funcion encargada de iniciar todo lo relacionado con la base de datos, la configuracion la conexion, crear las tablas etc
    '''
    if(checkFileExistance("config.ini")==True):
        if(checkConfigBien("config.ini")==False):
            salir=True
            while(salir):
                print("Hay un error en el fichero de configuracion \n1.Quieres restablecer el fichero con los valores por defecto \n2.Quieres cerrar el programa")
                opcion=escanerNumerico()
                if (opcion=='1'):
                    salir=False
                    print("El fichero de configuracion sera restablecido")
                    iniciarFicheroConfiguracion()
                    print('Si quieres hacer cambios en la conexion mire el archivo de configuracion "config.ini" ')
                    sys.exit()
                elif(opcion=='2'):
                    salir=False
                    print("El programa se cerrara")
                    sys.exit()
                else:
                    salir=True
                    print("Valor no valido")
    else:
        print("Se ha creado el fichero de configuracion")
        iniciarFicheroConfiguracion()
    
    mysqlconnect()
    
    conn =mysqlconnect()
    
    
    
    cur = conn.cursor()
    cur.execute('select @@version')
    cur.execute('''CREATE DATABASE IF NOT EXISTS miguel_roberto ;''')
    cur.execute('USE miguel_roberto')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS profesores
            (
            id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
            dni VARCHAR(9) UNIQUE NOT NULL,
            nombre VARCHAR(25) NOT NULL,
            direccion VARCHAR(25) NOT NULL,
            telefono VARCHAR(9) NOT NULL
            );
            ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS cursos
            (
            id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(25) UNIQUE NOT NULL,
            descripcion VARCHAR(25) NOT NULL,
            id_profesor integer ,
            CONSTRAINT FK_curso_profesor FOREIGN KEY (id_profesor) REFERENCES profesores(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
            );
            ''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS alumnos
            (
            id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(25) NOT NULL,
            apellidos VARCHAR(25) NOT NULL,
            telefono VARCHAR(11) NOT NULL,
            direccion VARCHAR(25) NOT NULL,
            f_nacimiento VARCHAR(10) NOT NULL,
            UNIQUE (nombre,apellidos)
            
            );
            ''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS alumno_curso
            (
            id_curso integer NOT NULL ,
            id_alumno integer NOT NULL ,
            PRIMARY KEY(id_curso,id_alumno),
            CONSTRAINT FK_alumno_curso_alumno FOREIGN KEY (id_alumno) REFERENCES alumnos (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            CONSTRAINT FK_alumno_curso_curso FOREIGN KEY (id_curso) REFERENCES cursos (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
            );
            ''')
    
    conn.commit()
    cur.close()
    return 0
def dropDataBase():
    '''
    Funcion que tira la base de datos ( pensado para facilitar el testear el codigo)
    '''
    cur=conectarse()
    cur.execute("DROP DATABASE miguel_roberto ;");
    conn.commit()
    return 0
def alta(tabla,campo1,campo2,campo3,campo4,campo5):
    '''
    Funcion encargada de la alta de cursos, profesores, alumnos
    :param tabla: En que tabla se van a insertar los datos
    :param campo1: El primer campo de cada tabla
    :param campo2: El segundo campo de cada tabla
    :param campo3: Si la tabla tiene un tercer campo, se pondra aqui(alumno, profesor)
    :param campo4: Si la tabla tiene un cuarto campo, se pondra aqui(alumno, profesor)
    :param campo5: Si la tabla tiene un quinto campo, se pondra aqui(alumno)
    '''
    cur=conectarse()
    if(tabla=='cursos'):
        print('Se supone que esto es un curso')
        cur.execute("INSERT INTO cursos(nombre,descripcion)VALUES('"+str(campo1)+"','"+str(campo2)+"');")
        conn.commit()
    elif(tabla=='profesores'):
        print('Se supone que esto es un profesor')
        cur.execute("INSERT INTO profesores(dni,nombre,direccion,telefono)VALUES('"+str(campo1)+"','"+str(campo2)+"','"+str(campo3)+"','"+str(campo4)+"');")
        conn.commit()
    elif(tabla=='alumnos'):
        print('Se supone que esto es un alumno')
        cur.execute("INSERT INTO alumnos(nombre,apellidos,telefono,direccion,f_nacimiento)VALUES('"+str(campo1)+"','"+str(campo2)+"','"+str(campo3)+"','"+str(campo4)+"','"+str(campo5)+"');")
        conn.commit()
    
    cur.close()
    return 0
def baja(tabla,campo1,campo2):
    '''
    Funcion encargada de eliminar una fila de una tabla
    :param tabla: La tabla en la que se quiere eliminar una fila
    :param campo1: El primer campo de cada tabla
    :param campo2: El segundo campo de la tabla alumnos
    '''
    cur=conectarse()
    if(tabla=='cursos'):
        print('Se supone que esto es un curso')
        cur.execute("DELETE FROM cursosWHERE nombre = '"+str(campo1)+"';")
    elif(tabla=='profesores'):
        print('Se supone que esto es un profesor')
        cur.execute("DELETE FROM profesoresWHERE dni = '"+str(campo1)+"';")
    elif(tabla=='alumnos'):
        print('Se supone que esto es un alumno')
        cur.execute("DELETE FROM alumnosWHERE nombre = '"+str(campo1)+"' AND apellidos= '"+str(campo2)+"' ;")
    conn.commit()
    cur.close()
    return 0
def modificar(tabla,idValor,campoMod,valorNew):
    '''
    Funcion que se encarga de modificar un campo de una tabla
    :param tabla: La tabla en la que se quiere hacer una modificacion
    :param idValor: La id de la fila que se quiere cambiar
    :param campoMod: El campo que se quiere modificar
    :param valorNew: El valor que se quiere poner en el campo
    '''
    cur=conectarse()
    if(tabla=='cursos'):
        print('Se supone que esto es un curso')
        cur.execute("UPDATE cursos SET "+str(campoMod)+" = '"+str(valorNew)+"' WHERE id=  "+str(idValor)+";")
    elif(tabla=='profesores'):
        print('Se supone que esto es un profesor')
        cur.execute("UPDATE profesores SET "+str(campoMod)+" = '"+str(valorNew)+"' WHERE id=  "+str(idValor)+" ;")
    elif(tabla=='alumnos'):
        print('Se supone que esto es un alumno')
        cur.execute("UPDATE alumnos SET "+str(campoMod)+" = '"+str(valorNew)+"' WHERE id=  "+str(idValor)+"  ;")
    conn.commit()
    cur.close()
    return 0
def buscar(tabla,campo1,campo2):
    '''
    Funcion encargada de buscar un curso, profesor o alumno y devolver una lista con los datos de este
    :param tabla: La tabla en la que se quiere buscar
    :param campo1: El primer campo de cada tabla
    :param campo2: El segundo campo de la tabla alumnos
    '''
    cur=conectarse()
    if(tabla=='cursos'):
        print('Se supone que esto es un curso')
        cur.execute("SELECT * FROM cursos WHERE nombre = '"+str(campo1)+"';")
        out1=cur.fetchall();
        cur.execute("SELECT alumnos.nombre , alumnos.apellidos FROM alumnos , alumno_curso WHERE alumnos.id=alumno_curso.id_alumno AND alumno_curso.id_curso=((SELECT cursos.id FROM cursos WHERE cursos.nombre='"+str(campo1)+"'));")
        out2=cur.fetchall();
        cur.execute("SELECT profesores.nombre FROM profesores WHERE profesores.dni=(SELECT profesores.dni FROM profesores , cursos WHERE profesores.id=cursos.id_profesor AND cursos.nombre='"+str(campo1)+"') ;")
        out3=cur.fetchall();
        
        lista1=list(out1)
        lista2=list(out2)
        lista3=list(out3)
        if( len(lista1)==0):
            print(tabla+' : '+campo1+' no ha sido encontrado')
            return None
        else:
            print("Curso: "+campo1+" {")
            for x in lista1:
                print(x)
            print("Profesor que imparte "+campo1+" :")
            for x in lista3:
                print(x)
            print("Alumnos en el curso "+campo1+" :")
            for x in lista2:
                print(x)
            print("}")
            return lista1
        
    elif(tabla=='profesores'):
        print('Se supone que esto es un profesor')
        cur.execute("SELECT * FROM profesores  WHERE dni = '"+str(campo1)+"' ;")
        out1=cur.fetchall();
        cur.execute("SELECT cursos.nombre FROM cursos  WHERE cursos.id_profesor=(SELECT profesores.id FROM  profesores WHERE profesores.dni='"+str(campo1)+"') ;")
        out2=cur.fetchall();
        lista1=list(out1)
        lista2=list(out2)
        if( len(lista1)==0):
            print(tabla+' : '+campo1+'  no ha sido encontrado')
            return None
        else:
            print("Profesor: "+campo1+" {")
            for x in lista1:
                print(x)
            print("Cursos que imparte el profesor "+campo1+" :")
            for x in lista2:
                print(x)
            print("}")
            return lista1
    elif(tabla=='alumnos'):
        print('Se supone que esto es un alumno')
        cur.execute("SELECT * FROM alumnos WHERE nombre = '"+str(campo1)+"' AND apellidos= '"+str(campo2)+"' ;")
        out1=cur.fetchall();
        cur.execute("SELECT cursos.nombre  FROM cursos , alumno_curso   WHERE cursos.id=alumno_curso.id_curso   AND alumno_curso.id_alumno=((SELECT alumnos.id FROM alumnos WHERE alumnos.nombre='"+str(campo1)+"' AND alumnos.apellidos='"+str(campo2)+"')) ;")
        out2=cur.fetchall();
        lista1=list(out1)
        lista2=list(out2)
        if( len(lista1)==0):
            print(tabla+' : '+campo1+' '+campo2+' no ha sido encontrado')
            return None
        else:
            print("Alumno: "+campo1+" "+campo2+" {")
            for x in lista1:
                print(x)
            print("Cursos en los que esta matriculado "+campo1+" "+campo2+" :")
            for x in lista2:
                print(x)
            print("}")
            return lista1
    
    conn.commit()
    cur.close()
    return None
def mostrarTodos(tabla):
    '''
    Funcion encargada de mostrar todas las fias de una tabla
    :param tabla: La tabla que se quiere mostrar
    '''
    cur=conectarse()
    if(tabla=='cursos'):
        print('Se supone que esto es un curso')
        cur.execute("SELECT cursos.* FROM cursos ;")
    elif(tabla=='profesores'):
        print('Se supone que esto es un profesor')
        cur.execute("SELECT profesores.* FROM profesores ;")
    elif(tabla=='alumnos'):
        print('Se supone que esto es un alumno')
        cur.execute("SELECT alumnos.* FROM alumnos ;")
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
    '''
    Funcion encargada de aniadir un alumno y un curso a la tabla que conecta alumnos y cursos(la tabla que tiene las matriculaciones de los alumnos)
    :param idAlumno: El id del alumno que se va a matriular
    :param idCurso: El id del curso en el que se va a matricular un alumno
    '''
    cur=conectarse()
    cur.execute("INSERT INTO alumno_curso(id_curso,id_alumno) VALUES( "+str(idCurso)+" , "+str(idAlumno)+"  );")
    conn.commit()
    cur.close()
    print("Alumno matriculado exitosamente")
    return 0
def desmatricularAlumno(idAlumno,idCurso):
    '''
    Funcion encargada de eliminar una matriculacion de la tabla que contiene las matriculaciones
    :param idAlumno: El alumno que se va a desmatricular
    :param idCurso: El curso del cual el alumno se va a desmatricular
    '''
    cur=conectarse()
    cur.execute("DELETE FROM alumno_curso  WHERE id_alumno =  "+str(idAlumno)+"  AND id_curso=  "+str(idCurso)+"   ;")
    conn.commit()
    cur.close()
    print("Alumno desmatriculado exitosamente")
    return 0
def desasignarProfesor(idProfesor,idCurso):
    '''
    Funcion encargada de eliminar un profesor de un curso
    :param idProfesor: El profesor que se va a desasignar
    :param idCurso: El curso del cual el profesor se va a desasignar
    '''
    cur=conectarse()
    cur.execute("UPDATE cursos SET id_profesor = NULL WHERE id="+str(idCurso)+" AND id_profesor="+str(idProfesor)+";")
    conn.commit()
    cur.close()
    print("Profesor desasignado exitosamente")
    return 0
iniciar()
conn = mysqlconnect()



