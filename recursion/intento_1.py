def cantidad_digitos(numero, contador = 0):
   if numero == 0:
      if contador % 2:
          return "impar"
      else:
          return "par"
   else:
        return cantidad_digitos(numero // 10, contador +1)


resultado = cantidad_digitos(147852369)
print(resultado)