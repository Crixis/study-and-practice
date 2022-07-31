"""
    LISTAS (arrays)
variable que puede contener un conjunto de datos, no necesariamente tienen que ser del mismo tipo

"""

#definir lista
letras= ["a","b","c","d"]
numeros= list(("1","2","3","4")) #se tiene que hacer una tupla
years= list(range(2020, 2050))

"""
print(letras)
print(numeros)
print(years)
"""
#indices
print(letras[2])
print(letras[0:3])

#modificar una posicion del array
letras[2]="z"
print(letras)

#añadir elementos a un array
letras.append("e")
print(letras)

#recorrer un array
print("***********LISTADO LETRAS**************")

for x in letras:
    print(x)

print("***********LISTADO letras**************")
for x in letras:
    print(f"{letras.index(x)}. {x}")

#matrices
contactos=[["nombre1", "correo1"],["nombre2", "correo2"],["nombre3", "correo3"]]

print(contactos)
print(contactos[1][1])

#recorrer la matriz
print("------------------------------------------------")
for x in contactos:
    for y in x:
        print(y)