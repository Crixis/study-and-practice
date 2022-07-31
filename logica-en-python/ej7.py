#recibir dos numero y la salida es la cantidad de numero impares que hay entre ellos

def cantImpares(num1, num2):
    contador=0
    for i in range(num1, num2):
        if i%2 !=0:
            contador+=1
    print(f"la cantidad de impares entre {num1} y {num2} son: {contador}")


cantImpares(1, 100)