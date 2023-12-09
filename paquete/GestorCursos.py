'''
Created on 1 dic 2023

@author: DAM2B-07
'''
from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerDni, confirmacion
from paquete.BaseDatos import alta, baja, buscar, modificar, mostrarTodos, buscarSinprint


def altaCurso():
    checkValido = True
    
    print('Introduzca el nombre del curso')
    nombre = escanerAlfanumerico()
    curso = buscarSinprint('cursos', nombre, None)
    if(nombre == None):
        print("Error al introducir el nombre")
        checkValido = False
    elif(curso != None):
        print("Ya existe un curso con ese nombre")
        
    if(checkValido):
        print('Introduzca los descripcion del curso')
        descripcion = escanerTexto()
        if(descripcion == None):
            print("Error al introducir la descripcion")
            checkValido = False
            
    if(checkValido):
        alta('cursos', nombre, descripcion, None, None, None)


def bajaCurso():
    checkValido = True
    
    print('Introduzca el nombre del curso')
    nombre = escanerAlfanumerico()
    curso = buscar('cursos', nombre, None)
    if(curso == None):
        checkValido = False
        
    if(checkValido):
        print("¿Desea confirmar la baja del Curso?(Si o no)")
        if(confirmacion()):
            baja('cursos', nombre, None)
            print("Curso eliminado")
        else:
            print("Curso no eliminado")
        

def modifCurso():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        if(nombre == None):
            checkValido = False
            
    if(checkValido):
        curso = buscar('cursos', nombre, None)
        if(curso != None):
            checkOpcion = True
            while (checkOpcion):
                opcion = input("Seleccione un campo a modificar:\n1.Nombre\n2.Descripcion\n3.Profesor\n0.Salir")
                
                # Opcion para modificar nombre
                if(opcion == '1'):
                    print('Introduzca el nombre del curso')
                    nombre = escanerAlfanumerico()
                    curso = buscarSinprint('cursos', nombre, None)
                    if(nombre == None):
                        print("Nombre no valido")
                    elif(curso!=None):
                        print("Ya existe un curso con ese nombre")
                    else:
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('cursos',curso[0][0],'nombre',nombre)
                        
                # Opcion para modificar la descripcion
                elif (opcion == '2'):
                    print('Introduzca los descripcion del curso')
                    descripcion = escanerTexto()
                    if(descripcion != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('cursos',curso[0][0],'descripcion',descripcion)
                    
                # Opcion para modificar telefono
                elif(opcion == '3'):
                    print('Introduzca el DNI del profesor')
                    dni = escanerDni()
                    profesor = buscar('profesores', dni, None)
                    # Metodo modificar telefono
                    if(profesor != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('cursos',curso[0][0],'id',profesor[0][0])
                            
                # Opcion para salir del bucle        
                elif(opcion == '0'):
                    checkOpcion = False
                
                else:
                    print("Valor no valido")


def buscarCurso():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        curso = buscarSinprint('cursos', nombre, None)
        if(curso == None):
            checkValido = False
    if(checkValido):
        buscar('cursos', nombre, None)


def mostrarTodosCurso():
    mostrarTodos('cursos')
