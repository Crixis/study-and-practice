"""
    diccionario
    un tipo de dato que almacena un conjunto de datos 
    en formato clave>valor.
    es parecido a un array
"""

persona={
    "nombre": "persona1",
    "apellido": "apellido1",
    "edad": "añosdelapersona1"
}
#persona= dict(nombre="persona1", apellido="apellido1", edad="añosdelapersona1")

print(persona)
print(type(persona))
print(persona["nombre"])

#lista con dicionarios

contactos=[
    {
        "nombre":"pedro",
        "edad":"18"
    },
    {
        "nombre":"lin",
        "edad":"19"
    }
]

print(contactos)
print(contactos[0]["edad"])

