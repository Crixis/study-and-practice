import mysql.connector

#conexion a la base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

#asegurarme que la conexion ha sido correcta
#print(database)

#cursor lo que permite generar las consultas
cursor=database.cursor(buffered=True)
"""
#crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
#mostrar bases de datos en consola
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
#crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) AUTO_INCREMENT NOT NULL,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    constraint pk_vehiculo primary key(id)
)
""")

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'opel', 'astra', 18500)")
database.commit()
#consultar por consola
"""
cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()

for coche in result:
    print(coche)
"""
#para borrar se utiliza     DELETE FROM vehiculos WHERE condicion
#database.commit()
#print(cursor.rowcount)     para llevar el registro de borrados (opcional)

#actualizar
#cursor.execute("UPDATE vehiculos SET modelo='leon' WHERE marca='seat'")
#database.commit()