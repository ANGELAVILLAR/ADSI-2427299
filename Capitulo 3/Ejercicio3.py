tabla_de_control=('TRWAGMYFPDXBNJZSQVHLCKE')
digito=input('Digite el numero de identificacion: ')
digito_de_control=tabla_de_control[int(digito)%23]
print(f' Su digito de control es: {digito}{digito_de_control}')