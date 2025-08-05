def decodificar(s, i=0):
    if len(s) == 0:
        return ""

    if i < len(s) and s[i].isdigit():
        return decodificar(s, i + 1)
    k = int(s[:i])

    ini = s.find('[', i)
    fin = s.find(']', ini)
    texto = s[ini+1:fin]

    return texto * k + decodificar(s[fin+1:])


print(decodificar("3[a]2[bc]"))
print(decodificar("4[ab]"))
