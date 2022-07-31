#Ejercicio 1
def es4():
    num=int(input("ingrese un numero entero: "))
    if (num%10) == 4 or num == 4:
        print(f"El numero {num} termina en 4")
    else:
        print(f"El numero {num} no termina en 4")

#es4()

#Ejercicio 2
def digi3():
    num=int(input("ingrese un numero entero: "))
    if num>99 and num<1000:
        print(f"el numero {num} tiene 3 digitos")
    else:
        print(f"el numero {num} no tiene 3 digitos")

#digi3()

#Ejercicio 3
def digPar():
    num=int(input("ingrese un numero de dos digitos: "))
    if num>9 and num<100:
        c=str(num)
        c1= int(c[0])
        c2= int(c[1])
        if c1%2 == 0:
            if c2%2 == 0:
                print("los dos digitos son pares")
            else:
                print("el segundo digito no es par")
        else:
            print("el primer digito no es par")
        
    else:
        print("el numero no tiene dos digitos")

#digPar()

#Ejercicio 4
def primo():
    num=int(input("ingrese un numero de dos digitos menor que 20: "))
    if num<20 and num>9:
        for n in range(2, num):
            if num%n==0:
                print(f"{num} no es primo")
                break
            else:
                print(f"{num} es primo")
                break
    else:
        print("el numero no está entre 9 y 20")

#primo()

#Ejercicio 5
def primNeg():
    num=int(input("Ingrese un numero: "))
    pri=False; neg=False
    if num<0:
        neg=True
    else:
        for n in range(2, num):
            if num%n == 0:
                pri=False
                break
            else:
                pri=True
                break

    if neg==True:
        print(f"el numero {num} es negativo")
    elif pri==True:
        print(f"el numero {num} es primo")
    else:
        print(f"el numero {num} no es primo ni negativo")

#primNeg()

#Ejercicio 6
def dig2():
    num=int(input("ingresa un numero de dos digitos: "))
    if num>=10 and num<=999:
        c=str(num)
        c1= int(c[0])
        c2= int(c[1])
        if c1 == c2:
            print("los dos digitos son iguales")
        else:
            print("los dos digitos son diferentes")
    else:
        print("no es un numero de dos cifras")

#dig2()

#Ejercicio 7
def mayorDe2():
    num1=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese otro numero: "))
    if num1>num2:
        print(f"{num1} es el mayor")
    else:
        print(f"{num2} es el mayor")

#mayorDe2()

#Ejercicio 8
def digSum():
    dosdig=False
    while dosdig == False:
        num1=int(input("Ingrese un numero: "))
        num2=int(input("Ingrese otro numero: "))
        if (num1>9 and num1<100)and(num2>9 and num2<100):
            dosdig==True
            break
        elif not(num1>9 and num1<100):
            print(f"{num1} no tiene dos digitos")
        elif not(num2>9 and num2<100):
            print(f"{num2} no tiene dos digitos")
    sn1=str(num1)
    sn2=str(num2)
    d1=int(sn1[0]); d2=int(sn1[1]); d3=int(sn2[0]); d4=int(sn2[1])
    resul=d1+d2+d3+d4
    print(f"la suma de todos los digitos de {num1} y {num2} es: {resul}")

#digSum()

#Ejercicio 9
def dig3():
    tresdig=False
    while tresdig == False:
        num1=int(input("Ingrese un numero: "))
        if (num1>99 and num1<1000):
            tresdig==True
            break
        elif not(num1>9 and num1<100):
            print(f"{num1} no tiene tres digitos")
    sn1=str(num1)
    d1=int(sn1[0]); d2=int(sn1[1]); d3=int(sn1[2])
    if d1>d2 and d1>d3:
        print(f"{d1} es el digito mayor")
    elif d2>d3:
        print(f"{d2} es el digito mayor")
    else:
        print(f"{d3} es el digito mayor")
    
#dig3()    

#Ejercicio 10
def dig3mult():
    tresdig=False
    while tresdig == False:
        num1=int(input("Ingrese un numero: "))
        if (num1>99 and num1<1000):
            tresdig==True
            break
        elif not(num1>9 and num1<100):
            print(f"{num1} no tiene tres digitos")
    sn1=str(num1)
    d1=int(sn1[0]); d2=int(sn1[1]); d3=int(sn1[2])
    if d1%d2==0 and d3%d2==0:
        print(f"{d2} es multiplo de {d1} y de {d3}")
    elif d2%d1==0 and d3%d1==0:
        print(f"{d1} es multiplo de {d2} y de {d3}")
    elif d1%d3==0 and d2%d3==0:
        print(f"{d3} es multiplo de {d1} y de {d2}")
    elif d2%d1==0:
        print(f"{d1} es multiplo de {d2}")
    elif d3%d1==0:
        print(f"{d1} es multiplo de {d3}")
    elif d1%d2==0:
        print(f"{d2} es multiplo de {d1}")
    elif d3%d2==0:
        print(f"{d2} es multiplo de {d3}")
    elif d1%d3==0:
        print(f"{d3} es multiplo de {d1}")
    elif d2%d3==0:
        print(f"{d3} es multiplo de {d2}")
    else:
        print("ninguno es multiplo")

#dig3mult()

#Ejercicio 11
numeroStr=[]
numeros=[]
def ingresalist():
    dosdig=False
    while dosdig==False:
        num=int(input("Ingrese un numero de dos digitos: "))
        if num>9 and num<100:
            numeroStr.append(str(num))
            break
        else:
            print(f"{num} no tiene dos cifras")

def strAnum():
    for n in range(0, len(numeroStr)):
        for i in range(0,2 ):
            numeros.append(int(numeroStr[n][i]))

def compara():
    mayor=0
    for n in range(0, len(numeros)):
            if mayor<numeros[n]:
                mayor=numeros[n]
    print(f"{mayor} es el numero mayor")

def digMay():
    for n in range(3):
        ingresalist()
    strAnum()
    compara()
    
#digMay()

#Ejercicio 12 no entendí

#Ejercicio 13
def prim():
    menor50=False
    while menor50==False:
        num=int(input("ingrese un numero del 1 al 50: "))
        if num>0 and num<=50:
            menor50=True
            break
    for n in range(2, num):
            if num%n==0:
                print(f"{num} no es primo, es divisible por {n}")
                break
            else:
                print(f"{num} es primo")
                break

prim()

#Ejercicio 14
