#Ejercicio #1
def goodgrades():
    i=1
    notas=0
    while i<=10:
        num=float(input(f"ingrese la nota #{i}: "))
        i+=1
        if num>=7:
           notas+=1
    print(f"hay {notas} estudiantes con nota 7 o superior")

#goodgrades()

#Ejercicio #2
def alturasProm():
    cant=int(input("ingrese la cantidad de personas a evaluar: "))
    i=1
    total=0
    while i<=cant:
        alt=int(input(f"ingrese la atura de la persona #{i}: "))
        total+=alt
        i+=1
    prom=total/cant
    print(f"el promedio de la altura de las personas es {prom}")
    
#alturasProm()

#Ejercicio #3
def sueldos():
    empleados=int(input("ingrese el numero de empleados: "))
    i=1
    sueldo1=0
    sueldo2=0
    gastoempresa=0
    while i<=empleados:
        sueldo=int(input(f"ingrese el sueldo del empleado #{i} :"))
        if sueldo<100 and sueldo>500:
            print("sueldo fuera de rango, ingrese un sueldo correcto")
            continue
        else:
            gastoempresa+=sueldo
            i+=1
            if sueldo>=100 and sueldo<=300:
                sueldo1+=1
            else:
                sueldo2+=1
    print(f"en la empresa hay {sueldo1} trabajadores que cobran entre $100 y $300 y {sueldo2} trabajadores que cobran mas de $300\n El total de gasto en sueldos es ${gastoempresa}")

#sueldos()

#Ejercicio #4
def impnum():
    termino=1
    num=0
    while termino<=25:
        num+=11
        termino+=1
        print(num)

#impnum()

#Ejercicio #5
def impnum8():
    num=8
    while num<=500:
        print(num)
        num+=8

#impnum8()

#Ejercicio #6
def doslist():
    lista1=[]
    lista2=[]
    total1=0
    total2=0
    num=1;num2=1
    while num<=2:
        lista1.append(int(input(f"valor #{num} ingrese un valor para la primer lista: ")))
        total1+=lista1[(num-1)]
        num+=1
    while num2<=2:
        lista2.append(int(input(f"valor #{num2} ingrese un valor para la segunda lista: ")))
        total2+=lista2[(num2-1)]
        num2+=1
    if total1>total2:
        print("lista 1 mayor")
    elif total1<total2:
        print("lista 2 mayor")
    else:
        print("listas iguales")

#doslist()    

#Ejercicio #7
def ej7():
    num=int(input("cuantos numeros desea ingresar: "))
    n=0
    par=0
    impar=0
    i=1
    while i<=num:
        n=int(input("ingrese un numero: "))
        if n%2==0:
            par+=1
        else:
            impar+=1
        i+=1
    print(f"hay {par} valores pares y {impar} impares")

#ej7()

#Ejercicio #8
