from random import randint

# genera un número del 1 al 10 inclusive
numero_aleatorio = randint(1, 10)

opciones_restantes = 3
#¡Arrancá tu juego!
while opciones_restantes>0:
    opcion=int(raw_input('Tu opcion: '))
    opciones_restantes-=1
    if numero_aleatorio==opcion:
        print 'Ganaste!'
        break
else:
    print 'Perdiste'
