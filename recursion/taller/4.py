def simulacion_juego(lista, jug1=0, jug2=0, conturno= 1):

    if len(lista) == 0:
        return [jug1, jug2]

    if lista[0] >= lista[-1]:
        num_elegido = lista[0]
        num_restante = lista[1:]

    else:
         num_elegido = lista[-1]
         num_restante = lista[:-1]

    if conturno == 1:
        return simulacion_juego(num_restante, jug1 + num_elegido, jug2, 2)
    else:
        return simulacion_juego(num_restante, jug1, jug2 + num_elegido, 1 )


print(simulacion_juego([4, 1, 7, 3]))
print(simulacion_juego([4, 1, 7, 3, 7, 9 ,8 ,7]))
print(simulacion_juego([]))