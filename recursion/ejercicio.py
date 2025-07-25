def cantidad_numero(numero:int):
    if numero < 10:
        return 1
    else:
        return 1 + cantidad_numero (numero // 10)
    
resultado = cantidad_numero(147852369)
print(resultado)
