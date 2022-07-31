from io import open
import shutil

#abrir archivo o crearlo
archivo = open("14-sistema-archivos/fichero_texto.txt", "a+")

#escribir
#archivo.write("************soy un texto****************\n")

#cerrar archivo
archivo.close()

#abrir archivo o crearlo
archivo_lectura = open("14-sistema-archivos/fichero_texto.txt", "r")

#leer contenido
#contenido=archivo_lectura.read()
#print(contenido)

#leer archivo y guardarlo en listas 
lista= archivo_lectura.readlines()
archivo_lectura.close()

print(lista)
for frase in lista:
    print("- "+frase)

#copiar
"""
archivo_original = str("14-sistema-archivos/fichero_texto.txt")
archivo_copiado = str("14-sistema-archivos/fichero_copiado.txt")
shutil.copyfile(archivo_original, archivo_copiado)
"""

#mover
#shutil.move(src, dst)

#eliminar
import os
#os.remove("14-sistema-archivos/fichero_copiado.txt")

#comprobar si existe
import os.path
if os.path.isfile("14-sistema-archivos/fichero_texto.txt"):
    print("el archivo existe")