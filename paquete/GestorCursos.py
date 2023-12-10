'''
Created on 1 dic 2023

@author: DAM2B-07
'''
from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerDni, confirmacion
from paquete.BaseDatos import alta, baja, buscar, modificar, mostrarTodos, buscarSinprint


def altaCurso():
    '''
    Metodo para dar de alta un curso
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre introducido es adecuado y se busca en la base de datos para comprobar que no existe
    print('Introduzca el nombre del curso')
    nombre = escanerAlfanumerico()
    curso = buscarSinprint('cursos', nombre, None)
    if(nombre == None):
        print("Error al introducir el nombre, pruebe solo letras y menos de 25 caracteres")
        checkValido = False
    elif(curso != None):
        print("Ya existe un curso con ese nombre")
        checkValido = False
    #Se comprueba que la descripcion introducida es adecuada
    if(checkValido):
        print('Introduzca los descripcion del curso')
        descripcion = escanerTexto()
        if(descripcion == None):
            print("Error al introducir la descripcion")
            checkValido = False
    #Si no ha habido errores se da de alta el curso           
    if(checkValido):
        alta('cursos', nombre, descripcion, None, None, None)


def bajaCurso():
    '''
    Metodo para dar de baja un curso
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre introducido es adecuado y se busca en la base de datos para comprobar que no existe
    print('Introduzca el nombre del curso')
    nombre = escanerAlfanumerico()
    if(nombre!=None):
        curso = buscar('cursos', nombre, None)
        if(curso == None):
            checkValido = False
    else:
        checkValido = False
    #Si no ha habido errores se pide confirmacion y se da de baja el curso    
    if(checkValido):
        print("¿Desea confirmar la baja del Curso?(Si o no)")
        if(confirmacion()):
            baja('cursos', nombre, None)
            print("Curso eliminado")
        else:
            print("Curso no eliminado")
        

def modifCurso():
    '''
    Metodo para modificar un curso
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre introducido es adecuado y se busca en la base de datos para comprobar que no existe
    if(checkValido):
        print('Introduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        if(nombre == None):
            checkValido = False
            
    if(checkValido):
        curso = buscar('cursos', nombre, None)
        if(curso != None):
            #Boolean para comprobar si el usuario quiere salir del bucle de las opciones de modificacion
            checkOpcion = True
            while (checkOpcion):
                opcion = input("Seleccione un campo a modificar:\n1.Nombre\n2.Descripcion\n3.Profesor\n0.Salir")
                
                # Opcion para modificar nombre
                if(opcion == '1'):
                    #Se comprueba que el nombre introducido es adecuado y se busca en la base de datos para comprobar que no existe
                    print('Introduzca el nombre del curso')
                    nombre = escanerAlfanumerico()
                    cursoAux = buscarSinprint('cursos', nombre, None)
                    if(nombre == None):
                        print("Nombre no valido, pruebe solo letras y menos de 25 caracteres")
                    elif(cursoAux != None):
                        print("Ya existe un curso con ese nombre")
                    else:
                        #Si no ha habido errores se pide confirmacion y se modifica el campo  
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('cursos', curso[0][0], 'nombre', nombre)
                        
                # Opcion para modificar la descripcion
                elif (opcion == '2'):
                    #Se comprueba que la descripcion introducida es adecuada
                    print('Introduzca los descripcion del curso')
                    descripcion = escanerTexto()
                    if(descripcion != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        #Si no ha habido errores se pide confirmacion y se modifica el campo  
                        if(confirmacion()):
                            modificar('cursos', curso[0][0], 'descripcion', descripcion)
                    
                # Opcion para modificar telefono
                elif(opcion == '3'):
                    #Se comprueba que el dni del profesor introducido es adecuado
                    print('Introduzca el DNI del profesor')
                    dni = escanerDni()
                    if(dni!=None):
                        profesor = buscar('profesores', dni, None)
                        # Metodo modificar telefono
                        if(profesor != None):
                            print("¿Desea confirmar la modificacion?(Si o no)")
                            #Si no ha habido errores se pide confirmacion y se modifica el campo  
                            if(confirmacion()):
                                modificar('cursos', curso[0][0], 'id_profesor', profesor[0][0])
                            
                # Opcion para salir del bucle        
                elif(opcion == '0'):
                    checkOpcion = False
                
                else:
                    print("Valor no valido")


def buscarCurso():
    '''
    Metodo para buscar un curso
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre introducido es adecuado y se busca en la base de datos
    print('Introduzca el nombre del curso')
    nombre = escanerAlfanumerico()
    if(nombre == None):
        checkValido = False
    if(checkValido):
        buscar('cursos', nombre, None)


def mostrarTodosCurso():
    '''
    Metodo para buscar todos los cursos
    '''
    mostrarTodos('cursos')
