class coche:

    #atributos inicializar
    def __init__(self, color, marca, velocidad):
        self.color=color
        self.marca=marca
        self.velocidad=velocidad

    #metodos
    def setcolor(self, color):
        self.color=color
    
    def getcolor(self):
        return self.color

    def setmarca(self, marca):
        self.marca=marca
    
    def getmarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad +=1

    def frenar(self):
        self.velocidad -=1
    
    def getvelocidad(self):
        return self.velocidad