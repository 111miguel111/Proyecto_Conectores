'''
Created on 1 dic 2023

@author: DAM2B-07
'''
from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerTelefono

def altaAlumno():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del alumno')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    if(checkValido):
        print('Introduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    if(checkValido):
        print('Introduzca el telefono del alumno')
        telefono = escanerTelefono()
        if(telefono==None):
            checkValido = False
    if(checkValido):
        print('Introduzca la direccion del alumno')
        direccion = escanerTexto()
        if(direccion==None):
            checkValido = False
    if(checkValido):
        print('Introduzca la fecha de nacimiento del alumno')
        fNacimiento = escanerTexto()
        if(fNacimiento==None):
            checkValido = False
    if(checkValido):
        print()
        #Llamada a la base de datos para crear alumno
        
def bajaAlumno():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del alumno')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    if(checkValido):
        print('Introduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    if(checkValido):
        print()
        #Llamada a la base de datos para borrar alumno
        
def modifAlumno():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del alumno')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    if(checkValido):
        print('Introduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    if(checkValido):
        #Metodo para checkear alumno
        checkOpcion=True
        while (checkOpcion):
            opcion = input("Seleccione un campo a modificar:\n1.Crear\n2.Borrar\n3.Modificar\n4.Consultar\n5.Mostrar Todos\n6.Matricular en Curso\n0.Salir")
            
            #Opcion para modificar nombre
            if(opcion=='1'):
                print('Introduzca el nombre del alumno')
                nombre = escanerAlfanumerico()
                #Metodo modificar nombre
                    
            #Opcion para modificar apellidos
            elif (opcion == '2'):
                print('Introduzca los apellidos del alumno')
                apellidos = escanerTexto()
                #Metodo modificar apellidos
                
            #Opcion para modificar telefono
            elif(opcion=='3'):
                print('Introduzca el telefono del alumno')
                telefono = escanerTelefono()
                #Metodo modificar telefono
            
            #Opcion para modificar direccion
            elif(opcion=='4'):
                print('Introduzca la direccion del alumno')
                direccion = escanerTexto()
                #Metodo para cambiar la direccion
                        
            #Opcion para modificar la fecha de nacimiento
            elif(opcion == '5'):
                print('Introduzca la fecha de nacimiento del alumno')
                fNacimiento = escanerTexto()
                #Metodo para cambiar fecha de nacimiento
            
            #Opcion para salir del bucle        
            elif(opcion == '0'):
                checkOpcion = False
            
            else:
                print("Valor no valido")
            
def buscarAlum():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del alumno')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    if(checkValido):
        print('Introduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    #Metodo para buscar alumno
    
def mostrarTodosAlum():
    #Metodo para buscar todos los alumnos
    print()
    
def matricularAlum():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del alumno')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    if(checkValido):
        print('Introduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    if(checkValido):
        print('Introduzca los apellidos del alumno')
        curso = escanerTexto()
        if(curso==None):
            checkValido = False
    if(checkValido):
        print()
        #Metodo matriculacion
        
def desmatricularAlum():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del alumno')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    if(checkValido):
        print('Introduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    if(checkValido):
        print('Introduzca los apellidos del alumno')
        curso = escanerTexto()
        if(curso==None):
            checkValido = False
    if(checkValido):
        print()
        #Metodo desmatriculacion
        
    