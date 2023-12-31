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
        #Se introduce la cadena y comprueba que no este vacio y que ponga 1 o 2 si no te vuelve a preguntar y si fallas 5 veces devulve none
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
    try:
        #Creamos un fichero .ini en el cual se guardan datos para la configuracion del programa 
        config = configparser.ConfigParser()#Creamos la variable
        config['SERVER'] = {'host': 'localhost',
                             'user': 'root',
                             'password': 'my-secret-pw',
                             'port':'3306'}
        with open('config.ini', 'w') as configfile:#Escribimos el fichero de configuracion
            config.write(configfile)
        print("Se ha creado el fichero de configuracion")
    except:
        print("No se ha podido crear el fichero de configuracion")
    return 0

def checkFileExistance(filePath):
    '''
    Comprueba que el fichero de configuracion existe
    :param filePath: El nombre del fichero
    :return Devuelve True si el fichero existe y False si no existe
    '''
    #Comprobamos que el fichero exista si no es el caso devolvemos false
    try:
        with open(filePath, "r") as f:
            return True
        print("El fichero de configuracion existe")
    except FileNotFoundError as e:
        return False
        print("El fichero de configuracion no existe")
    except IOError as e:
        return False
def checkConfigBien(filePath):
    '''
    Funcion encargada de comprobar que el fichero de configuracion esta completo y no tenga errores
    :param filePath: El nombre del fichero
    :return Devuelve False si hay algun problema al leer el fichero de configuracion y si todos los campos estan bien devuelve True
    '''
    campo=''
    #Comprobamos que el fichero tiene todas sus secciones y categorias en orden
    try:
        print("Comprobando estado del fichero de configuracion")
        config = configparser.ConfigParser()
        config.read(filePath)
        campo='host'
        #Comprobamos que la categoria existe solicitando el dato que hay dentro 
        host_variable=str(config['SERVER']['host'])
        if(host_variable.isspace()or len(host_variable)==0):#Si esta categoria esta mal devolveremos false y se entendera que el fichero de configuracion esta mal
            print("El campo "+campo+" no puede estar vacio\n")
            return False
        campo='user'
        #Comprobamos que la categoria existe solicitando el dato que hay dentro 
        user_variable=str(config['SERVER']['user'])
        if(user_variable.isspace() or len(user_variable)==0):#Si esta categoria esta mal devolveremos false y se entendera que el fichero de configuracion esta mal
            print("El campo "+campo+" no puede estar vacio\n")
            return False
        campo='password'
        #Comprobamos que la categoria existe solicitando el dato que hay dentro 
        password_variable=str(config['SERVER']['password'])
        if(password_variable.isspace()):#Si esta categoria esta mal devolveremos false y se entendera que el fichero de configuracion esta mal
            print("El campo "+campo+" no puede ser un espacio\n")
            return False
        campo='port'
        #Comprobamos que la categoria existe solicitando el dato que hay dentro 
        port_variable=int(config['SERVER']['port'])
        if(str(port_variable).isspace()  or str(port_variable).isnumeric()==False or len(str(port_variable))==0):#Si esta categoria esta mal o esta vacia devolveremos false y se entendera que el fichero de configuracion esta mal
            print("El campo "+campo+" tiene que ser numeros\n")
            return False
        print("El fichero de configuracion esta bien")
        print('Si quieres configurar los datos de conexion del sistema gestor de base de datos, modifique la informacion el fichero "config.ini"')
        return True
    except FileNotFoundError as e:
        print("El campo "+campo+" falta o esta mal\n")
        return False
    except IOError as e:
        print("El campo "+campo+" falta o esta mal\n")
        return False
    except :
        print("El campo "+campo+" falta o esta mal\n")
        return False

def conectarse():
    '''
    Funcion encargada de usar la base de datos y devolver un cursor
    :return Devuelve un cursor conectado a la base de datos 
    '''
    #Creamos un nuevo cursor y nos aseguramos de usar la base de datos correcta
    cur = conn.cursor()
    cur.execute('USE miguel_roberto')
    return cur
def deconectarse():
    '''
    Funcion encargada de desconectarse de la la base de datos y cerrar la conexion
    :param conn:
    '''
    #Guardamos culaquier cambio en la conexion y la cerramos
    conn.commit()
    conn.close()
    print("La conexion ha terminado ")
    return 0
def mysqlconnect(): 
    '''
    Funcion encargada de realizar la conexion si hay algun problema en la conexion informara al usuario.
    :return Devulve una conexion si todo ha ido bien
    '''
    #Cogemos todos los datos de el fichero de configuracion e iniciamos una coñexion en base a los datos en el fichero de configuracion
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
    #Si la conexion no se puede realizar ya sea por que  el gestor de base de datos esta apagado nos informara
    except pymysql.err.OperationalError as e:
        print("Se ha producido un error, compruebe que el sistema gestor de base de datos al que se quiere conectar \nesta operativa y que los datos son correctos.\nEl programa se cerrara")
        sys.exit()#Cerramos el programa ya que no deberia continuar tras este error
    #Si la conexion no se puede realizar por que el fichero de configuracion esta mal  nos informara
    except :
        print("Hay un error en el fichero de configuracion que impiede conectarse \n1.Quieres restablecer el fichero con los valores por defecto \n2.Quieres cerrar el programa ")
        opcion=escanerNumerico()
        if (opcion=='1'):
            print("El fichero de configuracion sera restablecido y el programa se cerrara")
            iniciarFicheroConfiguracion()
            print('Si quieres hacer cambios en la conexion mire el archivo de configuracion "config.ini" ')
            sys.exit()#Cerramos el programa ya que no deberia continuar tras este error
        elif(opcion=='2'):
            print("El programa se cerrara")
            sys.exit()#Cerramos el programa ya que no deberia continuar tras este error
        else:
            print("El programa se cerrara")
            sys.exit()#Cerramos el programa ya que no deberia continuar tras este error
    
def iniciar():
    '''
    Funcion encargada de iniciar todo lo relacionado con la base de datos, la configuracion la conexion, crear las tablas etc
    '''
    #Metodo que inicia lo relacionado con la base de datos, comprueba el fichero de datos, comprueba la conexion y si todo esta bien procede a crear una base de datos con las tablas necesarias 
    try:
        if(checkFileExistance("config.ini")==True):#Comprobamos que el fichero de configuracion existe, si no es el caso lo creamos con los datos por defecto
            if(checkConfigBien("config.ini")==False):#Comprobamos que el fichero de configuracion esta bien
                #Si hay algun error informamos al usuario
                print("Hay un error en el fichero de configuracion \n1.Quieres restablecer el fichero con los valores por defecto \n2.Quieres cerrar el programa")
                opcion=escanerNumerico()
                if (opcion=='1'):
                    print("El fichero de configuracion sera restablecido y el programa se cerrara")
                    iniciarFicheroConfiguracion()
                    print('Si quieres hacer cambios en la conexion mire el archivo de configuracion "config.ini" ')
                    sys.exit()#Cerramos el programa ya que no deberia continuar tras este error
                elif(opcion=='2'):
                    print("El programa se cerrara")
                    sys.exit()#Cerramos el programa ya que no deberia continuar tras este error
                else:
                    print("El programa se cerrara")
                    sys.exit()#Cerramos el programa ya que no deberia continuar tras este error
        else:
            
            iniciarFicheroConfiguracion()
        #Llama a la conexion para comprobar si esta funciona
        mysqlconnect()
        conn =mysqlconnect()#Nos conectamos
        cur = conn.cursor()#Creamos un cursor que se usara para crear la base de datos y las tablas correspondientes
        cur.execute('select @@version')
        cur.execute('''CREATE DATABASE IF NOT EXISTS miguel_roberto ;''')
        cur.execute('USE miguel_roberto')
        cur.execute('SET FOREIGN_KEY_CHECKS = 1;')
        
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
                    ON DELETE SET NULL
                    ON UPDATE CASCADE
                );
                ''')
        
        cur.execute('''CREATE TABLE IF NOT EXISTS alumnos
                (
                id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(25) NOT NULL,
                apellidos VARCHAR(25) NOT NULL,
                telefono VARCHAR(9) NOT NULL,
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
        print("La base de datos ha sido creada")
        conn.commit()
        cur.close()
        return True
    except:
        return False
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
    try:
        #Creamos un nuevo cursor y dependiendo de la tabla que nos mandan entramos en un if o en otro y usaremos los campos que necesitemos
        cur=conectarse()
        if(tabla=='cursos'):
            cur.execute("INSERT INTO cursos(nombre,descripcion)VALUES('"+str(campo1)+"','"+str(campo2)+"');")
        elif(tabla=='profesores'):
            cur.execute("INSERT INTO profesores(dni,nombre,direccion,telefono)VALUES('"+str(campo1)+"','"+str(campo2)+"','"+str(campo3)+"','"+str(campo4)+"');")
        elif(tabla=='alumnos'):
            cur.execute("INSERT INTO alumnos(nombre,apellidos,telefono,direccion,f_nacimiento)VALUES('"+str(campo1)+"','"+str(campo2)+"','"+str(campo3)+"','"+str(campo4)+"','"+str(campo5)+"');")
        conn.commit()
        cur.close()
        print("Alta realizada exitosamente")
    except:
        print("No se ha podido realizar el alta")
    return 0
def baja(tabla,campo1,campo2):
    '''
    Funcion encargada de eliminar una fila de una tabla
    :param tabla: La tabla en la que se quiere eliminar una fila
    :param campo1: El primer campo de cada tabla
    :param campo2: El segundo campo de la tabla alumnos
    '''
    try:
        #Creamos un nuevo cursor y dependiendo de la tabla que nos mandan entramos en un if o en otro y eliminaremos lo deseado en base al/los campos dados
        cur=conectarse()
        if(tabla=='cursos'):
            cur.execute("DELETE FROM cursos WHERE nombre = '"+str(campo1)+"';")
        elif(tabla=='profesores'):
            cur.execute("DELETE FROM profesores WHERE dni = '"+str(campo1)+"';")
        elif(tabla=='alumnos'):
            cur.execute("DELETE FROM alumnos WHERE nombre = '"+str(campo1)+"' AND apellidos= '"+str(campo2)+"' ;")
        conn.commit()
        cur.close()
        print("Baja realizada exitosamente")
    except:
        print("No se ha podido realizar la baja")
    return 0
def modificar(tabla,idValor,campoMod,valorNew):
    '''
    Funcion que se encarga de modificar un campo de una tabla
    :param tabla: La tabla en la que se quiere hacer una modificacion
    :param idValor: La id de la fila que se quiere cambiar
    :param campoMod: El campo que se quiere modificar
    :param valorNew: El valor que se quiere poner en el campo
    '''
    try:
        #Creamos un nuevo cursor y dependiendo de la tabla que nos mandan entramos en un if o en otro y actualizamos en campo de la fila y tabla deseada
        cur=conectarse()
        if(tabla=='cursos'):
            cur.execute("UPDATE cursos SET "+str(campoMod)+" = '"+str(valorNew)+"' WHERE id=  "+str(idValor)+";")
        elif(tabla=='profesores'):
            cur.execute("UPDATE profesores SET "+str(campoMod)+" = '"+str(valorNew)+"' WHERE id=  "+str(idValor)+" ;")
        elif(tabla=='alumnos'):
            cur.execute("UPDATE alumnos SET "+str(campoMod)+" = '"+str(valorNew)+"' WHERE id=  "+str(idValor)+"  ;")
        conn.commit()
        cur.close()
        print("Modificacion realizada exitosamente")
    except:
        print("No se ha podido realizar la modificacion")
    return 0
def buscar(tabla,campo1,campo2):
    '''
    Funcion encargada de buscar un curso, profesor o alumno mostrarlo y devolver una lista con los datos de este
    :param tabla: La tabla en la que se quiere buscar
    :param campo1: El primer campo de cada tabla
    :param campo2: El segundo campo de la tabla alumnos
    :return Devuelve la lista con la linea que se busca o None si no encuentra nada
    '''
    try:
        #Creamos un nuevo cursor y dependiendo de la tabla que nos mandan entramos en un if o en otro y devolvemos la fila de la tabla deseada teniendo en cuenta el o los campos necesarios, tambien mostramos las relaciones entre tablas que pueda tener
        cur=conectarse()
        if(tabla=='cursos'):
            cur.execute("SELECT * FROM cursos WHERE nombre = '"+str(campo1)+"';")
            out1=cur.fetchall();#Recogemos la respuesta del cursor para trabajar con ella de manera independiente
            cur.execute("SELECT alumnos.nombre , alumnos.apellidos FROM alumnos , alumno_curso WHERE alumnos.id=alumno_curso.id_alumno AND alumno_curso.id_curso=((SELECT cursos.id FROM cursos WHERE cursos.nombre='"+str(campo1)+"'));")
            out2=cur.fetchall();#Recogemos la respuesta del cursor en otra variable para trabajar con ella de manera independiente
            cur.execute("SELECT profesores.nombre FROM profesores WHERE profesores.dni=(SELECT profesores.dni FROM profesores , cursos WHERE profesores.id=cursos.id_profesor AND cursos.nombre='"+str(campo1)+"') ;")
            out3=cur.fetchall();#Recogemos la respuesta del cursor en otra variable para trabajar con ella de manera independiente
            
            #Convertimos las tuplas en listas para trabajar mejor con ellas
            lista1=list(out1)
            lista2=list(out2)
            lista3=list(out3)
            #Si la primera lista(que contendria la fila de la tabla objetivo)esta vacia informamos de ello si no, empezamos a mostrar los datos
            if( len(lista1)==0):
                print(tabla+' : '+campo1+' no ha sido encontrado')
                return None
            else:
                #Mostramos los datos de la fila
                print("Curso: "+campo1+" {")
                for x in lista1:
                    print(x)
                #Mostrasmos los datos de la tabla relacionada
                print("Profesor que imparte "+campo1+" :")
                for x in lista3:
                    print(x)
                #Mostrasmos los datos de la tabla relacionada
                print("Alumnos en el curso "+campo1+" :")
                for x in lista2:
                    print(x)
                print("}")
                return lista1
            
        elif(tabla=='profesores'):
            cur.execute("SELECT * FROM profesores  WHERE dni = '"+str(campo1)+"' ;")
            out1=cur.fetchall();#Recogemos la respuesta del cursor para trabajar con ella de manera independiente
            cur.execute("SELECT cursos.nombre FROM cursos  WHERE cursos.id_profesor=(SELECT profesores.id FROM  profesores WHERE profesores.dni='"+str(campo1)+"') ;")
            out2=cur.fetchall();#Recogemos la respuesta del cursor en otra variable para trabajar con ella de manera independiente
            
            #Convertimos las tuplas en listas para trabajar mejor con ellas
            lista1=list(out1)
            lista2=list(out2)
            #Si la primera lista(que contendria la fila de la tabla objetivo)esta vacia informamos de ello si no, empezamos a mostrar los datos
            if( len(lista1)==0):
                print(tabla+' : '+campo1+'  no ha sido encontrado')
                return None
            else:
                #Mostramos los datos de la fila
                print("Profesor: "+campo1+" {")
                for x in lista1:
                    print(x)
                #Mostrasmos los datos de la tabla relacionada
                print("Cursos que imparte el profesor "+campo1+" :")
                for x in lista2:
                    print(x)
                print("}")
                return lista1
        elif(tabla=='alumnos'):
            cur.execute("SELECT * FROM alumnos WHERE nombre = '"+str(campo1)+"' AND apellidos= '"+str(campo2)+"' ;")
            out1=cur.fetchall();#Recogemos la respuesta del cursor para trabajar con ella de manera independiente
            cur.execute("SELECT cursos.nombre  FROM cursos , alumno_curso   WHERE cursos.id=alumno_curso.id_curso   AND alumno_curso.id_alumno=((SELECT alumnos.id FROM alumnos WHERE alumnos.nombre='"+str(campo1)+"' AND alumnos.apellidos='"+str(campo2)+"')) ;")
            out2=cur.fetchall();#Recogemos la respuesta del cursor en otra variable para trabajar con ella de manera independiente
            
            #Convertimos las tuplas en listas para trabajar mejor con ellas
            lista1=list(out1)
            lista2=list(out2)
            #Si la primera lista(que contendria la fila de la tabla objetivo)esta vacia informamos de ello si no, empezamos a mostrar los datos
            if( len(lista1)==0):
                print(tabla+' : '+campo1+' '+campo2+' no ha sido encontrado')
                return None
            else:
                #Mostramos los datos de la fila
                print("Alumno: "+campo1+" "+campo2+" {")
                for x in lista1:
                    print(x)
                #Mostrasmos los datos de la tabla relacionada
                print("Cursos en los que esta matriculado "+campo1+" "+campo2+" :")
                for x in lista2:
                    print(x)
                print("}")
                return lista1
        cur.close()
    except:
        print("No se ha podido encontrar el elemento de la tabla")
    return None
def buscarSinprint(tabla,campo1,campo2):
    '''
    Funcion encargada de buscar un curso, profesor o alumno y devolver una lista con los datos de este
    :param tabla: La tabla en la que se quiere buscar
    :param campo1: El primer campo de cada tabla
    :param campo2: El segundo campo de la tabla alumnos
    :return Devuelve la lista con la linea que se busca o None si no encuentra nada
    '''
    #Creamos un nuevo cursor y dependiendo de la tabla que nos mandan entramos en un if o en otro y devolvemos la fila de la tabla deseada teniendo en cuenta el o los campos necesarios
    try:
        cur=conectarse()
        if(tabla=='cursos'):
            cur.execute("SELECT * FROM cursos WHERE nombre = '"+str(campo1)+"';")
            out1=cur.fetchall();#Recogemos la respuesta del cursor para trabajar con ella de manera independiente
            #Convertimos la tupla en lista para trabajar mejor con ella
            lista1=list(out1)
            #Si la lista(que contendria la fila de la tabla objetivo)esta vacia informamos de ello si no, la devolvemos
            if( len(lista1)==0):
                return None
            else:
                return lista1
        elif(tabla=='profesores'):
            cur.execute("SELECT * FROM profesores  WHERE dni = '"+str(campo1)+"' ;")
            out1=cur.fetchall();#Recogemos la respuesta del cursor para trabajar con ella de manera independiente
            #Convertimos la tupla en lista para trabajar mejor con ella
            lista1=list(out1)
            #Si la lista(que contendria la fila de la tabla objetivo)esta vacia informamos de ello si no, la devolvemos
            if( len(lista1)==0):
                return None
            else:
                return lista1
        elif(tabla=='alumnos'):
            cur.execute("SELECT * FROM alumnos WHERE nombre = '"+str(campo1)+"' AND apellidos= '"+str(campo2)+"' ;")
            out1=cur.fetchall();#Recogemos la respuesta del cursor para trabajar con ella de manera independiente
            #Convertimos la tupla en lista para trabajar mejor con ella
            lista1=list(out1)
            #Si la lista(que contendria la fila de la tabla objetivo)esta vacia informamos de ello si no, la devolvemos
            if( len(lista1)==0):
                return None
            else:
                return lista1
        cur.close()
    except:
        print("No se ha podido encontrar el elemento de la tabla")
    return None
def mostrarTodos(tabla):
    '''
    Funcion encargada de mostrar todas las fias de una tabla
    :param tabla: La tabla que se quiere mostrar
    '''
    try:
        #Creamos un nuevo cursor y dependiendo de la tabla que nos mandan entramos en un if o en otro y mostramos la tabla entera
        cur=conectarse()
        if(tabla=='cursos'):
            cur.execute("SELECT cursos.* FROM cursos ;")
        elif(tabla=='profesores'):
            cur.execute("SELECT profesores.* FROM profesores ;")
        elif(tabla=='alumnos'):
            cur.execute("SELECT alumnos.* FROM alumnos ;")
        out=cur.fetchall();#Recogemos la respuesta del cursor para trabajar con ella de manera independiente
        #Convertimos la tupla en lista para trabajar mejor con ella
        lista=list(out)
        #Si la lista(que contendria la fila de la tabla objetivo)esta vacia informamos de ello si no, la devolvemos
        if(len(lista)==0):
            print('La tabla '+tabla+' esta vacia')
        else:
            for x in lista:
                print(x)
        cur.close()
    except:
        print("No se ha podido mostrar la tabla")
    return 0
def matricularAlumno(idAlumno,idCurso):
    '''
    Funcion encargada de aniadir un alumno y un curso a la tabla que conecta alumnos y cursos(la tabla que tiene las matriculaciones de los alumnos)
    :param idAlumno: El id del alumno que se va a matriular
    :param idCurso: El id del curso en el que se va a matricular un alumno
    '''
    try:
        #Creamos un nuevo cursor y añadimos los ids a la tabla de matriculaciones
        cur=conectarse()
        cur.execute("INSERT INTO alumno_curso(id_curso,id_alumno) VALUES( "+str(idCurso)+" , "+str(idAlumno)+"  );")
        conn.commit()
        cur.close()
        print("Alumno matriculado exitosamente")
    except:
        print("No se ha podido matricular al alumno")
    return 0
def desmatricularAlumno(idAlumno,idCurso):
    '''
    Funcion encargada de eliminar una matriculacion de la tabla que contiene las matriculaciones
    :param idAlumno: El alumno que se va a desmatricular
    :param idCurso: El curso del cual el alumno se va a desmatricular
    '''
    try:
        #Creamos un nuevo cursor y quitamos los ids a la tabla de matriculaciones
        cur=conectarse()
        cur.execute("DELETE FROM alumno_curso  WHERE id_alumno =  "+str(idAlumno)+"  AND id_curso=  "+str(idCurso)+"   ;")
        conn.commit()
        cur.close()
        print("Alumno desmatriculado exitosamente")
    except:
        print("No se ha podido desmatricular al alumno")
    return 0
def desasignarProfesor(idProfesor,idCurso):
    '''
    Funcion encargada de eliminar un profesor de un curso
    :param idProfesor: El profesor que se va a desasignar
    :param idCurso: El curso del cual el profesor se va a desasignar
    '''
    try:
        #Creamos un nuevo cursor y quitamos el id de el curso correspondiente
        cur=conectarse()
        cur.execute("UPDATE cursos SET id_profesor = NULL WHERE id="+str(idCurso)+" AND id_profesor="+str(idProfesor)+";")
        conn.commit()
        cur.close()
        print("Profesor desasignado exitosamente")
    except:
        print("No se ha podido desasignar al profesor")
    return 0
#Nada mas comenzar el programa iniciamos lo necesario para conectarse
if(iniciar()):
    #Creamos una variable general de conexion para no estar conectandonos todo el rato
    conn = mysqlconnect()
else:
    sys.exit()#Cerramos el programa ya que no deberia continuar tras llegar aqui


