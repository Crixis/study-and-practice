# recibir dos arrays y devolver un array de los elementos comunes entre ambos

def comunElemento(array1, array2):
    arraycompuesto=list()
    for n in range(len(array1)):
        for m in range(len(array2)):
            if array1[n]==array2[m]:
                arraycompuesto.append(array1[n])
    return arraycompuesto, type(array2)

print(comunElemento([2,3,5,7], [9,7,3,1,5]))



