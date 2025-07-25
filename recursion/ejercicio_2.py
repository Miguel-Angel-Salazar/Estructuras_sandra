def reversa_palabra(palabra: str):
    if palabra == "":
        return ""
    else:
        return palabra [-1] + reversa_palabra(palabra[:-1])
    
resultado = reversa_palabra("casa")
print(resultado)

