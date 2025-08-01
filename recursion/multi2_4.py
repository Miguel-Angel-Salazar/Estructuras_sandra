def contar_multiplos_de_2_y_4(n):
    if n == 0:
        return 0
    
    digito = n % 10 
    
    if digito in [4, 8]:
        return 1 + contar_multiplos_de_2_y_4(n // 10)
    else:
        return contar_multiplos_de_2_y_4(n // 10)

print(contar_multiplos_de_2_y_4(84082))  




# profe

a = 34523
b = 84082

def contarmultiplos(num,cont=0):

  if num == 0:
    return cont

  digito = num%10

  if digito != 0 and digito%4 == 0:
      return contarmultiplos(num//10,cont+1)
  else:
      return contarmultiplos(num//10,cont)

print(f"el numero {a} tiene {contarmultiplos(a)} multiplos")
print(f"el numero {b} tiene {contarmultiplos(b)} multiplos")