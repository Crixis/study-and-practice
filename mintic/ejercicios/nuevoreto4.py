from functools import reduce

def informe(examenes_medicos:list)->list:
    total=list(map(lambda x: [x[0]]+[reduce(lambda a,b: a + b, x[1:])],list(map(lambda x: [x[0]]+list(map(lambda y:y[1], x[1:])), examenes_medicos))))
    cont = []
    cont.append(["EL_PCOVID" in z for y in examenes_medicos for z in y[1:len(y)]].count(True))
    lista_salida = total + cont
    return lista_salida

