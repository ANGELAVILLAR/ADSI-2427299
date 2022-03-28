Edad=int(input('Ingrese su edad: '))
Peso=float(input('Ingrese su peso: '))
Tension=int(input('Ingrese su tensión arterial: '))
Pulso=int(input('Ingrese su pulso: '))
Hemoglobina=float(input('Ingrese su nivel de hemoglobina: '))
Ayuno=input('Se encuentra en ayunas? :')
Estado_salud=input('Mencione si tiene alguna enfermedad preexistente? :')
Plaquetas=int(input('Ingrese su nivel de plaquetas: '))
Proteinas=int(input('Ingrese su nivel de proteinas: '))

if Edad>=18 and Edad<=65:
    print('Usted se encuentra en el rango de edad para donar sangre')
else:
    print('Usted no se encuentra en el rango de edad para donar sangre.')
if Peso<=50:
    print('Usted se encuentra con el peso adecuado para donar sangre')
else:
    print('Usted no cuenta con el peso adecuado para donar sangre.')
if Tension>=50 and Tension==100:
    print('Usted se encuentra con la tensión arterial adecuado para donar sangre')
else:
    print('Usted no cuenta con la tensión arterial adecuada para donar sangre.')
if Pulso>=50 and Pulso==110:
    print('Usted se encuentra con pulso adecuado para donar sangre')
else:
    print('Usted no cuenta con pulso adecuada para donar sangre.')
if Hemoglobina>=13.5:
    print('Usted se encuentra con el nivel de hemoglobina adecuado para donar sangre')
else:
    print('Usted no cuenta con el nivel de hemoglobina adecuado para donar sangre.')
if Ayuno=='si':
    print('Usted se encuentra en ayuno, se encuentra listo donar sangre')
else:
    print('Usted no cuenta con con el ayuno para donar sangre.')
if Estado_salud=='Si':
    print('Usted puede donar sangre')
else:
    print('Usted no no puede donar sangre.')
if Plaquetas>=150000:
    print('Usted se encuentra con las plaqueas adecuadas para donar sangre')
else:
    print('Usted no cuenta con las plaquetas adecuadaa para donar sangre.')
if Proteinas>=6:
    print('Usted se encuentra con las plaqueas adecuadas para donar sangre')
else:
    print('Usted no cuenta con las plaquetas adecuadaa para donar sangre.')