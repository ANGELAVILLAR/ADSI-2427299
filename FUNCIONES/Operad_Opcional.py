#Operadores Opcionales

"""def obtenerDatos(nombre1,celular=None):
    print(f'El nombre es: {nombre1}')
    if celular != None:
        print(f'El numero celular es: {celular}')
        
#Programa principal
nombre1=input('Digite el nombre: ')
celular=int(input('Digite la edad: '))

obtenerDatos(nombre1,celular)"""

#Usando el Return en una funcion

"""def obtenerDatos(nombre1):
    return nombre1

nombre1=input('Digite el nombre: ')
print(obtenerDatos(f'El nombre es {nombre1}'))"""

def mostrarNombre():
    informacion= f'El nombre es {nombre}'
    return informacion

def mostrarApellido():
    informacion=f'El apellido es: {apellido}'
    
def mostrarTodo(nombre,apellido):
    informacion= mostrarNombre (nombre)+'  '+mostrarApellido+ '  ' +(apellido)'
    return informacion

#Programa principal

nombre=input('Digite el nombre: ')
apellido=input('Digite el apellido: ')
print(mostrarTodo(nombre, apellido))

#Programa principal
