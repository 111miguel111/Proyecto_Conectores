'''
Created on 1 dic 2023

@author: DAM2B-07
'''

from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerTelefono,\
    escanerDni, confirmacion
from paquete.BaseDatos import alta, baja, buscar, modificar, mostrarTodos

def altaProfesor():
    checkValido = True

    print('Introduzca el DNI del profesor')
    dni = escanerDni()
    if(dni==None):
        checkValido = False
        
    if(checkValido):
        print('Introduzca el nombre del profesor')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    
    if(checkValido):
        print('Introduzca el telefono del profesor')
        telefono = escanerTelefono()
        if(telefono==None):
            checkValido = False
            
    if(checkValido):
        print('Introduzca la direccion del profesor')
        direccion = escanerTexto()
        if(direccion==None):
            checkValido = False
            
    if(checkValido):
        alta('profesores',dni,nombre,direccion,telefono,None)

def bajaProfesor():
    checkValido = True
    print('Introduzca el DNI del profesor')
    dni = escanerDni()
    if(dni==None):
        checkValido = False
        
    if(checkValido):
        print("¿Desea confirmar la baja del Profesor?(Si o no)")
        if(confirmacion()):
            baja('profesores', dni, None)
            print("Profesor eliminado")
        else:
            print("Profesor no eliminado")
            
def modifProfesor():
    checkValido = True
    if(checkValido):
        print('Introduzca el dni del profesor')
        dni = escanerDni()
        if(dni==None):
            checkValido = False
            
    if(checkValido):
        profesor = buscar('profesores', dni, None)
        if(profesor != None):
            checkOpcion=True
            while (checkOpcion):
                opcion = input("Seleccione un campo a modificar:\n1.DNI\n2.Nombre\n3.Direccion\n4.Telefono\n0.Salir")
                
                #Opcion para modificar nombre
                if(opcion=='1'):
                    print('Introduzca el DNI del profesor')
                    dni = escanerDni()
                    if(dni != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('profesores',profesor[0][0],'dni',dni)
                        
                #Opcion para modificar la descripcion
                elif (opcion == '2'):
                    print('Introduzca el nombre del profesor')
                    nombre = escanerAlfanumerico()
                    if(dni != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('profesores',profesor[0][0],'nombre',nombre)
                    
                #Opcion para modificar telefono
                elif(opcion=='3'):
                    print('Introduzca la direccion del profesor')
                    direccion = escanerTexto()
                    if(direccion != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('profesores',profesor[0][0],'direccion',direccion)
                
                elif(opcion == '4'):
                    print('Introduzca el telefono del profesor')
                    telefono = escanerTelefono()
                    if(telefono != None):
                        print("¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('profesores',profesor[0][0],'telefono',telefono)
                    
                #Opcion para salir del bucle        
                elif(opcion == '0'):
                    checkOpcion = False
                
                else:
                    print("Valor no valido")

def buscarProfesor():
    print('Introduzca el DNI del profesor')
    dni = escanerDni()
    if(dni==None):
        checkValido = False
    if(checkValido):
        buscar('profesores', dni, None)
    
def mostrarTodosProfesor():
    mostrarTodos('profesores')

