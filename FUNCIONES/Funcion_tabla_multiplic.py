#Funcion me realice la tabla de multiplicar de un número
def tablasMultiplicar(numero):
    print(f'Tabla de multiplicar del número {numero} \n')
    
    for i in range(1,11):
        resultado=3*i
        print(f'{numero}*{i}={resultado}')
        
#rpograma Principañ
numero=3
tablasMultiplicar(numero)