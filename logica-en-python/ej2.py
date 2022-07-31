#dada una cadena de texto, comprobar si es palindromo o no

from numpy import sort


def palin(texto):
    texto=texto.replace(" ", "")
    texto2=""
    for n in range(len(texto)-1, -1,-1):
        texto2+=texto[n]
    if texto==texto2:
        print("el texto es un palindromo")
        print(texto)
    else:
        print("el texto no es un palindromo")
        print(f"1. {texto}")
        print(f"2. {texto2}")


palin("anas")
