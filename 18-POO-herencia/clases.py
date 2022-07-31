# Herencia: posibilidad de compartir metodos y atributos entre clases
# y que diferentes clases hereden de otras
class persona:
    """
    nombre
    apellidos
    altura
    edad
    """
#como heredar
#nota: el constructor no se ejecuta en las clases hijas, 
# para ejecutar el constructor de la clase padre en la clase hija se debe hacer super().__init__()
#class hija(padre):