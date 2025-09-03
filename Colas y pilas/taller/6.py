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
    
def evaluar_postfija(s):
    pila = Stack()
    for token in s:
        if token.isdigit():
            pila.push(int(token))
        else:
            segundo = pila.pop()
            primero = pila.pop()

            if token == '+':
                resultado = primero + segundo
            elif token == '-':
                resultado = primero - segundo
            elif token in ['x', '*']:
                resultado = primero * segundo
            elif token == '/':
                resultado = primero // segundo

            pila.push(resultado)

    return pila.pop()


print(evaluar_postfija("25+"))
print(evaluar_postfija("43+"))
print(evaluar_postfija("35x83+-"))