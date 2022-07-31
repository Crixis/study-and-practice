#tkinter
#modulo para crear interfaces graficas de usuario

from tkinter import *

#crear ventana raiz
ventana=Tk()

#titulo de la ventana
ventana.title("interfaz grafica con python")

#icono de la ventana
#ventana.iconbitmap("ruta de la imagen")

#cambio en el tamaño de la ventana
ventana.geometry("750x450")

#bloquear el tamaño de la ventana
ventana.resizable(0, 0)

#arrancar y mostrar ventana hasta que se cierre
ventana.mainloop()