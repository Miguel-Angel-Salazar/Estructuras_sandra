class Node:
  __slots__ = ('__value','__next','__prev')

  def __init__(self,value):
    self.__value = value
    self.__next = None
    self.__prev = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,newNext):
    if newNext is not None and not isinstance(newNext,Node):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = newNext

  @property
  def prev(self):
    return self.__prev

  @prev.setter
  def prev(self,newPrev):
    if newPrev is not None and not isinstance(newPrev,Node):
      raise TypeError("prev debe ser un objeto tipo nodo ó None")
    self.__prev = newPrev

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue


class DoublyLinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @head.setter
  def head(self,newHead):
    if newHead is not None and not isinstance(newHead,Node):
      raise TypeError("Head debe ser un objeto tipo nodo ó None")
    self.__head = newHead

  @property
  def tail(self):
    return self.__tail

  @tail.setter
  def tail(self,newTail):
    if newTail is not None and not isinstance(newTail,Node):
      raise TypeError("Tail debe ser un objeto tipo nodo ó None")
    self.__tail = newTail

  @property
  def size(self):
    return self.__size

  @size.setter
  def size(self, newSize):
    if not isinstance(newSize, int):
      raise TypeError("El tamaño debe ser un objeto tipo numerico entero")
    self.__size = newSize

  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def prepend(self, value):
    newnode = Node(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      newnode.next = self.__head
      self.__head.prev = newnode
      self.__head = newnode
    self.__size += 1

  def append(self,value):
    newnode = Node(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode
      newnode.prev = self.__tail
      self.__tail = newnode
    self.__size += 1
#===========================================================
  def rotar_maximo(self):
      if self.__head is None or self.__head == self.__tail:
          return
      max_node = self.__head
      current = self.__head
      while current:
          if current.value > max_node.value:
              max_node = current
          current = current.next
      while self.__head != max_node:
          last = self.__tail
          second_last = last.prev
          second_last.next = None
          self.__tail = second_last
          last.prev = None
          last.next = self.__head
          self.__head.prev = last
          self.__head = last

dll = DoublyLinkedList()
dll.append(3)
dll.append(7)
dll.append(2)
dll.append(9)
dll.append(5)

print("Original:", dll)
dll.rotar_maximo()
print("Rotada :", dll)