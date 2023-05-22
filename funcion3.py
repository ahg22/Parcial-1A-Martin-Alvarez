def ordenarCaracteres(avion):
    ordenados=sorted(avion)
    ordenados = ''.join(ordenados)
    return ordenados

caracteres_ordenados=ordenarCaracteres("avion")

print("El caracter ordenado es:", caracteres_ordenados)