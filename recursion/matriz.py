m1 = [[1,2,3],
      [4,1,5],
      [6,7,1]]

m2 = [[5,2,3],
      [4,5,6],
      [6,7,9]]

print(len(m1))

def validardiagonal(m1,i=0):

  if i == len(m1)-1:
    return True
  print("index : ",i)
  if m1[i][i] == m1[i+1][i+1]:
    return validardiagonal(m1,i+1)
  else:
    return False

print("matriz : ", m1)
print("diagonales iguales: " , validardiagonal(m1))


print("matriz : ", m2)
print("diagonales iguales: " , validardiagonal(m2))
