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
    


class Editor:
    def __init__(self):
        self.texto = ""
        self.historial = Stack()

    def append(self, s):
        self.historial.push(self.texto)
        self.texto += s

    def delete(self, k):
        self.historial.push(self.texto)
        if k > 0:
            self.texto = self.texto[:-k]

    def print(self, k):
        if 1 <= k <= len(self.texto):
            return self.texto[k-1]
        return ""

    def undo(self):
        if not self.historial.is_empty():
            self.texto = self.historial.pop()

    def process(self, ops):
        salida = []
        for op in ops:
            if op.startswith("append "):
                self.append(op.split(" ",1)[1])
            elif op.startswith("delete "):
                self.delete(int(op.split(" ",1)[1]))
            elif op.startswith("print "):
                salida.append(self.print(int(op.split(" ",1)[1])))
            elif op == "undo":
                self.undo()
        return salida



ops1 = ["append abc","append xy","print 4","delete 3","print 2","undo","print 5","undo"]
print(Editor().process(ops1))