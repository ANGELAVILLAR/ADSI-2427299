# *** EJERCICIOS DE FUNCIONES *** 

#   ** PUNTO 1 **

#Diseñe una aplicación que dada una lista de 10 elementos, realice las siguientes acciones:



frutas=['manzana', 'naranja', 'pera', 'uchuva', 'uva', 'banano', 'ciruela', 'durazno', 'limon', 'mandarina']

# a) recorrer la lista y mostrar el contenido de la lista del


def mostrarContenidoList(frutas):
    print(f'\nEl contenido de la lista es:\n')
    contador =1
    for i in frutas:
        print(contador, i)
        contador +=1
    
mostrarContenidoList(frutas)

# b) Hacer una función que recorra la lista y devuelva una cadena
#    con los valores de la lista.

def mostrarCadena(frutas,cadena):
    print(f'\nAhora tenemos el contenido de la lista en String: {cadena}')
    cadena=0
    for i in frutas:
        print(i)

        
cadena=", ".join(frutas)       
mostrarCadena(frutas, cadena)

# c) Ordenarla de mayor a menor

def ordenaLista(frutas):
    frutas.sort()
    print(f'\nLista frutas ordenada de mayor a menor: {frutas}\n')

ordenaLista(frutas)

# d)Buscar un elemento que el usuario pida por teclado 

def buscarElemento(frutas):
    elemento = str(input('\nIngresa el elemento(fruta) que quieres buscar en la lista frutas: '))
    if elemento in frutas:
        print(f'\nEl elemento: {elemento} , se encuentra en la lista Frutas.')
    else:
        print(f'\nEl elemento: {elemento} , no se encuentra en la lista Frutas.')

buscarElemento(frutas)

# e)Mostrar su tamaño y longitud

def mostrarLongitud(frutas):
    cont=0
    for fruta in frutas:
        cont+=1
    return cont

longitud = mostrarLongitud(frutas)
print(f'\nLa longitud de la lista frutas es: {longitud}\n')