def formas_escalera(n):
    if n < 0:
        return 0
    if n == 0:
      return 1
    else:
        return formas_escalera(n - 1) + formas_escalera(n - 2)

print(formas_escalera(1))
print(formas_escalera(3))
print(formas_escalera(4))
print(formas_escalera(5))