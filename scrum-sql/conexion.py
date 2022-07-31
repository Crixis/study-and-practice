import mysql.connector


class datab():

    def __init__(self) -> None:
        try:
            self.cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="prueba_crud"
            )
        except:
            print("No se encontró conexion")

    def listarTabla(self):

        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        return resultados