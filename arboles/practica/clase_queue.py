from clase_BT import BinaryTreeNode, root, printTree

class Queue():

  def __init__(self):
    self.__list = []

  def __str__(self):
    return '--'.join(map(str,self.__list))


  def enqueue(self,e):
    self.__list.append(e)
    return True

  def dequeue(self):
    if self.is_empty():
      return "Error no es posible desencolar, no hay elementos"

    return self.__list.pop(0)

  def first(self):
    if self.is_empty():
      return "Error no es posible leer el primer elemento, no hay elementos"

    return self.__list[0]


  def is_empty(self):
    return len(self.__list) == 0

  def len(self):
    return len(self.__list)



def LevelOrder(root):
   if root is None:
    return

   auxqueue = Queue()
   auxqueue.enqueue(root)

   while not auxqueue.is_empty():
    tempRoot = auxqueue.dequeue()
    print(tempRoot.data)

    if tempRoot.leftchild:
      auxqueue.enqueue(tempRoot.leftchild)

    if tempRoot.rightchild:
      auxqueue.enqueue(tempRoot.rightchild)


print("Arbol con printTree")
print("\n")
printTree(root)
print("\n")
print("Arbol con recorrido LevelOrder")
LevelOrder(root)