"""Cree una función recursiva que calcule la suma de todos los números impares contenidos en las dos diagonales 
de una matriz cuadrada n x n: la diagonal principal (de izquierda a derecha) 
y la diagonal secundaria (de derecha a izquierda). Ejemplo para una matriz de 3x3"""

matriz = [[1, 2, 3],
          [4, 7, 6],
          [7, 8, 9]]

        
def suma_impares(matriz, i=0, suma = 0):
    if i == len(matriz):
        return suma


    if matriz[i][i] % 2 != 0:
        suma += matriz[i][i]


    if matriz[i][len(matriz) - 1 - i] % 2 != 0 and i != len(matriz) - 1 - i:
        suma += matriz[i][len(matriz) - 1 - i]

    return suma + suma_impares(matriz, i + 1)

print(suma_impares(matriz))
