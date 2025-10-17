def mover_antiguos_al_final(self, año_referencia=2010):
    current = self.via.head

    while current:
        nxt = current.next
        vehiculo = current.value

        # Si el vehículo es antiguo (año <= referencia) y no está al final
        if vehiculo.año <= año_referencia and current is not self.via.tail:
            # Desconectar el nodo actual de su posición
            if current.prev:
                current.prev.next = current.next
            else:
                # si era la cabeza, movemos la cabeza al siguiente
                self.via.head = current.next

            if current.next:
                current.next.prev = current.prev

            # Conectar el nodo actual al final de la lista
            current.prev = self.via.tail
            current.next = None
            self.via.tail.next = current
            self.via.tail = current

        current = nxt
      
