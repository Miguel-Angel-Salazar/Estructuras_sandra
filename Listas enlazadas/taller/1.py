from clase_lista_doble import Node, DoublyLinkedList

class TrainManager:
    def __init__(self):
        self.train = DoublyLinkedList()
        self.current = None
        self.start_train()


    def start_train(self):
        self.train.append("Vagón 1")
        self.current = self.train.head


    def siguiente(self):
        if self.current and self.current.next:
            self.current = self.current.next



    def anterior(self):
        if self.current and self.current.prev:
            self.current = self.current.prev


    def acoplar(self, name):
        if self.current is None:
            raise Exception("No hay vagón actual. El tren está vacío.")

        new_wagon = Node(name)
        next_node = self.current.next

        self.current.next = new_wagon
        new_wagon.prev = self.current

        if next_node:
            new_wagon.next = next_node
            next_node.prev = new_wagon
        else:
            self.train.tail = new_wagon

        self.train.size += 1

    def desacoplar(self):
        if self.current is None:
            raise Exception("El tren está vacío. No se puede eliminar.")

        prev_node = self.current.prev
        next_node = self.current.next

        if prev_node:
            prev_node.next = next_node
        else:
            self.train.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.train.tail = prev_node

        if next_node:
            self.current = next_node
        elif prev_node:
            self.current = prev_node
        else:
            self.current = None
            self.train.head = None
            self.train.tail = None
            self.train.size = 0
            return

        self.train.size -= 1

    def mover_inicio(self):
        if self.current is None:
            raise Exception("El tren está vacío.")
        valor = self.current.value
        self.desacoplar()
        self.train.prepend(valor)
        self.current = self.train.head

    def mover_final(self):
        if self.current is None:
            raise Exception("El tren está vacío.")
        valor = self.current.value
        self.desacoplar()
        self.train.append(valor)
        self.current = self.train.tail

manager = TrainManager()
print("Inicial:", manager.train, " | Actual:", manager.current)
manager.acoplar("Vagón 2")
print("Después de acoplar V2:", manager.train, " | Actual:", manager.current)
manager.acoplar("Vagón 3")
print("Después de acoplar V3:", manager.train, " | Actual:", manager.current)
manager.siguiente()
print("Mover siguiente:", manager.train, " | Actual:", manager.current)
manager.anterior()
print("Mover anterior:", manager.train, " | Actual:", manager.current)
manager.desacoplar()
print("Después de eliminar actual:", manager.train, " | Actual:", manager.current)
manager.mover_final()
print("Mover actual al final:", manager.train, " | Actual:", manager.current)
manager.mover_inicio()
print("Mover actual al inicio:", manager.train, " | Actual:", manager.current)