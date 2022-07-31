#dada una palabra buscarla en una frase y devolver la cantidad de veces que aparece
#la palabra y la frase deben ser parametros de una funcion

def buscaplbr(frase, palabra):
    palabra=palabra.lower()
    frase=frase.lower()
    chars=".,-#"

    for char in chars:
        frase=frase.replace(char, "")
        
    frase=frase.split()
    contador=0

    for n in range(len(frase)):
        if palabra==frase[n]:
            contador+=1
    print(f"la cantidad de veces que aparece la palabra '{palabra}' \n cantidad:{contador}")


buscaplbr("Una- #paloma#, una- liebre, una- gata.", "UNA")
