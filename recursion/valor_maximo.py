lista = [11,2,4,7,19,3]

def buscarmaximo(l1):

  if len(l1) == 1:
    return l1[0]

  return max(l1[0],buscarmaximo(l1[1:]))

print("el maximo es", buscarmaximo(lista))

def buscarmaximo2(l1,i=0):

  if len(l1)-1 == i:
    return l1[i]

  return max(l1[i],buscarmaximo2(l1,i+1))

print("2 - el maximo es", buscarmaximo2(lista))

def buscarmaximo3(l1,i=0):

  if len(l1)-1 == i:
    return l1[i]

  resto = buscarmaximo3(l1,i+1)
  return l1[i] if l1[i] > resto else resto

print("3 - el maximo es", buscarmaximo3(lista))