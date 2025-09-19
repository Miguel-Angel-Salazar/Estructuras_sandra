import random

class Stack:

  def __init__(self):
    self.__items = []

  def push(self,e):
    self.__items.append(e)
    return True

  def pop(self):
    if self.is_empty():
      return "Error, no hay elementos para retornar"

    return self.__items.pop()

  def is_empty(self):
    return len(self.__items) == 0

  def len(self):
    return len(self.__items)

  def top(self):
     if self.is_empty():
      return "Error, no hay elementos para retornar"

     return self.__items[-1]

  def __str__(self):
    return '--'.join(map(str,reversed(self.__items)))

  def generate(self,num, min, max):
   for i in range(0,num):
    self.push(random.randint(min,max))


customs = Stack()
customs.push(40)
customs.push(50)
customs.push(10)

print("elementos en la pila : ", customs.len())
print("pila : ", customs)

print("desapilar: ",customs.pop())
print("siguiente en la pila: ",customs.top())
print("pila : ", customs)