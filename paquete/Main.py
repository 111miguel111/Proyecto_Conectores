'''
Created on 1 dic 2023

@author: DAM2B-07
'''
import paquete.GestorAlumnos,paquete.GestorCursos,paquete.GestorProfesores
from paquete import BaseDatos

def submenuAlumnos():
    #Variable que controla el bucle que ofrece las opciones
    check=True
    while (check):
        opcion = input("\nSeleccione una opcion para Alumnos:\n1.Crear\t\t4.Consultar\t\t7.Desmatricular de Curso"+
"\n2.Borrar\t5.Mostrar Todos\n3.Modificar\t6.Matricular en Curso\n0.Salir\n\n")
        
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
            paquete.Utiles.matricularAlum()
            
        #Opcion para desmatricular un alumno en un curso    
        elif(opcion == '7'):
            paquete.Utiles.desmatricularAlum()
        #Opcion para salir del bucle        
        elif(opcion == '0'):
            check = False
        
        else:
            print("Valor no valido")

def submenuProfesores():
    #Variable que controla el bucle que ofrece las opciones
    check=True
    while (check):
        opcion = input("\nSeleccione una opcion para Profesores:\n1.Crear\t\t4.Consultar\t\t7.Desasignar de curso"+
"\n2.Borrar\t5.Mostrar Todos\n3.Modificar\t6.Asignar a Curso\n0.Salir\n\n")
        
        #Opcion para crear un nuevo profesor
        if(opcion=='1'):
            paquete.GestorProfesores.altaProfesor()
                
        #Opcion para buscar un profesor
        elif (opcion == '2'):
            paquete.GestorProfesores.bajaProfesor()
            
        #Opcion para modificar un profesor
        elif(opcion=='3'):
            paquete.GestorProfesores.modifProfesor()
        
        #Opcion para mostrar todos los profesores
        elif(opcion=='4'):
            paquete.GestorProfesores.buscarProfesor()
                    
        #Opcion para finalizar un profesor
        elif(opcion == '5'):
            paquete.GestorProfesores.mostrarTodosProfesor()
        
        #Metodo para asignar un profesor a un curso
        elif(opcion == '6'):
            paquete.Utiles.asignarProfesor()
            
        #Metodo para desasignar un profesor a un curso    
        elif(opcion == '7'):
            paquete.Utiles.desasignarProfesor()
        
        #Opcion para salir del bucle        
        elif(opcion == '0'):
            check = False
        
        else:
            print("Valor no valido")
            
def submenuCursos():
    #Variable que controla el bucle que ofrece las opciones
    check=True
    while (check):
        opcion = input("\nSeleccione una opcion para Cursos:\n1.Crear\t\t4.Consultar\t\t7.Desatricular alumno"+
"\n2.Borrar\t5.Mostrar Todos\t\t8.Asignar profesor\n3.Modificar\t6.Matricular alumno\t9.Desasignar profesor\n0.Salir\n\n")
        
        #Opcion para crear un nuevo curso
        if(opcion=='1'):
            paquete.GestorCursos.altaCurso()
                
        #Opcion para buscar un curso
        elif (opcion == '2'):
            paquete.GestorCursos.bajaCurso()
            
        #Opcion para modificar un curso
        elif(opcion=='3'):
            paquete.GestorCursos.modifCurso()
        
        #Opcion para mostrar un cursos
        elif(opcion=='4'):
            paquete.GestorCursos.buscarCurso()
                    
        #Opcion para mostrar todos los cursos
        elif(opcion == '5'):
            paquete.GestorCursos.mostrarTodosCurso()
        
        #Opcion para matricular un alumno en un curso 
        elif(opcion == '6'):
            paquete.Utiles.matricularAlum()
        
        #Opcion para desmatricular un alumno en un curso     
        elif(opcion == '7'):
            paquete.Utiles.desmatricularAlum()
        
        #Metodo para asignar un profesor a un curso
        elif(opcion == '8'):
            paquete.Utiles.asignarProfesor()
        
        #Metodo para desasignar un profesor a un curso    
        elif(opcion == '9'):
            paquete.Utiles.desasignarProfesor()
        
        #Opcion para salir del bucle        
        elif(opcion == '0'):
            check = False
        
        else:
            print("Valor no valido")

print('Inicio del programa\n')
#Bucle de opciones del menu principal
check = True
while (check):
    opcion = input("Seleccione una opcion del menu:\n1.Alumnos\n2.Profesores\n3.Cursos\n0.Salir\n\n")
    
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
BaseDatos.deconectarse()
print('Fin del programa')