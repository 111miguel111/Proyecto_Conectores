'''
Created on 1 dic 2023

@author: DAM2B-07
'''
from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerTelefono,\
    escanerDni, confirmacion
from paquete.BaseDatos import alta

def altaCurso():
    checkValido = True
    
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
        alta('curso',nombre,descripcion)

def bajaCurso():
    checkValido = True
    
    print('Introduzca el nombre del curso')
    nombre = escanerAlfanumerico()
    if(nombre==None):
        checkValido = False
        
    if(checkValido):
        print("¿Desea confirmar la baja del Curso?(Si o no)")
        if(confirmacion()):
            #Llamada a la base de datos para borrar curso
            print("Curso eliminado")
        else:
            print("Curso no eliminado")
        

def modifCurso():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
            
    if(checkValido):
        #Metodo para checkear curso
        checkOpcion=True
        while (checkOpcion):
            opcion = input("Seleccione un campo a modificar:\n1.Nombre\n2.Descripcion\n3.DNI\n0.Salir")
            
            #Opcion para modificar nombre
            if(opcion=='1'):
                print('Introduzca el nombre del curso')
                nombre = escanerAlfanumerico()
                if(nombre != None):
                    print("¿Desea confirmar la modificacion?(Si o no)")
                    if(confirmacion()):
                        #Metodo modificar nombre
                        print()
                    
            #Opcion para modificar la descripcion
            elif (opcion == '2'):
                print('Introduzca los descripcion del curso')
                descripcion = escanerTexto()
                if(descripcion != None):
                    print("¿Desea confirmar la modificacion?(Si o no)")
                    if(confirmacion()):
                        #Metodo modificar descripcion
                        print()
                
            #Opcion para modificar telefono
            elif(opcion=='3'):
                print('Introduzca el DNI del profesor')
                dni = escanerDni()
                #Metodo modificar telefono
                if(dni != None):
                    print("¿Desea confirmar la modificacion?(Si o no)")
                    if(confirmacion()):
                        #Metodo modificar dni
                        print()
                        
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
    #Metodo para buscar todos los cursos
    print()
    
def matricularAlum():
    checkValido = True
    
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
        print('Introduzca los apellidos del curso')
        curso = escanerTexto()
        if(curso==None):
            checkValido = False
            
    if(checkValido):
        print()
        #Metodo matriculacion
        
def desmatricularAlum():
    checkValido = True

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
        print('Introduzca los apellidos del curso')
        curso = escanerTexto()
        if(curso==None):
            checkValido = False
            
    if(checkValido):
        print()
        #Metodo desmatriculacion
        
def asignarProfesor():
    checkValido = True
    
    print('Introduzca el nombre del curso')
    nombre = escanerAlfanumerico()
    if(nombre==None):
        checkValido = False
        
    if(checkValido):
        print('Introduzca el DNI del profesor')
        dni = escanerDni()
        if(dni==None):
            checkValido = False
    #Metodo asignar profesor