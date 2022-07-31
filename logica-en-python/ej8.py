#recibir un numero entero, invertirlo y devolverlo

def invertirNumero(num):
    numstr=str(num)
    invertido=""
    for i in range(len(numstr)-1, -1, -1):
        invertido+=numstr[i]
    invertido=int(invertido)
    print(invertido)

invertirNumero(1469)