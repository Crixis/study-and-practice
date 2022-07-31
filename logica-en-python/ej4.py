#dada una string invertir el orden de sus caracteres sin usar metodos del lenguaje

def invertir(palabra):
    palabra=palabra.replace(" ", "")
    palabrainv=""
    for n in range(len(palabra)-1, -1, -1):
        palabrainv+=palabra[n]
    print(palabrainv)

invertir("laura")