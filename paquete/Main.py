'''
Created on 1 dic 2023

@author: DAM2B-07
'''
import paquete.GestorAlumnos,paquete.GestorCursos,paquete.GestorProfesores

def submenuAlumnos():
    #Variable que controla el bucle que ofrece las opciones
    check=True
    while (check):
        opcion = input("Seleccione una opcion para Alumnos:\n1.Crear\n2.Borrar\n3.Modificar\n4.Consultar\n5.Mostrar Todos\n6.Matricular en Curso\n6.Desatricular de Curso\n0.Salir")
        
        #Opcion para crear un nuevo alumno
        if(opcion=='1'):
            paquete.GestorAlumnos.altaAlumno()
                
        #Opcion para buscar un alumno
        elif (opcion == '2'):
            paquete.GestorAlumnos.bajaAlumno()
            
        #Opcion para modificar un alumno
        elif(opcion=='3'):
            paquete.GestorAlumnos.modifAlumno()
        
        #Opcion para mostrar todos los alumnos
        elif(opcion=='4'):
            paquete.GestorAlumnos.buscarAlum()
                    
        #Opcion para finalizar un alumno
        elif(opcion == '5'):
            paquete.GestorAlumnos.mostrarTodosAlum()
        
        #Opcion para matricular un alumno en un curso  
        elif(opcion == '6'):
            paquete.GestorAlumnos.matricularAlum()
            
        #Opcion para desmatricular un alumno en un curso    
        elif(opcion == '7'):
            paquete.GestorAlumnos.desmatricularAlum()
        #Opcion para salir del bucle        
        elif(opcion == '0'):
            check = False
        
        else:
            print("Valor no valido")

def submenuProfesores():
    #Variable que controla el bucle que ofrece las opciones
    check=True
    while (check):
        opcion = input("Seleccione una opcion para Profesores:\n1.Crear\n2.Borrar\n3.Modificar\n4.Consultar\n5.Mostrar Todos\n6.Asignar a Curso\n0.Salir")
        
        #Opcion para crear un nuevo profesor
        if(opcion=='1'):
            paquete.GestorProfesores.altaProfesor()
                
        #Opcion para buscar un profesor
        elif (opcion == '2'):
            paquete.GestorProfesores.bajaProfesor()
            
        #Opcion para modificar un profesor
        elif(opcion=='3'):
            paquete.GestorProfesores.modifProfesor()()
        
        #Opcion para mostrar todos los profesores
        elif(opcion=='4'):
            paquete.GestorProfesores.buscarProfesor()
                    
        #Opcion para finalizar un profesor
        elif(opcion == '5'):
            paquete.GestorProfesores.mostrarTodosProfesor()
        
        #Metodo para asignar un profesor a un curso
        elif(opcion == '6'):
            paquete.GestorProfesores.asignarProfesor()
        
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
        
        #Opcion para crear un nuevo curso
        if(opcion=='1'):
            paquete.GestorCursos.altaCurso()
                
        #Opcion para buscar un curso
        elif (opcion == '2'):
            paquete.GestorCursos.bajaCurso()
            
        #Opcion para modificar un curso
        elif(opcion=='3'):
            paquete.GestorCursos.modifCurso()
        
        #Opcion para mostrar todos los cursos
        elif(opcion=='4'):
            paquete.GestorCursos.buscarCurso()
                    
        #Opcion para finalizar un curso
        elif(opcion == '5'):
            paquete.GestorCursos.mostrarTodosCurso()
        
        #Opcion para matricular un alumno en un curso 
        elif(opcion == '6'):
            paquete.GestorCursos.matricularAlum()
        
        #Opcion para desmatricular un alumno en un curso     
        elif(opcion == '7'):
            paquete.GestorCursos.desmatricularAlum()
        
        #Metodo para asignar un profesor a un curso
        elif(opcion == '8'):
            paquete.GestorCursos.asignarProfesor()
        
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
    
    #Opcion para llamar al menu de alumnos
    if(opcion=='1'):
        submenuAlumnos()
    #Opcion para llamar al menu de profesores
    elif (opcion == '2'):
        submenuProfesores()
    #Opcion para llamar al menu de cursos
    elif (opcion == '3'):
        submenuCursos()
    #Opcion para salir    
    elif(opcion == '0'):
        check = False
        
    else:
        print("Valor no valido")
        
print('Fin del programa')