def vocales_consonantes(p1,conta_voccal=0,conta_consotante=0,i=0):
    if i == len(p1):
        if conta_voccal == conta_consotante:
            return "cantidad igual"
        elif conta_voccal > conta_consotante:
            return "mas vocales"
        else:
            return "mas consonantes"
    if p1[i] in l1:
        return vocales_consonantes(p1,conta_voccal +1, conta_consotante, i +1)
    else:
        return vocales_consonantes(p1, conta_voccal, conta_consotante +1, i+1)


p1 ="arbol"

l1=["a","e","i","o","u"]

print(f"la palabra {p1} tiene {vocales_consonantes(p1)}")