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
    
class Router:
    def __init__(self, memoryLimit):
        self.limit = memoryLimit
        self.cola = Queue()

    def addPacket(self, s, d, t):
        nuevo = [s, d, t]


        for pkt in self.cola.items:
            if pkt == nuevo:
                return False


        if self.cola.size() >= self.limit:
            self.cola.dequeue()


        self.cola.enqueue(nuevo)
        return True

    def forwardPacket(self):
        if not self.cola.is_empty():
            return self.cola.dequeue()
        return []

    def getCount(self, destino, t1, t2):
        count = 0
        for s, d, t in self.cola.items:
            if d == destino and t1 <= t <= t2:
                count += 1
        return count



r = Router(3)
print(r.addPacket(1, 2, 10))
print(r.addPacket(1, 2, 10))
print(r.addPacket(2, 3, 11))
print(r.addPacket(3, 4, 12))
print(r.addPacket(4, 5, 13))
print(r.forwardPacket())
print(r.getCount(5, 10, 20))