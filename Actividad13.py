print("¡Bienvenido al Gestor académico!")

estudiantes = {}

def agregar_estudiante():
    print("Agregar estudiante")
    idest = input("Ingresa el ID de estudiante: ")
    if idest in estudiantes:
        print("El ID ya está registrado")
        return
    nombre = input("Ingresa tu nombre completo: ")
    carrera = input("Ingresa tu carrera o programa académico: ")
    estudiantes[idest] = {"nombre": nombre, "carrera": carrera, "cursos": {}}
    print("¡Estudiante agregado correctamente!")

def agregar_curso():
    print("--Agregar curso con nota--")
    idest = input("Ingresa el ID de estudiante: ")
    if idest not in estudiantes:
        print("Estudiante no encontrado")
        return
    curso = input("Nombre del curso: ")
    nota = input("Nota final (0-100): ")
    try:
        nota = float(nota)
        if nota < 0 or nota > 100:
            print("¡Nota fuera del rango!")
            return
        estudiantes[idest]["cursos"][curso] = nota
        print("Curso y nota agregados correctamente")
    except:
        print("¡Nota inválida!")



