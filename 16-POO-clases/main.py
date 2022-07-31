#programacion orientada a objetos
#definir una clase
class coche:

    #atributos
    color="rojo"
    marca="ferrari"
    velocidad=300

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

#instanciar un objeto
coche1=coche()

coche1.setcolor("azul")
print(coche1.getmarca())
print(coche1.getcolor())
print(coche1.getvelocidad())

coche2=coche()