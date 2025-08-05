"""
Cree una función recursiva que reciba una lista donde cada posición de la lista es una palabra, debe retornar una lista, convirtiendo la primera letra de cada palabra en mayuscula, Restricciones de implementación
sin utilizar la función capitalize
"""

def fmayor(lista):
    if len(lista) == 0:
        return []
    palabra = lista[0]
    mayuscula = palabra[0].upper() + palabra[1:]
    return [mayuscula] + fmayor(lista[1:])

lista1 = ["hola", "casa","petalo"]
respuesta = fmayor(lista1)
print(fmayor(lista1))