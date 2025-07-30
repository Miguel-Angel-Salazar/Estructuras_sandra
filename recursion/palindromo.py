
def espalindrome(palabra):
    if len(palabra) <= 1:
        return True


    if palabra[0] != palabra[-1]:
        return False

    return espalindrome(palabra[1:-1])

resultado = espalindrome("rotor")
print(resultado)
