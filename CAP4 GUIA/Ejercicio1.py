print("Este juego es Piedra Papel y Tijera:")
JUGADOR1=input('Jugador 1 Elija su opcion: ')
JUGADOR2=input('Jugador 2 Elija su opción: ')
if (JUGADOR1=="piedra") and (JUGADOR2=="piedra"):
    print("Han empatado por que han elejido la misma opción")
elif (JUGADOR1=="piedra") and (JUGADOR2=="papel"):
    print("Gana Jugador 2 porque el papel envuelve la piedra")
elif (JUGADOR1=="piedra") and (JUGADOR2=="tijera"):
    print("Gana Jugador 1 porque la piedra daña la tijera")
elif (JUGADOR1=="papel") and (JUGADOR2=="piedra"):
    print("Ha ganado Jugador 1 por que el papel envuelve la piedra")
elif (JUGADOR1=="papel") and (JUGADOR2=="papel"):
    print("Han empatado por que han elejido la misma opción")
elif (JUGADOR1=="papel") and (JUGADOR2=="tijera"):
    print("Gana Jugador 2 porque la tijera daña el papel")
elif (JUGADOR1=="tijera") and (JUGADOR2=="piedra"):
    print("Ha ganado Jugador 2 por que la tijera se daña con la piedra")
elif (JUGADOR1=="tijera") and (JUGADOR2=="papel"):
    print("Ha ganado Jugador 1 por que la tijera corta el papel")
elif (JUGADOR1=="tijera") and (JUGADOR2=="tijera"):
    print("Han empatado por que han elejido la misma opción")