productos = [
    { "codigo": "002","nombre":"areta","categoria":"accesorio","precio":1000000},
    { "codigo": "002","nombre":"cadena","categoria":"accesorio","precio":100000},
    { "codigo": "003","nombre":"gorra","categoria":"accesorio","precio":45000},
    { "codigo": "004","nombre":"hot wheels","categoria":"juguetes","precio":10000},
    { "codigo": "005","nombre":"jaron","categoria":"artesania","precio":75000},
    { "codigo": "006","nombre":"muñeco de madera","categoria":"artesania","precio":15000},
    { "codigo": "007","nombre":"pantalon","categoria":"ropa","precio":35000},
    { "codigo": "008","nombre":"trompo","categoria":"juguetes","precio":7000},
]


def busqueda_producto(productos, nombre, i=0, final=None):
    if final is None:
        final = len(productos) - 1
    if i > final:
        return None
    inmitad = (i + final) // 2

    if productos[inmitad]["nombre"].lower() == nombre.lower():
        return productos[inmitad]
    if nombre.lower() < productos[inmitad]["nombre"].lower():
        return busqueda_producto(productos, nombre, i, inmitad - 1)
    else:
        return busqueda_producto(productos, nombre, inmitad + 1, final)


def calculo_total(productos, i=0, cont=0):
    if i == len(productos):
        return cont
    return calculo_total(productos, i + 1, cont + productos[i]["precio"])


def calculo_precio_promedio(productos, categoria, i=0, suma=0, cont1=0):
    if i == len(productos):
        if cont1 == 0:
            return 0
        return round(suma / cont1)
    if productos[i]["categoria"].lower() == categoria.lower():
        return calculo_precio_promedio(productos, categoria, i + 1, suma + productos[i]["precio"], cont1 + 1)
    else:
        return calculo_precio_promedio(productos, categoria, i + 1, suma, cont1)


def particionar(lista, pivote, i=0, menores=None, mayores=None, ascendente=True):
    if menores is None: menores = []
    if mayores is None: mayores = []

    if i == len(lista):
        return menores, mayores

    actual = lista[i]
    if ascendente:
        if actual["precio"] <= pivote["precio"]:
            menores.append(actual)
        else:
            mayores.append(actual)
    else:
        if actual["precio"] >= pivote["precio"]:
            menores.append(actual)
        else:
            mayores.append(actual)

    return particionar(lista, pivote, i + 1, menores, mayores, ascendente)


def ordenamiento_precio(productos, ascendente=True):
    if len(productos) <= 1:
        return productos
    pivote = productos[0]
    menores, mayores = particionar(productos[1:], pivote, ascendente=ascendente)
    return ordenamiento_precio(menores, ascendente) + [pivote] + ordenamiento_precio(mayores, ascendente)


def busqueda_de_rangos(productos, minimo, maximo, i=0):
    if i == len(productos):
        return []
    resto = busqueda_de_rangos(productos, minimo, maximo, i + 1)
    if minimo <= productos[i]["precio"] <= maximo:
        return [productos[i]] + resto
    else:
        return resto


def generar_recomenda(productos, categoria, i=0):
    if i == len(productos):
        return []
    resto = generar_recomenda(productos, categoria, i + 1)
    if productos[i]["categoria"].lower() == categoria.lower():
        return [productos[i]] + resto
    else:
        return resto



def imprimir_lista(productos, i=0):
    if i == len(productos):
        return
    print(f"- {productos[i]['nombre'].title()} | ${productos[i]['precio']}")
    imprimir_lista(productos, i + 1)


if __name__ == "__main__":
    print("="*40)
    print("🔍 BÚSQUEDAS")
    print("="*40)
    for nombre in ["gorra", "areta", "cadena", "trompo"]:
        p = busqueda_producto(productos, nombre)
        if p:
            print(f"- {p['nombre'].title()} | ${p['precio']}")
        else:
            print(f"- {nombre} no encontrado")

    print("\n" + "="*40)
    print("PRECIO TOTAL")
    print("="*40)
    print(f"Total: ${calculo_total(productos)}")

    print("\n" + "="*40)
    print("PROMEDIOS POR CATEGORÍA")
    print("="*40)
    print(f"Ropa: ${calculo_precio_promedio(productos, 'ropa')}")
    print(f"Accesorio: ${calculo_precio_promedio(productos, 'accesorio')}")
    print(f"Juguetes: ${calculo_precio_promedio(productos, 'juguetes')}")
    print(f"Artesania: ${calculo_precio_promedio(productos, 'artesania')}")

    print("\n" + "="*40)
    print("ORDENAMIENTO ASCENDENTE")
    print("="*40)
    imprimir_lista(ordenamiento_precio(productos, ascendente=True))

    print("\n" + "="*40)
    print("ORDENAMIENTO DESCENDENTE")
    print("="*40)
    imprimir_lista(ordenamiento_precio(productos, ascendente=False))

    print("\n" + "="*40)
    print("PRODUCTOS EN RANGO (10000 - 80000)")
    print("="*40)
    imprimir_lista(busqueda_de_rangos(productos, 10000, 80000))

    print("\n" + "="*40)
    print("RECOMENDACIONES (Categoría: 'juguetes')")
    print("="*40)
    imprimir_lista(generar_recomenda(productos, "juguetes"))
