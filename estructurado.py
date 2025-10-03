tasks = []

def agregar_tarea(desc):
    
    tasks.append(desc)
    print(f"Tarea agregada: {desc}")

def mostrar_tareas():

    # evalúa true si la lista está vacía e imprime que no existen tareas en la lista
    if not tasks:
        print("No hay tareas")
        return

    # enumerate(lista) entrega indice junto a su elemento y el ciclo for recorre cada tarea con su posición
    for i, t in enumerate(tasks):
        print(f"{i}: {t}")

def eliminar_tarea(indice):
   
    try:
        # .pop(i) elimina y muestra el elemento en la posición i que acaba de eliminarse
        eliminado = tasks.pop(indice)
        print(f"Tarea eliminada: {eliminado}")
    except IndexError:
        # marca error si el índice está fuera del rango
        print("Índice inválido. No se eliminó nada.")

def menu():
   
    while True:
        # muestra el menú
        print("\n Gestor de tareas ")
        print("1. Agregar  2. Mostrar  3. Eliminar  4. Salir")

        opt = input("Elige una opción: ").strip()

        if opt == '1':
            # pedimos la descripción de la nueva tarea y agregamos
            desc = input("Descripción de la tarea: ").strip()
            agregar_tarea(desc)

        elif opt == '2':
            # mostramos todas las tareas
            mostrar_tareas()

        elif opt == '3':
            # antes de eliminar, mostramos para que la persona vea los índices y esté seguro de cuál eliminar
            mostrar_tareas()
            try:
                # como input convierte los datos a string, int() lo convierte a entero para que pueda borrarse con el índice
                idx = int(input("Índice a eliminar: ").strip())
                eliminar_tarea(idx)
            except ValueError:
                # valida que la opción sea un int y no otro tipo de dato
                print("¡Por favor ingresa un número!")

        elif opt == '4':
            # mensaje de salida y se rompe el bucle del menú con 'break'
            print("Gracias por usar el gestor de tareas :)")
            break

        else:
            # si no fue alguna de las 4 opciones, avisamos que no es válido
            print("Opción inválida. Vuelve a intentarlo.")

if _name_ == "_main_":
    menu()