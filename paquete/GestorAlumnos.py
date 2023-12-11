'''
Created on 1 dic 2023

@author: DAM2B-07
'''
from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerTelefono, confirmacion,\
    escanerFecha
from paquete.BaseDatos import alta, baja, buscar, modificar, mostrarTodos, buscarSinprint

def altaAlumno():
    '''
    Metodo para dar de alta un alumno
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre introducido es adecuado (Por tener nombre y apellidos como clave se decide permitir poner numeros)
    print('\nALTA:\nIntroduzca el nombre del alumno')
    nombre = escanerAlfanumerico()
    if(nombre==None):
        print("\nError al introducir nombre, pruebe solo letras y menos de 25 caracteres")
        checkValido = False
    #Se comprueba que el apellido introducido es adecuado y se busca en la base de datos para comprobar que no existe
    #(Por tener nombre y apellidos como clave se decide permitir poner numeros)
    if(checkValido):
        print('\nIntroduzca los apellidos del alumno')
        apellidos = escanerTexto()
        alum = buscarSinprint("alumnos", nombre, apellidos)
        if(apellidos==None):
            print("\nError al introducir apellidos, pruebe solo letras y menos de 25 caracteres")
            checkValido = False
        elif(alum!=None):
            print("\nEl alumno introducido ya existe")
            checkValido = False
    #Se comprueba que el telefono introducido es un telefono   
    if(checkValido):
        print('\nIntroduzca el telefono del alumno')
        telefono = escanerTelefono()
        if(telefono==None):
            checkValido = False
    #Se comprueba que la calle es una calle       
    if(checkValido):
        print('\nIntroduzca la direccion del alumno')
        direccion = escanerTexto()
        if(direccion==None):
            checkValido = False
    #Se comprueba que la fecha de nacimiento es una fecha        
    if(checkValido):
        print('\nIntroduzca la fecha de nacimiento del alumno')
        fNacimiento = escanerFecha()
        if(fNacimiento==None):
            checkValido = False
    #Si no ha habido errores se da de alta el alumno       
    if(checkValido):
        alta('alumnos',nombre,apellidos,telefono,direccion,fNacimiento)
        
def bajaAlumno():
    '''
    Metodo para dar de baja un alumno
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre introducido es adecuado
    print('\nBAJA:\nIntroduzca el nombre del alumno')
    nombre = escanerAlfanumerico()
    if(nombre==None):
        checkValido = False
    #Se comprueba que el apellido introducido es adecuado
    if(checkValido):
        print('\nIntroduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    #Se comprueba que el alumno no exista
    if(checkValido):
        alumno = buscar('alumnos', nombre, apellidos)
        if(alumno == None):
            checkValido = False
    #Si no ha habido errores se pide confirmacion y se da de baja el alumno   
    if(checkValido):
        print("\n¿Desea confirmar la baja del alumno?(Si o no)")
        if(confirmacion()):
            baja('alumnos', nombre, apellidos)
            print("\nAlumno eliminado")
        else:
            print("\nAlumno no eliminado")
        
        
def modifAlumno():
    '''
    Metodo para modificar un alumno
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre introducido es adecuado
    print('\nMODIFICAR:\nIntroduzca el nombre del alumno')
    nombre = escanerAlfanumerico()
    if(nombre==None):
        checkValido = False
    #Se comprueba que el apellido introducido es adecuado   
    if(checkValido):
        print('\nIntroduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    #Se busca el alumno en la base de datos para comprobar que no existe        
    if(checkValido):
        alumno=buscar('alumnos', nombre, apellidos)
        if(alumno!=None):
            #Boolean para comprobar si el usuario quiere salir del bucle de las opciones de modificacion
            checkOpcion=True
            while (checkOpcion):
                opcion = input("Seleccione un campo a modificar:\n1.Nombre\t4.Direccion\n2.Apellidos\t5.Fecha nacimiento\n3.Telefono\n0.Salir")
                
                #Opcion para modificar nombre
                if(opcion=='1'):
                    #Se comprueba que el nombre introducido es adecuado y se busca en la base de datos para comprobar que no existe
                    #(Por tener nombre y apellidos como clave se decide permitir poner numeros)
                    print('\nIntroduzca el nombre del alumno')
                    nombre = escanerAlfanumerico()
                    alum = buscarSinprint("alumnos", nombre, alumno[0][2])
                    if(nombre==None):
                        print("\nError al introducir nombre, pruebe solo letras y menos de 25 caracteres")
                    elif(alum!=None):
                        print("\nEl alumno introducido ya existe")
                    else:
                        #Si no ha habido errores se pide confirmacion y se modifica el nombre   
                        print("\n¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            print()
                            modificar('alumnos',alumno[0][0],'nombre',nombre)
                            #Se refresca el alumno para que quede reflejado el nuevo nombre
                            alumno = buscarSinprint('alumnos',nombre,alumno[0][2])
                        
                #Opcion para modificar apellidos
                elif (opcion == '2'):
                    #Se comprueba que los apellidos introducidos son adecuados y se busca en la base de datos para comprobar que no existe
                    #(Por tener nombre y apellidos como clave se decide permitir poner numeros)
                    print('\nIntroduzca los apellidos del alumno')
                    apellidos = escanerTexto()
                    alum = buscarSinprint("alumnos", alumno[0][1], apellidos)
                    if(apellidos==None):
                        print("\nError al introducir nombre, pruebe solo letras y menos de 25 caracteres")
                    elif(alum!=None):
                        print("\nEl alumno introducido ya existe")
                    else:
                        #Si no ha habido errores se pide confirmacion y se modifican los apellidos   
                        print("\n¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0][0],'apellidos',apellidos)
                            #Se refresca el alumno para que queden reflejados los nuevos apellidos
                            alumno = buscarSinprint('alumnos',alumno[0][1],apellidos)
                    
                #Opcion para modificar telefono
                elif(opcion=='3'):
                    #Se comprueba que el telefono introducido es un telefono y si no ha habido errores se pide confirmacion y se modifica
                    print('\nIntroduzca el telefono del alumno')
                    telefono = escanerTelefono()
                    if(telefono != None):
                        print("\n¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0][0],'telefono',telefono)
                
                #Opcion para modificar direccion
                elif(opcion=='4'):
                    #Se comprueba que la direccion introducida es una direccion y si no ha habido errores se pide confirmacion y se modifica
                    print('\nIntroduzca la direccion del alumno')
                    direccion = escanerTexto()
                    if(direccion != None):
                        print("\n¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0][0],'direccion',direccion)
                            
                #Opcion para modificar la fecha de nacimiento
                elif(opcion == '5'):
                    #Se comprueba que la fecha introducida es una fecha y si no ha habido errores se pide confirmacion y se modifica
                    print('\nIntroduzca la fecha de nacimiento del alumno')
                    fNacimiento = escanerFecha()
                    if(fNacimiento != None):
                        print("\n¿Desea confirmar la modificacion?(Si o no)")
                        if(confirmacion()):
                            modificar('alumnos',alumno[0][0],'f_nacimiento',fNacimiento)
                
                #Opcion para salir del bucle        
                elif(opcion == '0'):
                    checkOpcion = False
                
                else:
                    print("\nValor no valido")
            
def buscarAlum():
    '''
    Metodo para buscar un alumno
    '''
    #Boolean que impide que el codigo siga si uno de los valores no es valido
    checkValido = True
    #Se comprueba que el nombre introducido es adecuado
    print('\nBUSCAR:\nIntroduzca el nombre del alumno')
    nombre = escanerAlfanumerico()
    if(nombre==None):
        checkValido = False
    #Se comprueba que los apellidos introducidos son adecuados y se busca en la base de datos
    if(checkValido):
        print('\nIntroduzca los apellidos del alumno')
        apellidos = escanerTexto()
        if(apellidos==None):
            checkValido = False
    if(checkValido):
        buscar('alumnos', nombre, apellidos)
    
def mostrarTodosAlum():
    '''
    Metodo para buscar todos los alumnos
    '''
    print("\nMOSTRAR TODOS:")
    mostrarTodos('alumnos')
        
    