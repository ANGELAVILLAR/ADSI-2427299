# *** EJERCICIOS DE FUNCIONES *** 

#   ** PUNTO 3 **

# Diseñe un programa que defina una lista vacia 
# Llenarla con la serie Fibobacci
# Hasta el 50

def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        c = a + b
        a = b
        b = c
    
    return b

for i in range(50):
    print(fibonacci(i))
