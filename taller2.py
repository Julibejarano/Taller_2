"""Taller 2 de análisis de algoritmos"""
def boolean_rep(s):
    """Función principal"""
    if s == 0:
        return 0
    if s == 1:
        return 1
    cantbits = cantidad(s)
    return boolean_rep_aux(s, 0, cantbits - 1)

def cantidad(s):
    """Retorna la cantidad de bits"""
    cantbits = 0
    while s >> cantbits:
        cantbits += 1
    return cantbits

def boolean_rep_aux(s, b, e):
    """Complemento de la principal"""
    #Caso base
    if b == e:
        return str((s >> b) & 1)
    q = (b+e) // 2
    R = boolean_rep_aux(s, q+1, e)
    L = boolean_rep_aux(s, b, q)
    return R + L

s = int(input('Ingrese el número: '))
print(f"La representación booleana del número es {boolean_rep(s)}")
