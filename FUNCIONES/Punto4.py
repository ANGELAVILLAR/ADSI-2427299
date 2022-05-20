# *** EJERCICIOS DE FUNCIONES *** 

#   ** PUNTO 4 **

# Crear un diccionario de géneros literarios con el siguiente contenido:
# Mostrar la información por categorías

narrativa = ('La Vorágine', 'Don Quijote de la mancha', 'Con la soga al cuello')

dramatico = ('El hechizo del agua', 'Primero es ella', 'Hasta que salga el sol')

lirico =('Los Heraldos negros', 'Los versos del capitan', 'Cantar del Mio Cid')

categorias=('narrativa', 'dramatico', 'lirico')


categorias = {'narrativa' : list(narrativa), 'dramatico':list(dramatico), 'lirico':list(lirico)}

print(f' El diccionario de Categorías Literarias es: {categorias}')