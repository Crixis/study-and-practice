Datos_empleado={
    "nombre":"juan",
    "apellido":"castro",
    "id":"12345678",
    "salario":"945000",
    "ventas":"2130000"
}
def pago_mensual(datos_empleado: dict)->dict:
    ven=int(datos_empleado["ventas"])
    if ven>0 and ven<1000000:
        comision=ven*0.03
        pagoTotal=(int(datos_empleado["salario"])+comision)
    elif ven>1000000 and ven<=3000000:
        comision=ven*0.05
        pagoTotal=(int(datos_empleado["salario"])+comision)
    elif ven>3000000 and ven<=5000000:
        comision=ven*0.08
        pagoTotal=(int(datos_empleado["salario"])+comision)
    elif ven>5000000:
        comision=ven*0.12
        pagoTotal=(int(datos_empleado["salario"])+comision)
    else:
        pagoTotal=int(datos_empleado["salario"])

    if ven>10000000:
        felicitacion="si"
    else:
        felicitacion="no"
        
    dicSalida={
        "nombreCompleto":datos_empleado["nombre"]+" "+datos_empleado["apellido"],
        "id":datos_empleado["id"],
        "pagoTotal":int(pagoTotal),
        "felicitacion":felicitacion
    }

    return f"El pago mensual de {dicSalida['nombreCompleto']} identificado con {dicSalida['id']} es: {dicSalida['pagoTotal']}. Felicitaciones por ventas: {dicSalida['felicitacion']}"

print(pago_mensual(Datos_empleado))



