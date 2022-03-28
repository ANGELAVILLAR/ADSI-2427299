palabra=input('Ingrese la palabra a medir: ')

total_palabra=len(palabra)

a=palabra.count('a')
e=palabra.count('e')
i=palabra.count('i')
o=palabra.count('o')
u=palabra.count('u')

metrica=total_palabra*(a+e+i+o+u)
print(metrica)