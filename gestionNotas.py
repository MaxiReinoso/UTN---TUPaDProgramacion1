#Validacion de notas
def validarNota():
    while True:
        try:
            nota = float(input("Ingrese la nota (0-10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("La nota debe ser entre 0 y 10")
        except ValueError:
            print("Error: Ingrese un numero valido")

#Calculo y guardo promedio de alumno
def guardarPromedio(alumno):
    if materias[3]:
        promedio_final = sum(materias[3]) / len(materias[3])
        promedioAlumno[alumno] = round(promedio_final, 2)
        print(f"El promedio final de {alumno} es: {promedioAlumno[alumno]}")
    else:
        print("No hay promedios para calcular")
#Materia con nota mas alta
def mejorMateria(alumno):
    if materia[3]:
        notaMayor = max(materias[3])
        print(f"La materia con mejor promedio es: {notaMayor}")
    else:
        print("No hay notas para analizar")

#creo diccionario
diccionario = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"    
}
#lista de materia y notas
materias = [
    ["Ciencias", "Historia", "Geografia", "Matematicas", "Fisica"],
    [],
    [],
    []
]
#lista de alumnos con notas finales
notasFinales = [
    ["Rodolfo Fernandez", "Luis Gomez", "Andrea Pereira", "Juan Cruz Gonzales"],
    []
]
#iteracion
for clave, nombre in diccionario.items():
    print(clave, nombre)

#eleccion de alumno
alumno_Elegido = None
while True:
    try:
        legajo = int(input("Ingrese el legajo de un alumno para ingresar sus notas: "))
        if legajo in diccionario:
            alumno_Elegido = diccionario[legajo]
            print(f"Ingrese la notas de {alumno_Elegido}")
            break
        else:
            print("Legajo no valido")
    except ValueError:
            print("Error: Ingrese un numero valido ")

#ingreso de notas
for materia in materias[0]:
    print(f"-- {materia} --")
    nota1 = validarNota()
    nota2 = validarNota()

    promedio = (nota1 + nota2) / 2
    print(promedio)

    materias[1].append(nota1)
    materias[2].append(nota2)
    materias[3].append(promedio)
    
#mostrar lista con las notas
for i, fila in enumerate(materias):
    if i == 0:
        print(f"Materias:  {fila}")
    elif i == 1:
        print(f"Nota 1:    {fila}")
    elif i == 2:
        print(f"Nota 2:    {fila}")
    elif i == 3:
        print(f"Promedios: {fila}")

promedioAlumno = {
    "Rodolfo Fernandez": None,
    "Luis Gomez": None,
    "Andrea Pereira": None,
    "Juan Cruz Gonzales":None 
}

#Guardo el promedio final en el diccionario
guardarPromedio(alumno_Elegido)


