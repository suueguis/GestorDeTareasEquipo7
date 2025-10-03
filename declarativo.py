# declarativo.py

def mostrar_tareas(tasks):
    # si hay tareas cada una la imprime con su índice, sino imprime que no hay tareas
    print("\n".join(f"{i}: {t}" for i, t in enumerate(tasks)) or "No hay tareas.") 


def agregar_tarea(tasks, desc):
    return [*tasks, desc] # crea una nueva lista con las tareas existentes y la nueva al final


def eliminar_tarea(tasks, indice):
    # usa list comprehension para crear una nueva lista sin el índice dado
    if 0 <= indice < len(tasks):
        return [t for i, t in enumerate(tasks) if i != indice] # sin pop()
    print("Índice inválido.")
    return tasks


def menu_declarativo():
    tasks = [] # lista inicial vacía
    while True:
        opcion = (
            input("\n Gestor (Declarativo) \n"
                  "1. Agregar  2. Mostrar  3. Eliminar  4. Salir\n"
                  "Elige: ").strip()
        )

        tasks = ( # muestra la lista nueva si se agrega o la misma si no
            agregar_tarea(tasks, input("Descripción: ").strip())
            if opcion == '1' else
            tasks
        )

        mostrar_tareas(tasks) if opcion == '2' else None
        # if porque hay interacción del usuario y es necesario validación
        if opcion == '3':
            mostrar_tareas(tasks)
            try:
                idx = int(input("Índice a eliminar: ").strip())
                tasks = eliminar_tarea(tasks, idx)
            except ValueError:
                print("Debes ingresar un número.")

        if opcion == '4':
            print("Chao :)")
            break


if __name__ == "__main__":
    menu_declarativo()