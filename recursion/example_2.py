def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero*factorial(numero-1)

resultado = factorial(0)
print(resultado)