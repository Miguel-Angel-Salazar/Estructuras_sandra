class Queue:

  def __init__(self):
    self.__items = []


  def enqueue(self,e):
    self.__items.append(e)
    return True

  def dequeue(self):
    if self.is_empty():
      return "Error, no hay elementos para retornar"

    return self.__items.pop(0)

  def is_empty(self):
    return len(self.__items) == 0

  def len(self):
    return len(self.__items)

  def first(self):
     if self.is_empty():
      return "Error, no hay elementos para retornar"

     return self.__items[0]

  def __str__(self):
    return '--'.join(map(str,self.__items))

customq = Queue()
customq.enqueue(20)
customq.enqueue(50)
customq.enqueue(10)

print("elementos en la cola : ", customq.len())

print("cola : ", customq)

print("desencolar : ",customq.dequeue())

print("cola despues de desencolar : ", customq)

print("siguiente en la cola")