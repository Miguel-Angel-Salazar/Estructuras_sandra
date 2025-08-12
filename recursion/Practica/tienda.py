class TiendaSouvenirs:
    def __init__(self):
        self.productos = [
            {"codigo": "A001", "nombre": "Artesanía de madera", "categoria": "artesanías", "precio": 25000},
            {"codigo": "C002", "nombre": "Camisa turística", "categoria": "ropa", "precio": 40000},
            {"codigo": "C003", "nombre": "Collar artesanal", "categoria": "accesorios", "precio": 15000},
            {"codigo": "G004", "nombre": "Gorra bordada", "categoria": "ropa", "precio": 30000},
            {"codigo": "I005", "nombre": "Imán de la ciudad", "categoria": "imanes", "precio": 8000},
            {"codigo": "J006", "nombre": "Jarra pintada a mano", "categoria": "artesanías", "precio": 28000},
            {"codigo": "L007", "nombre": "Llaveros artesanales", "categoria": "accesorios", "precio": 12000},
            {"codigo": "P008", "nombre": "Poncho típico", "categoria": "ropa", "precio": 50000},
            {"codigo": "S009", "nombre": "Sombrero vueltiao", "categoria": "ropa", "precio": 35000},
            {"codigo": "T010", "nombre": "Taza con diseño local", "categoria": "artesanías", "precio": 10000}
        ]

    def buscar_producto(self, nombre, inicio=0, fin=None):
        if fin is None:
            fin = len(self.productos) - 1
        pass

    def calcular_precio_total(self, indice=0, total=0):
        pass

    def promedio_categoria(self, categoria, indice=0, total=0, cantidad=0):
        pass

    def ordenar_por_precio(self, lista=None, ascendente=True):
        if lista is None:
            lista = self.productos
        pass

    def buscar_en_rango(self, minimo, maximo, indice=0, encontrados=None):
        if encontrados is None:
            encontrados = []
        pass

    def recomendar_por_categoria(self, nombre_producto, indice=0, categoria=None, recomendaciones=None):
        if recomendaciones is None:
            recomendaciones = []
        pass


tienda = TiendaSouvenirs()
print(tienda.productos)
