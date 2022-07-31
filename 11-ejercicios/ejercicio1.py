numeros=[12, 15, 8, 5, 3, 1, 8, 10]

def mostrarlista(lista):
    resultado=""
    for elemento in lista:
        resultado+= str(elemento)
        resultado+="\n"
    return resultado

print(mostrarlista(numeros))


numeros.sort()
print(mostrarlista(numeros))

print(len(numeros))

busqueda= int(input("introduce el numero: "))

comprobar= isinstance(busqueda, int)
while not comprobar or busqueda<=0:
    busqueda= int(input("introduce en numero: "))
else:
        print(f"has introducido el {busqueda}")

print(f"####### buscar en la lista el numero {busqueda} #######")

search = numeros.index(busqueda)
print(f"el numero buscado existe en la lista, es el indice: {search}")