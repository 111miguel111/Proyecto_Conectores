'''
Created on 1 dic 2023

@author: DAM2B-07
'''

from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerTelefono,\
    escanerDni

def altaProfesor():
    checkValido = True
    if(checkValido):
        print('Introduzca el DNI del alumno')
        dni = escanerDni()
        if(dni==None):
            checkValido = False
    if(checkValido):
        print('Introduzca el nombre del alumno')
        nombre = escanerAlfanumerico()
        if(nombre==None):
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
        print()
        #Llamada a la base de datos para crear alumno

def bajaProfesor():
    checkValido = True
    if(checkValido):
        print('Introduzca el DNI del alumno')
        dni = escanerDni()
        if(dni==None):
            checkValido = False
            
def mofifCurso():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    if(checkValido):
        #Metodo para checkear alumno
        checkOpcion=True
        while (checkOpcion):
            opcion = input("Seleccione un campo a modificar:\n1.Nombre\n2.Descripcion\n3.DNI\n0.Salir")
            
            #Opcion para modificar nombre
            if(opcion=='1'):
                print('Introduzca el nombre del alumno')
                nombre = escanerAlfanumerico()
                #Metodo modificar nombre
                    
            #Opcion para modificar la descripcion
            elif (opcion == '2'):
                print('Introduzca los descripcion del curso')
                descripcion = escanerTexto()
                #Metodo modificar apellidos
                
            #Opcion para modificar telefono
            elif(opcion=='3'):
                print('Introduzca el DNI del profesor')
                dni = escanerDni()
                #Metodo modificar telefono
            #Opcion para salir del bucle        
            elif(opcion == '0'):
                checkOpcion = False
            
            else:
                print("Valor no valido")

def buscarProfesor():
    checkValido = True
    if(checkValido):
        print('Introduzca el DNI del alumno')
        dni = escanerDni()
        if(dni==None):
            checkValido = False
    #Metodo para buscar curso
    
def mostrarTodosProfesor():
    #Metodo para buscar todos los alumnos
    print()

def asignarProfesor():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del alumno')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    checkValido = True
    if(checkValido):
        print('Introduzca el DNI del profesor')
        dni = escanerDni()
        if(dni==None):
            checkValido = False
    #Metodo asignar profesor