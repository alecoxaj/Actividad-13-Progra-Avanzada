print("¡Bienvenido al Gestor académico!")

estudiantes = {}

def agregar_estudiante():
    print("Agregar estudiante")
    IDest = input("Ingresa el ID de estudiante: ")
    if IDest in estudiantes:
        print("El ID ya está registrado")
        return
    nombre = input("Ingresa tu nombre completo: ")
    carrera = input("Ingresa tu carrera o programa académico: ")
    estudiantes[IDest] = {"nombre": nombre, "carrera": carrera, "cursos": {}}
    print("¡Estudiante agregado correctamente!")

