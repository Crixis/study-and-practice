try:
    accion=int(input("Elige una opcion: "))

    while accion!=1 or accion!=2:
        if accion==1:
            print("Bienvenido al registro de usuarios!!!!")
            nombre=input("Ingresa tu nombre: ")
            apellidos=input("ingresa tus apellidos: ")
            email=input("Ingresa tu email: ")
            contra=input("Ingresa tu contraseña: ")
            break
        elif accion==2:
            print("Bienvenido al sistema de login!!!!")
            email=input("Ingresa tu email: ")
            contra=input("Ingresa tu contraseña: ")
            break
        else:
            accion=int(input("lo que has introducido no concuerda con las opciones\nIntroduce una opcion valida: "))

except ValueError: print("!!!Error!!!! has ingresado caracteres")