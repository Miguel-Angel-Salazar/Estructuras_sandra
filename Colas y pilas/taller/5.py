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
    
def profundidad(cadena):
    pila = Stack()
    max_prof = 0

    for c in cadena:
        if c == '(':
            pila.push(c)
            if pila.size() > max_prof:
                max_prof = pila.size()
        elif c == ')':
            pila.pop()

    return max_prof


print(profundidad("(1+(2*3)+((8)/4))+1"))
print(profundidad("(1)+((2))+(((3)))"))