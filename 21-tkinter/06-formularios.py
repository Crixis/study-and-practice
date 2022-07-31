from cProfile import label
from locale import normalize
from tkinter import *
from turtle import left, right
from types import ClassMethodDescriptorType

ventana=Tk()
ventana.geometry("700x400")
ventana.title("formularios en Tkinter")

#texto encabezado
encabezado=Label(ventana, text="Formularios con Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("arial", 18),
    padx=10,
    pady=10
    )
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

#label para el campo(nombre)
label=Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

# CAMPO DE TEXTO(nombre)
campo_texto=Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#label para el campo(apellidos)
label=Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5)

# CAMPO DE TEXTO(apellidos)
campo_texto=Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#label para el campo(descripcion)
label=Label(ventana, text="Descripcion")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

#campo de texto grande(descripcion)
campo_grande=Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(height=5, width=30, padx=10, pady=10, font=("arial",12))

#boton
Label(ventana).grid(row=4, column=1)
boton=Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=15, pady=10, bg="blue", fg="white")

ventana.mainloop()