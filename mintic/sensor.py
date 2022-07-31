def alarma(sen1: bool, sen2:bool, sen3:bool):
    if sen1 == True and sen2 == True and sen3 == True:
        alert = "tres sensores activos"
    elif sen1 == False and sen2 == False and sen3 == False:
        alert = "sensores inactivos"
    elif sen1 == True and sen2 == True:
        alert = "sensor 1 y 2 activos"
    elif sen2 == True and sen3 == True:
        alert = "sensor 2 y 3 activos"
    elif sen3 == True and sen1 == True:
        alert = "sensor 1 y 3 activos"
    elif sen1 == True or sen2 == True or sen3 == True:
        if sen1 == True:
            alert = "sensor 1 activo"
        elif sen2 == True:
            alert = "sensor 2 activo"
        elif sen3 == True:
            alert = "sensor 3 activo"
    return f"{alert}"
    
print(alarma(True, True, True))
print(alarma(False, True, False))