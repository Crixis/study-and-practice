apro=0
repro=0

for x in range(1, 16):
    notas=float(input(f"ingrese la nora del alumno {x}: "))
    if notas<=3.0:
        repro+=1
    else:
        apro+=1
print(f"Alumnos aprovados: {apro}\nAlumnos reprovados: {repro}")