from practica.clase_BT import BinaryTreeNode,root, printTree
from practica.clase_queue import Queue


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
    self.atendidos = 0  # 🆕 contador de pacientes atendidos


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
    self.atendidos += 1  # 🆕 Incrementa contador de atendidos

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

  # 🆕 CAMBIO 1: Reporte de pacientes registrados y atendidos
  def reporte(self):
    print(f"\n📋 Reporte de pacientes:")
    print(f"Total registrados: {self.tamano + self.atendidos}")
    print(f"En espera: {self.tamano}")
    print(f"Atendidos: {self.atendidos}")

  # 🆕 CAMBIO 2: Reasignar nivel de emergencia (actualizar prioridad)
  def reasignar_emergencia(self, id, nuevo_nivel):
    if self.raiz is None:
      print("No hay pacientes registrados.")
      return

    # Buscar el paciente por id
    q = Queue()
    q.enqueue(self.raiz)
    encontrado = None
    while not q.is_empty():
      n = q.dequeue()
      if n.data.id == id:
        encontrado = n
        break
      if n.leftchild:
        q.enqueue(n.leftchild)
      if n.rightchild:
        q.enqueue(n.rightchild)

    if encontrado is None:
      print("Paciente no encontrado.")
      return

    # Actualizar nivel y reorganizar
    print(f"\n🔄 Reasignando emergencia de {encontrado.data.nombre}: {encontrado.data.nivel} ➜ {nuevo_nivel}")
    encontrado.data.nivel = nuevo_nivel
    self.subir_heap(encontrado)
    self.bajar_heap(encontrado)
    print("Prioridades actualizadas correctamente.")


hospital = SistemaHospital()
hospital.registrar_paciente(Paciente(1, "Ana", 3, 1))
hospital.registrar_paciente(Paciente(2, "Luis", 1, 2))
hospital.registrar_paciente(Paciente(3, "Marta", 2, 3))
hospital.registrar_paciente(Paciente(4, "Carlos", 1, 4))
hospital.registrar_paciente(Paciente(5, "Sofía", 5, 5))

print("\nPacientes en espera:")
hospital.ver_lista()

hospital.reporte()  # 🆕 Reporte

hospital.ver_siguiente()
hospital.atender_paciente()
hospital.reporte()  # 🆕 Reporte actualizado

# 🆕 Cambiar prioridad (por id)
hospital.reasignar_emergencia(5, 1)  # Sofía pasa a emergencia máxima
print("\nHeap reorganizado:")
printTree(hospital.raiz)
hospital.ver_siguiente()
