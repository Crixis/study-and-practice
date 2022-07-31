import pandas as pd
from pandas.core.frame import DataFrame

def ventas(ruta_archivo:str, codigo:int)->dict:
    df= pd.read_csv(ruta_archivo, names=['id_cliente', 'nombre', 'codigo_producto', 'cantidad'])
    n=0
    cant=0
    while n<len(df['codigo_producto']):
        if codigo==df['codigo_producto'][n]:
            cant+=df['cantidad'][n]
        n+=1
    salida={
        codigo:cant
    }
    return salida
    

    

print(ventas("https://raw.githubusercontent.com/marinacharris/retos/main/Ventas.csv", 50016))