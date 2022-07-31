# autor: Cristian Camilo Vargas Mejia 
def calcularMtsTela(empresa: str, num_talla_S: int, num_talla_M: int, num_talla_L: int):
    canTela=0
    canTela+=(num_talla_L*3)
    canTela+=(num_talla_M*2.5)
    canTela+=(num_talla_S*2)

    resul=f"Para fabricar {num_talla_S} trajes talla S, {num_talla_M} trajes talla M, {num_talla_L} trajes talla L, para la empresa {empresa} se necesitan {canTela} metros de tela"

    return resul

    
print(calcularMtsTela("telasMario", 5, 8, 10))

