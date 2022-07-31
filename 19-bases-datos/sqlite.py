#importar modulo
import sqlite3

#conexion
conexion=sqlite3.connect('./19-bases-datos/pruebas.db')

#crear cursor
cursor=conexion.cursor()

#crear tabla
cursor.execute("create table if not exists productos("+
"id integer primary key autoincrement, "+
"titulo VARCHAR(255), "+
"descripcion text, " +
"precio int(255)"+
")")

#guardar cambios
conexion.commit()

#cerrar conxion
conexion.close()