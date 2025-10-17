from clase_lista_doble import Node, DoublyLinkedList

# ==================cambios=====================================
class Vehiculo:
    def __init__(self, placa, tipo, prioridad, año):
        self.placa = placa
        self.tipo = tipo
        self.prioridad = prioridad
        self.año = año

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
                # Desconectar nodo actual
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current is self.via.tail:
                    self.via.tail = current.prev

                # Mover al inicio
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

            if vehiculo.tipo == "camion" and vehiculo.prioridad > 3:
                if current is self.via.head:
                    self.via.popfirst()
                elif current is self.via.tail:
                    self.via.pop()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
            current = nxt

    def simular_accidente(self, placa1, placa2):
        nodo1 = None
        nodo2 = None
        current = self.via.head

        while current:
            if current.value.placa == placa1:
                nodo1 = current
            elif current.value.placa == placa2:
                nodo2 = current
            current = current.next

        if nodo1 is None or nodo2 is None or nodo1 is nodo2:
            return 0

        primero, segundo = None, None
        current = self.via.head
        while current:
            if current is nodo1:
                primero, segundo = nodo1, nodo2
                break
            elif current is nodo2:
                primero, segundo = nodo2, nodo1
                break
            current = current.next

        if primero.next is segundo:
            return 0

        removidos = 0
        nodo_intermedio = primero.next

        while nodo_intermedio and nodo_intermedio is not segundo:
            removidos += 1
            nodo_intermedio = nodo_intermedio.next

        primero.next = segundo
        segundo.prev = primero
        self.via.size -= removidos

        return removidos

    def invertir_via(self):
        auto = 0
        moto = 0
        current = self.via.head
        while current:
            if current.value.tipo == "auto":
                auto += 1
            elif current.value.tipo == "moto":
                moto += 1
            current = current.next

        if auto <= moto:
            return False

        current = self.via.head
        prev_nodo = None

        while current is not None:
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
                nxt = nxt.next
            current = current.next

    def mover_nuevos_al_principio(self, año_referencia=2020):
        current = self.via.head
        while current:
            nxt = current.next
            vehiculo = current.value

            if vehiculo.año > año_referencia and current is not self.via.head:
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

    def intercambiar_prioridades_extremas(self):
        if self.via.head is None:
            return

        menor = mayor = self.via.head
        current = self.via.head

        while current:
            if current.value.prioridad < menor.value.prioridad:
                menor = current
            if current.value.prioridad > mayor.value.prioridad:
                mayor = current
            current = current.next

        menor.value, mayor.value = mayor.value, menor.value

    def validar_autos_motos_y_final(self):
        autos = 0
        motos = 0
        current = self.via.head

        while current:
            if current.value.tipo == "auto":
                autos += 1
            elif current.value.tipo == "moto":
                motos += 1
            current = current.next

        if autos <= motos:
            print("❌ No hay más autos que motos.")
        elif self.via.tail and self.via.tail.value.tipo == "camion":
            print("❌ El último vehículo no puede ser camión.")
        else:
            print("✅ Condición cumplida: más autos que motos y último no es camión.")

    def mover_camiones_al_final(self):
        if not self.via.head:
            return

        current = self.via.head
        cola = self.via.tail  # referencia fija al final original

        while current is not None:
            nxt = current.next
            vehiculo = current.value

            # mover solo si es camion y no está ya al final
            if vehiculo.tipo == "camion" and current != self.via.tail:
                nodo_mover = current

                # --- Desconectar el nodo ---
                if nodo_mover.prev:
                    nodo_mover.prev.next = nodo_mover.next
                else:
                    self.via.head = nodo_mover.next

                if nodo_mover.next:
                    nodo_mover.next.prev = nodo_mover.prev

                # --- Conectar al final ---
                nodo_mover.prev = self.via.tail
                nodo_mover.next = None
                self.via.tail.next = nodo_mover
                self.via.tail = nodo_mover

            current = nxt


# --- CASOS DE USO ---
simulacion = Via()
simulacion.insertar_vehiculos("AAA111", "auto", 3, 2018)
simulacion.insertar_vehiculos("BBB222", "moto", 1, 2020)
simulacion.insertar_vehiculos("CCC333", "camion", 4, 2005)
simulacion.insertar_vehiculos("DDD444", "moto", 1, 2001)
simulacion.insertar_vehiculos("EEE555", "auto", 2, 2023)
simulacion.insertar_vehiculos("FFF666", "auto", 2, 2025)
simulacion.insertar_vehiculos("CCC353", "camion", 4, 2005)
simulacion.insertar_vehiculos("GGG666", "auto", 2, 2020)

simulacion.mover_camiones_al_final()
print("\ncamion al final :")
current = simulacion.via.head
while current:
    print(current.value)
    current = current.next


