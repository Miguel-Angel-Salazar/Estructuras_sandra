from clase_lista_doble import Node, DoublyLinkedList

class Vehiculo:
  def __init__(self, placa, tipo, prioridad):
    self.placa: str = placa
    self.tipo: str = tipo
    self.prioridad: int = prioridad

  def __str__(self):
    return f"{self.placa}: {self.tipo}:{self.prioridad}"


class Via:
  def __init__(self):
    self.via = DoublyLinkedList()

  def insertar_vehiculos(self, placa, tipo, prioridad):
    vehiculo = Vehiculo(placa, tipo, prioridad)
    self.via.append(vehiculo)


  def paso_preferencial(self):
    current = self.via.head
    while current is not None:
      nxt = current.next
      vehiculo = current.value

      if vehiculo.tipo == "moto" and vehiculo.prioridad == 1 and current is not self.via.head:
        if current.prev:
          current.prev.next = current.next
        if current.next:
          current.next.prev = current.prev
        if current is self.via.tail:
          self.via.tail = current.prev

        current.prev = None
        current.next = self.via.head
        self.via.head.prev = current
        self.via.head = current

      current = nxt
  def eliminar_camiones(self):
    current = self.via.head
    while current is not None:
      nxt = current.next
      vehiculo = current.value

      if vehiculo.tipo == "camion" and vehiculo.prioridad > 3 :
          if current is self.via.head:
              self.via.popfirst()
          elif current is self.via.tail:
              self.via.pop()

          else:
              current.prev.next = current.next
              current.next.prev = current.prev

      current = nxt

  def simular_accidente(self):



    pass

  def invertir_via(self):
    auto = 0
    moto = 0
    current = self.via.head
    for current in self.via:
      if current.value.tipo == "auto":
          auto += 1
      elif current.value.tipo == "moto":
          moto += 1
    if auto <= moto:
        return False

    current = self.via.head
    prev_nodo = None

    while current is not None :
      next_nodo = current.next

      current.next = prev_nodo

      current.prev = next_nodo
      prev_nodo = current
      current = next_nodo

    self.via.tail = self.via.head
    self.via.head = prev_nodo


  def reorganizar_via(self):
      if self.via.head is None:
          return
      current = self.via.head
      while current:
            nxt = current.next
            while nxt:
              if current.value.prioridad > nxt.value.prioridad:
                current.value, nxt.value = nxt.value, current.value
              nxt=nxt.next
            current= current.next




simulacion = Via()
simulacion.insertar_vehiculos("AAA111", "auto", 3)
simulacion.insertar_vehiculos("BBB222", "moto", 1)
simulacion.insertar_vehiculos("CCC333", "camion", 4)
simulacion.insertar_vehiculos("DDD444", "moto", 1)
simulacion.insertar_vehiculos("EEE555", "auto", 2)
simulacion.insertar_vehiculos("FFF666", "auto", 2)

print("\nvia:")
current = simulacion.via.head
while current:
    print(current.value)
    current = current.next

simulacion.paso_preferencial()
print("\npaso preferencial:")
current = simulacion.via.head
while current:
    print(current.value)
    current = current.next

simulacion.eliminar_camiones()
print("\nEliminar camion > 3:")
current = simulacion.via.head
while current:
    print(current.value)
    current = current.next

simulacion.simular_accidente()
print("\nAccidente en la regional:")
current = simulacion.via.head
while current:
    print(current.value)
    current = current.next

simulacion.invertir_via()
print("\nInvertir :")
current = simulacion.via.head
while current:
    print(current.value)
    current = current.next

simulacion.reorganizar_via()
print("\nReorganizar:")
current = simulacion.via.head
while current:
    print(current.value)
    current = current.next