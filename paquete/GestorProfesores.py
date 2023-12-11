'''
Created on 1 dic 2023

@author: DAM2B-07
'''

from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerTelefono,\
    escanerDni, confirmacion
from paquete.BaseDatos import alta, baja, buscar, modificar, mostrarTodos, buscarSinprint

def altaProfesor():
    '''
    Metodo para dar de alta un profesor
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el dni introducido es adecuado y se busca en la base de datos para comprobar que no existe
    print('\nALTA:\nIntroduzca el DNI del profesor')
    dni = escanerDni()
    if(dni==None):
        print("\nValor de DNI no valido, pruebe a introducir 8 numeros y una letra")
        checkValido = False
    else:
        prof = buscarSinprint("profesores", dni, None)
        if(prof!=None):
            print("\nEl profesor introducido ya existe")
            checkValido = False
    #Se comprueba que el nombre introducido es adecuado
    if(checkValido):
        print('\nIntroduzca el nombre del profesor')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    #Se comprueba que el telefono introducido es adecuado
    if(checkValido):
        print('\nIntroduzca el telefono del profesor')
        telefono = escanerTelefono()
        if(telefono==None):
            checkValido = False
    #Se comprueba que la direccion introducida es adecuada      
    if(checkValido):
        print('\nIntroduzca la direccion del profesor')
        direccion = escanerTexto()
        if(direccion==None):
            checkValido = False
    #Si no ha habido errores se da de alta el profesor
    if(checkValido):
        alta('profesores',dni,nombre,direccion,telefono,None)

def bajaProfesor():
    '''
    Metodo para dar de baja un profesor
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el dni introducido es adecuado y se busca en la base de datos para comprobar que no existe
    print('\nBAJA:\nIntroduzca el DNI del profesor')
    dni = escanerDni()
    if(dni==None):
        checkValido = False
    else:
        prof = buscarSinprint("profesores", dni, None)
        if(prof!=None):
            print("\nEl profesor introducido ya existe")
            checkValido = False
    #Si no ha habido errores se pide confirmacion y se da de baja el profesor
    if(checkValido):
        print("\n¿Desea confirmar la baja del Profesor?(Si o no)")
        if(confirmacion()):
            baja('profesores', dni, None)
            print("\nProfesor eliminado")
        else:
            print("\nProfesor no eliminado")
            
def modifProfesor():
    '''
    Metodo para modificar los campos de un profesor
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el dni introducido es adecuado y se busca en la base de datos para comprobar que no existe
    if(checkValido):
        print('\nMODIFICAR:\nIntroduzca el dni del profesor')
        dni = escanerDni()
        if(dni==None):
            checkValido = False
            
    if(checkValido):
        profesor = buscar('profesores', dni, None)
        if(profesor != None):
            #Boolean para comprobar si el usuario quiere salir del bucle de las opciones de modificacion
            checkOpcion=True
            while (checkOpcion):
                opcion = input("Seleccione un campo a modificar:\n1.DNI\n2.Nombre\n3.Direccion\n4.Telefono\n0.Salir")
                
                #Opcion para modificar nombre
                if(opcion=='1'):
                    #Se comprueba que el dni introducido es adecuado y se busca en la base de datos para comprobar que no existe
                    print('\nIntroduzca el DNI del profesor')
                    dni = escanerDni()
                    prof = buscarSinprint("profesores", dni, None)
                    if(dni==None):
                        print("\nValor de DNI no valido, pruebe a introducir 8 numeros y una letra")
                    elif(prof !=None):
                        print("\nEl profesor introducido ya existe")
                    else:
                        #Si no ha habido errores se pide confirmacion y se modifica el campo
                        print("\n¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('profesores',profesor[0][0],'dni',dni)
                        
                #Opcion para modificar la descripcion
                elif (opcion == '2'):
                    #Se comprueba que el nombre introducido es adecuado
                    print('\nIntroduzca el nombre del profesor')
                    nombre = escanerAlfanumerico()
                    if(nombre != None):
                        #Si no ha habido errores se pide confirmacion y se modifica el campo
                        print("\n¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('profesores',profesor[0][0],'nombre',nombre)
                    
                #Opcion para modificar telefono
                elif(opcion=='3'):
                    #Se comprueba que la direccion introducida es adecuada
                    print('\nIntroduzca la direccion del profesor')
                    direccion = escanerTexto()
                    if(direccion != None):
                        #Si no ha habido errores se pide confirmacion y se modifica el campo
                        print("\n¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('profesores',profesor[0][0],'direccion',direccion)
                
                elif(opcion == '4'):
                    #Se comprueba que el telefono introducido es adecuado
                    print('\nIntroduzca el telefono del profesor')
                    telefono = escanerTelefono()
                    if(telefono != None):
                        #Si no ha habido errores se pide confirmacion y se modifica el campo
                        print("\n¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('profesores',profesor[0][0],'telefono',telefono)
                    
                #Opcion para salir del bucle        
                elif(opcion == '0'):
                    checkOpcion = False
                
                else:
                    print("\nValor no valido")

def buscarProfesor():
    '''
    Metodo para buscar un profesor
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    print('\nBUSCAR:\nIntroduzca el DNI del profesor')
    #Se comprueba que el dni introducido es adecuado y se busca en la base de datos
    dni = escanerDni()
    if(dni==None):
        checkValido = False
    if(checkValido):
        buscar('profesores', dni, None)
    
def mostrarTodosProfesor():
    '''
    Metodo para buscar todos los profesores
    '''
    print("\nMOSTRAR TODOS:\n")
    mostrarTodos('profesores')

