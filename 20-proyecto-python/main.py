"""
Proyecto python y Mysql:
-Abrir asistente
-si elegimos registro creara un usuario en la bbdd
-si elegimos login, identifica al usuario y nos preguntará
-crear nota, mostrar nota, borrar nota, modificar nota.

"""
from usuarios import acciones

hacer=acciones.Acciones()

print("""
    Acciones Disponibles:
    (1) registro
    (2) login
""")

try:
    accion=int(input("Elige una opcion: "))

    while accion!=1 or accion!=2:
        if accion==1:
            hacer.registro()
            break
        elif accion==2:
            hacer.login()
        else:
            accion=int(input("lo que has introducido no concuerda con las opciones\nIntroduce una opcion valida: "))

except ValueError: print("!!!Error!!!! has ingresado caracteres")




