print 'Pig Latin'
# Preparo el sonido final
pyg = 'ay'
# Pido la cadena de texto
original = raw_input('Escribe una palabra:')
# Compruebo que se ha introducido algo y que es una palabra
if len(original) > 0 and original.isalpha():
	palabra = original.lower()
	primera = palabra[0]
	nueva_palabra=palabra[1:len(palabra)]+primera+pyg
	print 'La traduccion de tu palabra es:'
	print nueva_palabra
else:
	print 'Vacio'
