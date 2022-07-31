#dibujar un cuadrado hueco con asteriscos

def cuadrado():
    figura="*"
    cuadrado=""
    for i in range(4):
        cuadrado+=figura
    print(cuadrado)
    for i in range(2):
        print(figura,"",figura)
    print(cuadrado)

cuadrado()