'''
Created on 1 dic 2023

@author: DAM2B-07
'''

def submenuAlumnos():
    #Variable que controla el bucle que ofrece las opciones
    check=True
    while (check):
        opcion = input("Seleccione una opcion para Alumnos:\n1.Crear\n2.Borrar\n3.Modificar\n4.Consultar\n5.Mostrar Todos\n6.Matricular en Curso\n0.Salir")
        
        #Opcion para crear un nuevo alquiler
        if(opcion=='1'):
            
                
        #Opcion para buscar un alquiler
        elif (opcion == '2'):
            
            
        #Opcion para modificar un alquiler
        elif(opcion=='3'):
            
        
        #Opcion para mostrar todos los alquileres en general o con restriccion por DNI o Matricula
        elif(opcion=='4'):
            
                    
        #Opcion para finalizar un alquiler
        elif(opcion == '5'):
            
        elif(opcion == '6'):
        
        #Opcion para salir del bucle        
        elif(opcion == '0'):
            check = False
        
        else:
            print("Valor no valido")

def submenuProfesores():
    #Variable que controla el bucle que ofrece las opciones
    check=True
    while (check):
        opcion = input("Seleccione una opcion para Profesores:\n1.Crear\n2.Borrar\n3.Modificar\n4.Consultar\n5.Mostrar Todos\n0.Salir")
        
        #Opcion para crear un nuevo alquiler
        if(opcion=='1'):
            
                
        #Opcion para buscar un alquiler
        elif (opcion == '2'):
            
            
        #Opcion para modificar un alquiler
        elif(opcion=='3'):
            
        
        #Opcion para mostrar todos los alquileres en general o con restriccion por DNI o Matricula
        elif(opcion=='4'):
            
                    
        #Opcion para finalizar un alquiler
        elif(opcion == '5'):
            
        
        #Opcion para salir del bucle        
        elif(opcion == '0'):
            check = False
        
        else:
            print("Valor no valido")
            
def submenuCursos():
    #Variable que controla el bucle que ofrece las opciones
    check=True
    while (check):
        opcion = input("Seleccione una opcion para Cursos:\n1.Crear\n2.Borrar\n3.Modificar\n4.Consultar\n5.Mostrar Todos\n0.Salir")
        
        #Opcion para crear un nuevo alquiler
        if(opcion=='1'):
            
                
        #Opcion para buscar un alquiler
        elif (opcion == '2'):
            
            
        #Opcion para modificar un alquiler
        elif(opcion=='3'):
            
        
        #Opcion para mostrar todos los alquileres en general o con restriccion por DNI o Matricula
        elif(opcion=='4'):
            
                    
        #Opcion para finalizar un alquiler
        elif(opcion == '5'):
            
        
        #Opcion para salir del bucle        
        elif(opcion == '0'):
            check = False
        
        else:
            print("Valor no valido")

print('Inicio del programa')

#Bucle de opciones del menu principal
check = True
while (check):
    opcion = input("Seleccione una opcion:\n1.Alumnos\n2.Profesores\n3.Cursos\n0.Salir")
    
    #Opcion para llamar al menu de vehiculos
    if(opcion=='1'):
        submenuAlumnos()
    #Opcion para llamar al menu de alquileres    
    elif (opcion == '2'):
        submenuProfesores()
    elif (opcion == '3'):
        submenuCursos()
    #Opcion para salir    
    elif(opcion == '0'):
        check = False
        
    else:
        print("Valor no valido")
        
print('Fin del programa')