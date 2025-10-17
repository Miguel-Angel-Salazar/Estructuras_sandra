class Vehiculo:
    def __init__(self, placa, tipo, prioridad, año):
        self.placa: str = placa
        self.tipo: str = tipo
        self.prioridad: int = prioridad
        self.año: int = año

    def __str__(self):
        return f"{self.placa}: {self.tipo}:{self.prioridad}:{self.año}"


class Via:
    def __init__(self):
        self.via = DoublyLinkedList()

    def insertar_vehiculos(self, placa, tipo, prioridad, año):
        vehiculo = Vehiculo(placa, tipo, prioridad, año)
        self.via.append(vehiculo)

    def paso_preferencial(self):
        current = self.via.head
        while current is not None:
            nxt = current.next
            vehiculo = current.value

            if vehiculo.tipo == "moto" and vehiculo.prioridad == 1 and current is not self.via.head:
                # Desconectamos el nodo actual
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev

                if current is self.via.tail:
                    self.via.tail = current.prev

                # Movemos el nodo al frente
                current.prev = None
                current.next = self.via.head
                self.via.head.prev = current
                self.via.head = current

            current = nxt

    def mover_antiguos_al_final(self, año_referencia):
        current = self.via.head

        while current is not None:
            nxt = current.next
            vehiculo = current.value

            # si el año es menor o igual al año de referencia y no está al final
            if vehiculo.año <= año_referencia and current is not self.via.tail:

                # desconectamos el nodo actual
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.via.head = current.next

                if current.next:
                    current.next.prev = current.prev

                # conectamos el nodo al final
                current.prev = self.via.tail
                current.next = None
                self.via.tail.next = current
                self.via.tail = current

            current = nxt

simulacion = Via()
simulacion.insertar_vehiculos("BBB222", "moto", 1, 2010)
simulacion.insertar_vehiculos("AAA111", "auto", 3, 2020)
simulacion.insertar_vehiculos("FFF666", "auto", 2, 2021)
simulacion.insertar_vehiculos("GGG666", "auto", 2, 2021)
simulacion.insertar_vehiculos("DDD444", "auto", 1, 2003)

print("Antes de mover antiguos:")
cur = simulacion.via.head
while cur:
    print(cur.value)
    cur = cur.next

simulacion.mover_antiguos_al_final(2010)

print("\nDespués de mover antiguos:")
cur = simulacion.via.head
while cur:
    print(cur.value)
    cur = cur.next

