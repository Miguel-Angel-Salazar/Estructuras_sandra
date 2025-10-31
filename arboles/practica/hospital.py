from clase_BT import BinaryTreeNode, root, printTree
from clase_queue import Queue

class Paciente:
  def __init__(self, id, nombre, nivel, llegada):
    self.id = id
    self.nombre = nombre
    self.nivel = nivel
    self.llegada = llegada

  def __str__(self):
    return f"{self.id}-{self.nombre}(Nivel:{self.nivel},Llegada:{self.llegada})"


class SistemaHospital:
  def __init__(self):
    self.raiz = None
    self.tamano = 0


  def registrar_paciente(self, paciente):
    nuevo = BinaryTreeNode(paciente)
    self.tamano += 1
    if self.raiz is None:
      self.raiz = nuevo
      return

    q = Queue()
    q.enqueue(self.raiz)

    while not q.is_empty():
      actual = q.dequeue()
      if actual.leftchild is None:
        actual.leftchild = nuevo
        break
      elif actual.rightchild is None:
        actual.rightchild = nuevo
        break
      else:
        q.enqueue(actual.leftchild)
        q.enqueue(actual.rightchild)
    self.subir_heap(nuevo)


  def subir_heap(self, nodo):
    if self.raiz == nodo:
      return

    padre = self.encontrar_padre(nodo)
    while padre and self.comparar(nodo.data, padre.data): 
      nodo.data, padre.data = padre.data, nodo.data
      nodo = padre
      padre = self.encontrar_padre(nodo)


  def encontrar_padre(self, nodo):
    if nodo == self.raiz:
      return None
    q = Queue()
    q.enqueue(self.raiz)
    while not q.is_empty():
      actual = q.dequeue()
      if actual.leftchild == nodo or actual.rightchild == nodo:
        return actual
      if actual.leftchild:
        q.enqueue(actual.leftchild)
      if actual.rightchild:
        q.enqueue(actual.rightchild)
    return None


  def comparar(self, p1, p2):
    if p1.nivel < p2.nivel:
      return True
    if p1.nivel == p2.nivel and p1.llegada < p2.llegada:
      return True
    return False


  def ver_siguiente(self):
    if self.raiz:
      print("Siguiente paciente:", self.raiz.data)
    else:
      print("No hay pacientes")


  def atender_paciente(self):
    if self.raiz is None:
      print("No hay pacientes")
      return
    print("Atendido:", self.raiz.data)
    if self.tamano == 1:
      self.raiz = None
      self.tamano = 0
      return
    q = Queue()
    q.enqueue(self.raiz)
    ultimo = None
    padre = None
    while not q.is_empty():
      actual = q.dequeue()
      if actual.leftchild:
        q.enqueue(actual.leftchild)
        padre = actual
      if actual.rightchild:
        q.enqueue(actual.rightchild)
        padre = actual
      ultimo = actual
    self.raiz.data = ultimo.data
    if padre.rightchild == ultimo:
      padre.rightchild = None
    else:
      padre.leftchild = None
    self.tamano -= 1
    self.bajar_heap(self.raiz) 

  def bajar_heap(self, nodo):
    while True:
      menor = nodo
      if nodo.leftchild and self.comparar(nodo.leftchild.data, menor.data):
        menor = nodo.leftchild
      if nodo.rightchild and self.comparar(nodo.rightchild.data, menor.data):
        menor = nodo.rightchild
      if menor == nodo:
        break
      nodo.data, menor.data = menor.data, nodo.data
      nodo = menor

  def ver_lista(self):
    if self.raiz is None:
      return
    q = Queue()
    q.enqueue(self.raiz)
    while not q.is_empty():
      n = q.dequeue()
      print(n.data)
      if n.leftchild:
        q.enqueue(n.leftchild)
      if n.rightchild:
        q.enqueue(n.rightchild)

  def ver_por_nivel(self, nivel):
    if self.raiz is None:
      return
    print("Pacientes con nivel", nivel, ":")
    q = Queue()
    q.enqueue(self.raiz)
    while not q.is_empty():
      n = q.dequeue()
      if n.data.nivel == nivel:
        print(n.data)
      if n.leftchild:
        q.enqueue(n.leftchild)
      if n.rightchild:
        q.enqueue(n.rightchild)

hospital = SistemaHospital()
hospital.registrar_paciente(Paciente(1, "Ana", 3, 1))
hospital.registrar_paciente(Paciente(2, "Luis", 1, 2))
hospital.registrar_paciente(Paciente(3, "Marta", 2, 3))
hospital.registrar_paciente(Paciente(4, "Carlos", 1, 4))
hospital.registrar_paciente(Paciente(5, "Sofía", 5, 5))

print("\nÁrbol actual (printTree):")
printTree(hospital.raiz)
print("\nPacientes en espera (LevelOrder):")
hospital.ver_lista()
print("\nSiguiente paciente:")
hospital.ver_siguiente()
print("\nAtender paciente:")
hospital.atender_paciente()
print("\nÁrbol actualizado:")
printTree(hospital.raiz)
print("\nPacientes con nivel actual:")
hospital.ver_por_nivel(1)

print("=======================================")

print("\nÁrbol actual (printTree):")
printTree(hospital.raiz)
print("\nPacientes en espera (LevelOrder):")
hospital.ver_lista()
print("\nSiguiente paciente:")
hospital.ver_siguiente()
print("\nAtender paciente:")
hospital.atender_paciente()
print("\nÁrbol actualizado:")
printTree(hospital.raiz)
print("\nPacientes con nivel actual:")
hospital.ver_por_nivel(2)