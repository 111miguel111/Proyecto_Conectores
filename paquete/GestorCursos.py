'''
Created on 1 dic 2023

@author: DAM2B-07
'''
from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerTelefono,\
    escanerDni

def altaCurso():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    if(checkValido):
        print('Introduzca los descripcion del curso')
        descripcion = escanerTexto()
        if(descripcion==None):
            checkValido = False
    if(checkValido):
        print()
        #Llamada a la base de datos para crear curso

def bajaCurso():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False

def modifCurso():
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


def buscarCurso():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    #Metodo para buscar curso

def mostrarTodosCurso():
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