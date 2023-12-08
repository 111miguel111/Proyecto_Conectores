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
        alumno = buscar('alumnos', nombre, apellidos)
        if(alumno == None):
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
                opcion = input("Seleccione un campo a modificar:\n1.Nombre\n2.Apellidos\n3.Telefono\n4.Direccion\n5.Fecha nacimiento\n0.Salir")
                
                #Opcion para modificar nombre
                if(opcion=='1'):
                    print('Introduzca el nombre del alumno')
                    nombre = escanerAlfanumerico()
                    if(nombre != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0][0],'nombre',nombre)
                        
                #Opcion para modificar apellidos
                elif (opcion == '2'):
                    print('Introduzca los apellidos del alumno')
                    apellidos = escanerTexto()
                    if(apellidos != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0][0],'apellidos',apellidos)
                    
                #Opcion para modificar telefono
                elif(opcion=='3'):
                    print('Introduzca el telefono del alumno')
                    telefono = escanerTelefono()
                    if(telefono != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0][0],'telefono',telefono)
                
                #Opcion para modificar direccion
                elif(opcion=='4'):
                    print('Introduzca la direccion del alumno')
                    direccion = escanerTexto()
                    if(direccion != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0][0],'direccion',direccion)
                            
                #Opcion para modificar la fecha de nacimiento
                elif(opcion == '5'):
                    print('Introduzca la fecha de nacimiento del alumno')
                    fNacimiento = escanerFecha()
                    if(fNacimiento != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0][0],'f_nacimiento',fNacimiento)
                
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
        
    