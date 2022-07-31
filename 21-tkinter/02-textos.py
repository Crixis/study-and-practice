from cProfile import label
from tkinter import *

ventana=Tk()
ventana.geometry("500x500")

texto=Label(ventana, text="bienvenido a mi programa")
#texto.config()    para modificar la apariencia dentro de la interfaz
texto.pack()

ventana.mainloop()