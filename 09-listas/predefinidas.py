numeros=[5, 8, 4, 2, 7, 9, 6]
perros=["perro1", "perro2", "perro3", "perro4", "perro5"]

#ordenar
numeros.sort()
print(numeros)

#añadir elementos
perros.append("perro6")
perros.insert(3,"perro8")
print(perros)

#eliminar elementos
perros.pop(3)
perros.remove("perro6")
print(perros)

# dar la vuelta a una lista
numeros.reverse()
print(numeros)

#buscar dentro de una lista 
print("perro3" in perros)

#contar elementos
print(len(numeros))

#cuantas veces aparece un elemento
print(numeros.count(7))

#conseguir indice
print(perros.index("perro4"))

#unir listas
perros.extend(numeros)
print(perros)