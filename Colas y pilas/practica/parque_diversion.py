from pila import Stack
from cola import Queue


class Atraccion:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.visitantes = Stack()

    def __str__(self):
        return f"{self.nombre} (capacidad {self.capacidad})"



class ParqueDiversiones:
    def __init__(self):
        self.atracciones = Queue()


        self.atracciones.enqueue(Atraccion("Montaña Rusa", 3))
        self.atracciones.enqueue(Atraccion("Carros Chocones", 2))
        self.atracciones.enqueue(Atraccion("Rueda de la Fortuna", 2))
        self.atracciones.enqueue(Atraccion("Casa del Terror", 2))


    def agregar_visitante(self, visitante):
        primera = self.atracciones.first()
        primera.visitantes.push(visitante)


    def procesar_atraccion(self, atracciones, index=0, visitantes_entrantes=None):
        if index >= atracciones.len():
            return

        atraccion = atracciones.dequeue()
        atracciones.enqueue(atraccion)


        if visitantes_entrantes:
            while not visitantes_entrantes.is_empty():
                atraccion.visitantes.push(visitantes_entrantes.pop())


        procesados = Stack()
        for _ in range(atraccion.capacidad):
            if atraccion.visitantes.is_empty():
                break
            procesados.push(atraccion.visitantes.pop())


        print(f"\n[{atraccion.nombre}]")
        print(" Procesados:", procesados if not procesados.is_empty() else "Ninguno")
        print(" En espera:", atraccion.visitantes)


        self.procesar_atraccion(atracciones, index + 1, procesados)


    def ejecutar_turno(self):
        print("\n=== Ejecutando turno ===")
        self.procesar_atraccion(self.atracciones)


    def eliminar_atraccion(self, nombre):
        nueva_cola = Queue()
        atraccion_eliminada = None
        while not self.atracciones.is_empty():
            atr = self.atracciones.dequeue()
            if atr.nombre == nombre:
                atraccion_eliminada = atr
            else:
                nueva_cola.enqueue(atr)


        if atraccion_eliminada:
            if not nueva_cola.is_empty():
                siguiente = nueva_cola.first()
                while not atraccion_eliminada.visitantes.is_empty():
                    siguiente.visitantes.push(atraccion_eliminada.visitantes.pop())
            print(f"Atracción {nombre} eliminada y visitantes redistribuidos.")
        else:
            print(f"Atracción {nombre} no encontrada.")

        self.atracciones = nueva_cola


    def agregar_atraccion(self, nombre, capacidad):
        self.atracciones.enqueue(Atraccion(nombre, capacidad))
        print(f"Atracción {nombre} agregada con capacidad {capacidad}.")


    def mostrar_estado(self):
        print("\n=== Estado del Parque ===")
        self._mostrar_estado_rec(self.atracciones, self.atracciones.len())

    def _mostrar_estado_rec(self, atracciones, n):
        if n == 0:
            return
        atr = atracciones.dequeue()
        print(f"{atr.nombre}: {atr.visitantes}")
        atracciones.enqueue(atr)
        self._mostrar_estado_rec(atracciones, n - 1)



if __name__ == "__main__":
    parque = ParqueDiversiones()


    for v in ["A1", "N1", "A2", "N2", "A3", "A4", "N3"]:
        parque.agregar_visitante(v)

    parque.mostrar_estado()


    parque.ejecutar_turno()
    parque.ejecutar_turno()
    parque.ejecutar_turno()


    parque.eliminar_atraccion("Rueda de la Fortuna")
    parque.mostrar_estado()


    parque.agregar_atraccion("Simulador 4D", 2)
    parque.mostrar_estado()