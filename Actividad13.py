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

def consultar_estudiante():
    print("--Consulta de estudiantes--")
    idest = input("Ingresa el ID del estudiante: ")
    if idest in estudiantes:
        est = estudiantes[idest]
        print("Nombre:", est["nombre"])
        print("Carrera:", est["carrera"])
        print("Cursos y notas de", est["nombre"])
        for curso in est["cursos"]:
            print("-", curso, ":", est["cursos"][curso])
    else:
        print("Estudiante no encontrado")

def calcular_promedio():
    print("--Calcular promedio--")
    for idest in estudiantes:
        est = estudiantes[idest]
        cursos = est["cursos"]
        total = 0
        suma = 0
        for c in cursos:
            suma += cursos[c]
            total += 1
        if total > 0:
            promedio = suma / total
            print(f"{est['nombre']} (ID {idest}) - Promedio: {promedio}")
        else:
            print(f"{est['nombre']} (ID {idest}) - No tiene cursos registrados.")


def verificar_aprobacion():
    print("--Verificar si aprueba--")
    for idest in estudiantes:
        est = estudiantes[idest]
        cursos = est["cursos"]
        if len(cursos) == 0:
            print(f"{est['nombre']} (ID {idest}) - No tiene cursos registrados.")
        else:
            todos_aprobados = True
            for curso in cursos:
                if cursos[curso] < 61:
                    todos_aprobados = False
            if todos_aprobados:
                print(f"{est['nombre']} (ID {idest}) - Aprueba todos los cursos.")
            else:
                print(f"{est['nombre']} (ID {idest}) - NO aprueba todos los cursos.")

def mostrar_todos():
    print("--Mostrar todos los estudiantes-- ")
    for id_est in estudiantes:
        est = estudiantes[id_est]
        print(f"ID: {id_est} - {est['nombre']} - {est['carrera']}")
        for curso in est["cursos"]:
            print(f"   {curso}: {est['cursos'][curso]}")

def guardado():
    print("\n--Guardado--")
    for idest in estudiantes:
        est = estudiantes[idest]
        print(f"{idest}|{est['nombre']}|{est['carrera']}")
        for curso in est["cursos"]:
            print(f"{idest};{curso};{est['cursos'][curso]}")
    print("Datos Guardados y saliendo...")
while True:
    print("MENÚ")
    print("1. Agregar estudiante")
    print("2. Agregar curso con nota")
    print("3. Consultar estudiante")
    print("4. Calcular promedio")
    print("5. Verificar aprobación")
    print("6. Mostrar todos los estudiantes")
    print("7. Salir")

    option = input("Selecciona una opción (1-7): ")

    match option:
        case "1":
            agregar_estudiante()
        case "2":
            agregar_curso()
        case "3":
            consultar_estudiante()
        case "4":
            calcular_promedio()
        case "5":
            verificar_aprobacion()
        case "6":
            mostrar_todos()
        case "7":
            guardado()
            break
        case _:
            print("¡Opción inválida! Inténtalo nuevamente.")
