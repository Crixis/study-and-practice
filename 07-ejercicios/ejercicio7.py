num1= int(input("ingrese el primer valor de un rango: "))
num2= int(input("ingrese el segundo valor de un rango: "))

if num1<num2:
    for cont in range(num1, num2+1):
        if cont%2 != 0:
            print(cont)
else:
    print("el primer numero debe ser menor que el segundo")