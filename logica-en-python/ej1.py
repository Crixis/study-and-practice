#define una funcion que me reciba un numero y me devuelva su tabla de multiplicar

def mul(num):
    for n in range(1,11):
        resultado=num*n
        print(f"{num} x {n} = {resultado}")

mul(5)