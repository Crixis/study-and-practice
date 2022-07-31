def listarProductos(productos):
    print("Productos: ")
    lis=1
    for pro in productos:
        print(f"{lis}. Id: {pro[0]}  | Producto: {pro[1]} | Precio: {pro[2]}")
        lis+=1

    print(" ")