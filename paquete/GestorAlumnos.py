'''
Created on 1 dic 2023

@author: DAM2B-07
'''
from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerTelefono, confirmacion,\
    escanerFecha
from paquete.BaseDatos import alta, baja, buscar, modificar, mostrarTodos, matricularAlumno, desmatricularAlumno

def altaAlumno():
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
        fNacimiento = escanerFecha()
        if(fNacimiento==None):
            checkValido = False
            
    if(checkValido):
        alta('alumnos',nombre,apellidos,telefono,direccion,fNacimiento)
        
def bajaAlumno():
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
        print("¿Desea confirmar la baja del alumno?(Si o no)")
        if(confirmacion()):
            baja('alumnos', nombre, apellidos)
            print("Alumno eliminado")
        else:
            print("Alumno no eliminado")
        
        
def modifAlumno():
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
        alumno=buscar('alumnos', nombre, apellidos)
        if(alumno!=None):
            checkOpcion=True
            while (checkOpcion):
                opcion = input("Seleccione un campo a modificar:\n1.Crear\n2.Borrar\n3.Modificar\n4.Consultar\n5.Mostrar Todos\n6.Matricular en Curso\n0.Salir")
                
                #Opcion para modificar nombre
                if(opcion=='1'):
                    print('Introduzca el nombre del alumno')
                    nombre = escanerAlfanumerico()
                    if(nombre != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0],'nombre',nombre)
                        
                #Opcion para modificar apellidos
                elif (opcion == '2'):
                    print('Introduzca los apellidos del alumno')
                    apellidos = escanerTexto()
                    if(apellidos != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0],'apellidos',apellidos)
                    
                #Opcion para modificar telefono
                elif(opcion=='3'):
                    print('Introduzca el telefono del alumno')
                    telefono = escanerTelefono()
                    if(telefono != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0],'telefono',telefono)
                
                #Opcion para modificar direccion
                elif(opcion=='4'):
                    print('Introduzca la direccion del alumno')
                    direccion = escanerTexto()
                    if(direccion != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0],'direccion',direccion)
                            
                #Opcion para modificar la fecha de nacimiento
                elif(opcion == '5'):
                    print('Introduzca la fecha de nacimiento del alumno')
                    fNacimiento = escanerTexto()
                    if(fNacimiento != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0],'f_nacimiento',fNacimiento)
                
                #Opcion para salir del bucle        
                elif(opcion == '0'):
                    checkOpcion = False
                
                else:
                    print("Valor no valido")
            
def buscarAlum():
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
        buscar('alumnos', nombre, apellidos)
    
def mostrarTodosAlum():
    mostrarTodos('alumnos')
    
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
        
    