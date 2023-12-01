'''
Created on 1 dic 2023

@author: DAM2B-07
'''
from paquete.Utiles import escanerAlfanumerico, escanerTexto, escanerTelefono

def altaAlumno():
    check = True
    if(check):
        print('Introduzca el nombre del alumno')
        nombre = escanerAlfanumerico
    if(check):
        print('Introduzca los apellidos del alumno')
        apellidos = escanerTexto
    if(check):
        print('Introduzca el telefono del alumno')
        telefono = escanerTelefono
    if(check):
        print('Introduzca la direccion del alumno')
        direccion = escanerTexto
    if(check):
        print('Introduzca la fecha de nacimiento del alumno')
        fNacimiento = escanerTexto
    if(check):
        #Llamada a la base de datos para crear alumno
    