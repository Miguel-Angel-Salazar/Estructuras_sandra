class Stack:

  def __init__(self):
    self.__items = []

  def push(self,e):
    self.__items.append(e)
    return True

  def pop(self):
    return self.__items.pop()
  
  def is_empty(self):
    return len(self.__items) == 0
  
def invertircadena(cadena):

    customs = Stack()

    for c in cadena:
        customs.push(c)

    print("pila :", customs)

    newcadena = ""

    while not customs.is_empty():
        newcadena

    cadena = "Hola"
    print(invertircadena(cadena))
