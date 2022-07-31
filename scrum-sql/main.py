
from conexion import datab
import funciones


def menuPrincipal():
    continuar = True
    while continuar:
        validar = False
        while not validar:
            print("########## MENU PRINCIPAL ###############")
            print("     1- MOSTRAR PRODUCTOS")
            print("     2- REGISTRAR PRODUCTO")
            print("     3- ACTUALIZAR PRODUCTO")
            print("     4- ELIMINAR PRODUCTO")
            print("     5- SALIR")
            print("##########################################")
            opcion = int(input("SELECCIONE UNA OPCION: "))

            if opcion < 1 or opcion > 5:
                print("SELECCIONE UNA OPCION VALIDA...")
            elif opcion == 5:
                continuar = False
                print("HASTA PRONTO")
                break
            else:
                validar = True
                opcionar(opcion)


def opcionar(opcion):

    if opcion == 1:

        productos = datab.listarTabla()
        if len(productos) > 0:
            funciones.listarProductos(productos)
        else:
            print("NO SE ENCUENTRAN PRODUCTOS")
    elif opcion == 2:
        print("registar")
    elif opcion == 3:
        print("actualizar")
    elif opcion == 4:
        print("eliminar")


menuPrincipal()
