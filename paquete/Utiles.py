'''
Created on 1 dic 2023

@author: DAM2B-07
'''
import datetime
from paquete.BaseDatos import buscar, modificar, matricularAlumno, desmatricularAlumno
from paquete import BaseDatos

def matricularAlum():
    '''
    Funcien encargada de pedir los datos necesarios, verificarlos y matricular un alumno
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre del alumno introducido es adecuado
    print('\nIntroduzca el nombre del alumno')
    nombre = escanerAlfanumerico()
    if(nombre==None):
        checkValido = False
    #Se comprueba que el apellido del alumno introducido es adecuado 
    if(checkValido):
        print('\nIntroduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    #Se comprueba que el alumno exista
    if(checkValido):        
        alumno=buscar('alumnos', nombre, apellidos)
        if(alumno==None):
            checkValido=False
    #Se comprueba que el nombre del curso introducido es adecuado y se busca en la base de datos para comprobar que existe
    if(checkValido):
        print('\nIntroduzca el nombre del curso')
        nomCurso = escanerTexto()
        if(nomCurso==None):
            checkValido = False
    
    if(checkValido):
        curso = buscar('cursos', nomCurso, None)
        if(curso==None):
            checkValido=False
    #Si no ha habido errores se matricula el alumno en el curso    
    if(checkValido):
        print("\n¿Desea confirmar la modificacion?(Si o no)")
        if(confirmacion()):
            matricularAlumno(alumno[0][0],curso[0][0])
        
def desmatricularAlum():
    '''
    Funcien encargada de pedir los datos necesarios, verificarlos y desmatricular un alumno
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre del alumno introducido es adecuado
    print('\nIntroduzca el nombre del alumno')
    nombre = escanerAlfanumerico()
    if(nombre==None):
        checkValido = False
    #Se comprueba que el apellido del alumno introducido es adecuado y se busca en la base de datos para comprobar que existe  
    if(checkValido):
        print('\nIntroduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    
    if(checkValido):        
        alumno=buscar('alumnos', nombre, apellidos)
        if(alumno==None):
            checkValido=False
    #Se comprueba que el nombre del curso introducido es adecuado y se busca en la base de datos para comprobar que existe
    if(checkValido):
        print('\nIntroduzca el nombre del curso')
        nomCurso = escanerTexto()
        if(nomCurso==None):
            checkValido = False
    
    if(checkValido):
        curso = buscar('cursos', nomCurso, None)
        if(curso==None):
            checkValido=False
    #Si no ha habido errores se desmatricula el alumno en el curso
    if(checkValido):
        print("\n¿Desea confirmar la modificacion?(Si o no)")
        if(confirmacion()):
            desmatricularAlumno(alumno[0][0],curso[0][0])
        
def asignarProfesor():
    '''
    Funcion que se encarga de pedir los datos necesarios, verificarlos y asignar un profesor
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre del curso introducido es adecuado y se busca en la base de datos para comprobar que existe
    if(checkValido):
        print('\nIntroduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        if(nombre == None):
            checkValido = False
            
    if(checkValido):
        curso = buscar('cursos', nombre, None)
        if(curso == None):
            checkValido = False
    #Se comprueba que el dni del profesor introducido es adecuado y se busca en la base de datos para comprobar que existe
    if(checkValido):
        print('\nIntroduzca el DNI del profesor')
        dni = escanerDni()
        if(dni!=None):
            profesor = buscar('profesores',dni,None)
            if(profesor != None):
                #Si no ha habido errores se asigna el profesor en el curso
                print("\n¿Desea confirmar la modificacion?(Si o no)")
                if(confirmacion()):
                    modificar('cursos',curso[0][0],'id_profesor',profesor[0][0])

def desasignarProfesor():
    '''
    Funcion que se encarga de pedir los datos necesarios, verificarlos y desasignar un profesor
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre del curso introducido es adecuado y se busca en la base de datos para comprobar que existe
    if(checkValido):
        print('\nIntroduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        if(nombre == None):
            checkValido = False
            
    if(checkValido):
        curso = buscar('cursos', nombre, None)
        if(curso == None):
            checkValido = False
    #Se comprueba que el dni del profesor introducido es adecuado y se busca en la base de datos para comprobar que existe        
    if(checkValido):
        print('\nIntroduzca el DNI del profesor')
        dni = escanerDni()
        if(dni!=None):
            profesor = buscar('profesores',dni,None)
            if(profesor != None):
                #Si no ha habido errores se desasigna el profesor en el curso
                print("\n¿Desea confirmar la modificacion?(Si o no)")
                if(confirmacion()):
                    BaseDatos.desasignarProfesor(profesor[0][0], curso[0][0])

def escanerTexto():
    '''
    Metodo para escanear un texto
    :return Si el texto es valido devuelve el texto si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 5 intentos
    intentos=0
    while(intentos<5):
        #Se introduce el texto y si hay algo escrito se devuelve
        scan=input()
        if(scan.isspace()==False and scan!=""):
            if(len(scan)<=25):
                return scan
            else:
                print("\nNo puedes introducir mas de 25 caracteres")
        else:
            print("\nNo puedes introducir solos espacios o dejarlo en blanco")
        intentos+=1
    print("\nHas superado el numero de intentos")
    return None

def escanerAlfanumerico():
    '''
    Metodo para escanear una cadena sin espacios
    :return Si la cadena es valida devuelve la cadena, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 5 intentos
    intentos=0
    while(intentos<5):
        #Se introduce la cadena y si no hay espacios se devuelve
        scan=input()
        if(scan.isspace()==False):
            if(scan.isalnum()):
                if(len(scan)<=25):
                    return scan
                else:
                    print("\nNo puedes introducir mas de 25 caracteres")
            else:
                print("\nNo puedes introducir caracteres que no sean alfanumericos")
        else:
            print("\nNo puedes introducir solos espacios o dejarlo en blanco")
            
        intentos+=1
    print("\nHas superado el numero de intentos")
    return None

def escanerAlfabetico():
    '''
    Metodo para escanear una cadena con solo letras
    :return Si la cadena es valida devuelve la cadena, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 5 intentos
    intentos=0
    while(intentos<5):
        #Se introduce la cadena y si solo hay letras se devuelve
        scan=input()
        if(scan.isspace()==False):
            if(scan.isalpha()):
                if(len(scan)<=25):
                    return scan
                else:
                    print("\nNo puedes introducir mas de 25 caracteres")
            else:
                print("\nNo puedes introducir caracteres que no sean alfabeticos")
        else:
            print("\nNo puedes introducir solos espacios o dejarlo en blanco")
        intentos+=1
    print("\nHas superado el numero de intentos")
    return None

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
        if(scan.isspace()==False):
            if(scan.isnumeric()):
                return scan
            else:
                print("\nNo puedes introducir caracteres que no sean numeros")
        else:
            print("\nNo puedes introducir solos espacios o dejarlo en blanco")
        intentos+=1
    print("\nHas superado el numero de intentos")
    return None

def escanerTelefono():
    '''
    Metodo para escanear una cadena con solo numeros
    :return Si la cadena es valida devuelve la cadena, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 5 intentos
    intentos=0
    while(intentos<5):
        scan=input()
        #Se introduce la cadena y si solo hay letras se devuelve
        if(scan.isspace()==False):
            if(scan.isnumeric()):
                if(len(scan)==9):
                    return scan
                else:
                    print("\nSolo puedes introducir 9 caracteres")
            else:
                print("\nNo puedes introducir caracteres que no sean numeros")
        else:
            print("\nNo puedes introducir solos espacios o dejarlo en blanco")
        intentos+=1
    print("\nHas superado el numero de intentos")
    return None

def escanerNumericoDecimal():
    '''
    Metodo para escanear una cadena de numeros con decimales
    :return Si la cadena es valida devuelve la cadena, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 5 intentos
    intentos=0
    while(intentos<5):
        intentos+=1
        #Se introduce la cadena y se le hace un split por el punto
        scan=input()
        scanSplitPunto=scan.split('.')
        
        #Se comprueba que la cadena no esta vacia y si el split ha creado uno o dos valores
        if(scan.isspace()==False and len(scanSplitPunto)==1 or len(scanSplitPunto)==2):
            
            #Si el split solo crea un valor se comprueba si es un numero y se le agrega '.00' y se devuelve
            if(len(scanSplitPunto)==1 and scan.isnumeric()):
                return scan+'.00'
            
            #Si el split crea dos valores se comprueba que ambos sean numeros se comprueba la longitud del segundo campo
            elif(len(scanSplitPunto)==2 and scanSplitPunto[0].isnumeric() and scanSplitPunto[1].isnumeric()):
                
                #Si el segundo campo tiene longitud 1 se devuelve con un 0 delante
                if(len(scanSplitPunto[1])==1):
                    return scanSplitPunto[0]+'.'+scanSplitPunto[1]+'0'
                
                #Si el segundo campo tiene longitud 2 se devuelve tal cual
                elif(len(scanSplitPunto[1])==2):
                    return scanSplitPunto[0]+'.'+scanSplitPunto[1]
                
                #Si el segundo campo tiene mas de 2 valores se pide que se vuelva a introducir
                else:
                    print('\nPorfavor introduce solo 2 decimales')
            else:
                print('\nFormato de decimales incorrecto')
        else:
            print('\nPorfavor introduce numeros y los decimales con punto')
    print("\nHas superado el numero de intentos")
    return None

def escanerDni():
    '''
    Metodo para escanear un DNI
    :return Si la cadena es valida devuelve el DNI, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 5 intentos
    intentos=0
    while(intentos<5):
        #Se introduce el DNI y se comprueba el formato, si cumple se devuelve
        scan=input()
        if(scan.isspace()==False):
            if(len(scan)==9):
                if(scan[0:7].isnumeric()):
                    if(scan[8].isalpha()):
                        return scan.upper()
            
                    else:
                        print("\nSolo puedes introducir letras en caracter 9")
                else:
                    print("\nSolo puedes introducir numeros en los 8 primeros caracteres")
            else:
                print("\nSolo puedes introducir 9 caracteres")
        else:
            print("\nNo puedes introducir solos espacios o dejarlo en blanco")
        intentos+=1
        print('\nPorfavor introduce un DNI (Ocho numeros y una letra)')
    print("\nHas superado el numero de intentos")
    return None

def escanerFecha():
    '''
    Metodo para escanear el dia, mes y anno de un alquiler
    :return Si la cadena es valida devuelve una fecha, si no devuelve None
    '''
    #Se crea un contador de intentos para el bucle que solo iterara hasta 5 intentos
    intentos=0
    while(intentos<5):
        #Se crea un boolean para comprobar si se debe continuar introduciendo datos
        continuar=True
        #Se introduce un dia y se comprueba que sea un numero entre 1 y 31, si no continuar se cambia a false
        print("Introduzca un dia")
        dia=input()
        if(dia.isspace() or dia.isnumeric()==False or int(dia)>31 or int(dia)<=0):
            continuar=False
        #Se introduce un mes y se comprueba que continuar sea true y que sea un numero entre 1 y 12, si no continuar se cambia a false
        if(continuar):
            print("\nIntroduzca un mes")
            mes=input()
            if(mes.isspace() or mes.isnumeric()==False or int(mes)>12 or int(mes)<=0 or continuar==False):
                continuar=False   
        #Se introduce un anno y se comprueba que continuar sea true y que sea un numero entre 1900 y el anno actual, si no continuar se cambia a false
        if(continuar):
            print("\nIntroduzca un anno") 
            anno=input()
            hoy = datetime.datetime.now()
            if(anno.isspace() or anno.isnumeric()==False or int(anno)>int(hoy.strftime("%Y")) or int(anno)<1900 or continuar==False):
                continuar=False 
        #Si continuar sigue siendo true se castea a datetime y se devuelve la string de la fecha
        if(continuar):
            fNacimiento = datetime.datetime(int(anno), int(mes), int(dia))
            return fNacimiento.strftime("%d-%m-%Y")
        intentos+=1
        print('\nPorfavor introduce una fecha correcta (Dia 1-31 mes 1-12 anno 1900-hoy)')
    print("\nHas superado el numero de intentos")
    return None

def confirmacion():
    '''
    Metodo para confirmar si se quiere confirmar una operacion
    :return Devuelve un un boolean. El valor sera True si escribe 'si' y False si escribe 'no'
    '''
    cont = 0
    while(cont<5):
        inputConfirmacion = input()
        if(inputConfirmacion.lower() == 'si'):
            return True
        elif(inputConfirmacion.lower() == 'no'):
            return False
        else:
            if(cont<4):
                print("\nValor incorrecto, pruebe otra vez(Si o no)")
            cont+=1
    print("\nHas superado el numero de intentos")
    return False