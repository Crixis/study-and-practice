#dado un numnero mostrar una escalera con escalones de "[-]"
#usando el numero para los nieveles de la escalera

def escalera(cantidad):
    escalon="[-]"
    for n in range(1, cantidad+1):
        print(escalon*n)
        
    """
    n=1
    while n<=cantidad:
        print(escalon*n)
        n+=1
    """



escalera(8)