'''
Created on 1 dic 2023

@author: DAM2B-07
'''
from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerDni, confirmacion
from paquete.BaseDatos import alta, baja, buscar, modificar, mostrarTodos, matricularAlumno, desmatricularAlumno


def altaCurso():
    checkValido = True
    
    print('Introduzca el nombre del curso')
    nombre = escanerAlfanumerico()
    if(nombre == None):
        checkValido = False
        
    if(checkValido):
        print('Introduzca los descripcion del curso')
        descripcion = escanerTexto()
        if(descripcion == None):
            checkValido = False
            
    if(checkValido):
        alta('cursos', nombre, descripcion, None, None, None)


def bajaCurso():
    checkValido = True
    
    print('Introduzca el nombre del curso')
    nombre = escanerAlfanumerico()
    if(nombre == None):
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
        curso = buscar('alumnos', nombre, None)
        if(curso != None):
            checkOpcion = True
            while (checkOpcion):
                opcion = input("Seleccione un campo a modificar:\n1.Nombre\n2.Descripcion\n3.DNI\n0.Salir")
                
                # Opcion para modificar nombre
                if(opcion == '1'):
                    print('Introduzca el nombre del curso')
                    nombre = escanerAlfanumerico()
                    if(nombre != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('cursos',curso[0],'nombre',nombre)
                        
                # Opcion para modificar la descripcion
                elif (opcion == '2'):
                    print('Introduzca los descripcion del curso')
                    descripcion = escanerTexto()
                    if(descripcion != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('cursos',curso[0],'descripcion',descripcion)
                    
                # Opcion para modificar telefono
                elif(opcion == '3'):
                    print('Introduzca el DNI del profesor')
                    dni = escanerDni()
                    # Metodo modificar telefono
                    if(dni != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('cursos',curso[0],'dni',dni)
                            
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
        if(nombre == None):
            checkValido = False
    if(checkValido):
        buscar('cursos', nombre, None)


def mostrarTodosCurso():
    mostrarTodos('cursos')

    
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
            
    alumno=buscar('alumnos', nombre, apellidos)
    if(alumno==None):
        checkValido=False
        
    if(checkValido):
        print('Introduzca los apellidos del curso')
        curso = escanerTexto()
        if(curso==None):
            checkValido = False
    
    curso = buscar('cursos', nombre, None)
    if(curso==None):
        checkValido=False
            
    if(checkValido):
        matricularAlumno(alumno[0],curso[0])
        
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
            
    alumno=buscar('alumnos', nombre, apellidos)
    if(alumno==None):
        checkValido=False
        
    if(checkValido):
        print('Introduzca los apellidos del curso')
        curso = escanerTexto()
        if(curso==None):
            checkValido = False
    
    curso = buscar('cursos', nombre, None)
    if(curso==None):
        checkValido=False
    
    if(checkValido):
        desmatricularAlumno(alumno[0],curso[0])

        
def asignarProfesor():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del curso')
        nombre = escanerAlfanumerico()
        if(nombre == None):
            checkValido = False
            
    if(checkValido):
        curso = buscar('alumnos', nombre, None)
        if(curso == None):
            checkValido = False
            
    if(checkValido):
        print('Introduzca el DNI del profesor')
        dni = escanerDni()
        if(dni != None):
            print("¿Desea confirmar la modificacion?(Si o no)")
            if(confirmacion()):
                modificar('cursos',curso[0],'dni',dni)
                
