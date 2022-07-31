import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("Bienvenido al registro de usuarios!!!!")
        nombre=input("Ingresa tu nombre: ")
        apellidos=input("ingresa tus apellidos: ")
        email=input("Ingresa tu email: ")
        contra=input("Ingresa tu contraseña: ")

        usuario=modelo.Usuario(nombre, apellidos, email, contra)
        registro=usuario.registrar()

        if registro[0]>=1:
            print(f"perfecto{registro[1].nombre} te has registrado con el email{registro[1].email}")
        else:
            print("no te has registrado correctamente")
    
    def login(self):
        print("Bienvenido al sistema de login!!!!")
        email=input("Ingresa tu email: ")
        contra=input("Ingresa tu contraseña: ")