def formas_escalera(n, actual=0):
    if actual == n:
        return 1
    if actual > n:
        return 0
    return formas_escalera(n, actual + 1) + formas_escalera(n, actual + 2)

print(formas_escalera(1))
print(formas_escalera(3))
print(formas_escalera(4))
print(formas_escalera(6))


def generar_recomendaciones_n(productos, n, categoria=None, i=0, detener=False):
    """
    Genera n recomendaciones de productos.
    Si se especifica categoria, filtra por esa categoría.
    Permite detener la generación cuando se desee.
    """
    if detener or i >= len(productos) or n <= 0:
        return []
    
    producto_actual = productos[i]
    cumple_criterio = categoria is None or producto_actual["categoria"].lower() == categoria.lower()
    
    if cumple_criterio:
        resto = generar_recomendaciones_n(productos, n - 1, categoria, i + 1, detener)
        return [producto_actual] + resto
    else:
        return generar_recomendaciones_n(productos, n, categoria, i + 1, detener)