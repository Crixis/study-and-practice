num1=int(input("ingrese un numero:"))
num2=int(input("ingrese otro numero:"))

if num1<num2:
    for cont in range(num1, (num2+1)):
        print(cont)
else:
    print("el primer numero tiene que ser menor que el segundo")