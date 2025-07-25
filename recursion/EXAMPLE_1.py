def muñecas(numero_muñecas):
    if numero_muñecas == 1:
        return print("proceso finalizado:" + str(numero_muñecas))
    muñecas(numero_muñecas -1)
    print("proceso de muñecas:" + str(numero_muñecas))

muñecas(4)
    