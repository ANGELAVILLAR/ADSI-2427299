# *** EJERCICIOS DE FUNCIONES *** 

#   ** PUNTO 5 **

# Realizar un algoritmo que le permita:

# Registrar y mostrar información de 5 estudiantes de un colegio
# Menu con las siguientes opciones:

# a) Ingresar estudiantes
# b) Listar estudiantes
# c) Modificar notas de un estudiante por código
# d) Consultar la nota definitiva de un estudiante por código
# e) Salir

def bienvenida():
    print('\nBienvenido: este es un programa para la gestión de notas de un colegio!\n')
    return

bienvenida()

def listar():
    estudiantes.sort()
    est=','.join(estudiantes)
    print (est)
    

def listarEstudiantes():
        for x in range(3):
            print(estudiantes[x],nota1[x][0],nota2[x][1], promedio[x][2])

estudiantes=[]
codigoEstudiante=[]
listaEstudiantes=[]
nota1=[]
nota2=[]


def promedio():
    prome=(nota1+nota2)/2
    return prome

def listarEstudiantes():
    for x in range(3):
        print(estudiantes[x],nota1[x][0],nota2[x][1], promedio[x][2])

while True:
    for i in range(5):
        nombre=input("Digite el nombre completo del estudiante: ")
        estudiantes.append(nombre)    
        cod_Estudiante=int(input("Digite el codigo del estudiante: "))
        codigoEstudiante.append(cod_Estudiante)
        nota1_Estudiante=float(input("Digite la nota 1: "))
        nota1.append(nota1_Estudiante)
        nota2_Estudiante=float(input("Digite la nota 2: "))
        nota2.append(nota2_Estudiante)

        while True:
            modifica=input("Desea modificar alguna nota de un estudiante si/no: ")
            if modifica=="si":
                modificaNota1=input("Modificar nota 1 si/no. ")
                if  modificaNota1=="si":            
                    cambionota1=float(input("Digite la nueva nota 1: "))
                    if cambionota1>=0.0 and cambionota1<=5.0:                    
                        nota1[0]=cambionota1
                elif modificaNota1=="no":
                        modificaNota2=input("Modificar nota 2 si/no: ")
                        cambionota2=float(input("Digite la nueva nota 2: "))
                        if cambionota2>=0.0 and cambionota2<=5.0:                    
                            nota2[0]=cambionota2
            elif modifica=="no":
                break
        continue
    print(listarEstudiantes())





