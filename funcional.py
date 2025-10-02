# funcional.py

# la lista de tareas será una variable que se pasa como argumento y se devuelve modificada cuando sea necesario


def agregar_tarea(tasks, desc):
    # se crea una lista nueva en lugar de modificar la existente.
    return tasks + [desc]


def mostrar_tareas(tasks):
    if not tasks:
        print("No hay tareas.")
        return
    for i, t in enumerate(tasks):
        print(f"{i}: {t}")


def eliminar_tarea(tasks, indice):
    if indice < 0 or indice >= len(tasks):
        print("Índice inválido.")
        return tasks
    # se usa slicing para generar una nueva lista sin ese índice, o sea si ("A", "B", "C") y quiero eliminar el índice 1,
    # tasks[:1] entrega ("A",) y tasks[2:] entrega ("C",), y al concatenarlas queda ("A", "C")
    return tasks[:indice] + tasks[indice+1:]


def menu_funcional():
    tasks = []
    while True:
        print("\n Gestor (Funcional) ")
        print("1. Agregar  2. Mostrar  3. Eliminar  4. Salir")
        opt = input("Elige una opción: ").strip()

        if opt == '1':
            desc = input("Descripción de la tarea: ").strip()
            tasks = agregar_tarea(tasks, desc)

        elif opt == '2':
            mostrar_tareas(tasks)

        elif opt == '3':
            mostrar_tareas(tasks)
            try:
                idx = int(input("Índice a eliminar: ").strip())
                tasks = eliminar_tarea(tasks, idx)
            except ValueError:
                print("Por favor ingresa un número.")

        elif opt == '4':
            print("Gracias por utilizar el gestor de tareas :)")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if _name_ == "_main_":
    menu_funcional()