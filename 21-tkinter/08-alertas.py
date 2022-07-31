from tkinter import *
from tkinter import messagebox

ventana= Tk()
ventana.config(bd=70)

def sacarAlerta():
    messagebox.showinfo("Alerta", "voy a ser el mejor")

def salir():
    resultado = messagebox.askquestion("Salir", "Desea salir de la aplicacion?")
    if resultado=="yes":
        ventana.destroy()




Button(ventana, text="Mostrar alerta!!!!", command=sacarAlerta).pack()

Button(ventana, text="Salir", command=salir).pack()

ventana.mainloop()