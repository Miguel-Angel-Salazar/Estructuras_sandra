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