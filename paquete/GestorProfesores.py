'''
Created on 1 dic 2023

@author: DAM2B-07
'''

from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerTelefono,\
    escanerDni, confirmacion

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
        print()
        #Llamada a la base de datos para crear profesor

def bajaProfesor():
    checkValido = True
    print('Introduzca el DNI del profesor')
    dni = escanerDni()
    if(dni==None):
        checkValido = False
        
    if(checkValido):
        print("¿Desea confirmar la baja del Profesor?(Si o no)")
        if(confirmacion()):
            #Llamada a la base de datos para borrar profesor
            print("Profesor eliminado")
        else:
            print("Profesor no eliminado")
            
def modifProfesor():
    checkValido = True
    if(checkValido):
        print('Introduzca el nombre del profesor')
        nombre = escanerAlfanumerico()
        if(nombre==None):
            checkValido = False
    if(checkValido):
        #Metodo para checkear profesor
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
                        #Metodo modificar dni
                    
            #Opcion para modificar la descripcion
            elif (opcion == '2'):
                print('Introduzca el nombre del profesor')
                nombre = escanerAlfanumerico()
                if(dni != None):
                    print("¿Desea confirmar la modificacion?(Si o no)")
                    if(confirmacion()):
                        #Metodo modificar nombre
                
            #Opcion para modificar telefono
            elif(opcion=='3'):
                print('Introduzca la direccion del profesor')
                direccion = escanerTexto()
                if(dni != None):
                    print("¿Desea confirmar la modificacion?(Si o no)")
                    if(confirmacion()):
                        #Metodo para cambiar la direccion
            
            elif(opcion == '4'):
                print('Introduzca el telefono del profesor')
                telefono = escanerTelefono()
                if(dni != None):
                    print("¿Desea confirmar la modificacion?(Si o no)")
                    if(confirmacion()):
                        #Metodo modificar telefono
                
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
    #Metodo para buscar profesor
    
def mostrarTodosProfesor():
    #Metodo para buscar todos los profesors
    print()

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