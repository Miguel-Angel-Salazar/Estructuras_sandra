class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
def pares_de_pila(pila_colas):
    nueva_pila = Stack()


    while not pila_colas.is_empty():
        cola = pila_colas.pop()

        while not cola.is_empty():
            x = cola.dequeue()
            if x % 2 == 0:
                nueva_pila.push(x)

    return nueva_pila

c1 = Queue(); [c1.enqueue(x) for x in [1,2,3,4]]
c2 = Queue(); [c2.enqueue(x) for x in [5,6,7,8]]


pila_colas = Stack()
pila_colas.push(c1)
pila_colas.push(c2)


resultado = pares_de_pila(pila_colas)


pares = []
while not resultado.is_empty():
    pares.append(resultado.pop())

print(pares)