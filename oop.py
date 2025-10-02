# oop.py

# clase que representa una tarea
class Tarea:
    # constructor, self indica la instancia y descripción es el parámetro que se recibe cuando se crea el objeto 
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self): # __str__ es el tipo de dato que retorna
        return self.descripcion


# clase que gestiona las tareas
class GestorTareas:
    def __init__(self): # constructor, self únicamente para indicar la instancia y no tiene parámetros adicionales
        self.tasks = []

    def agregar_tarea(self, desc):
        nueva = Tarea(desc)
        self.tasks.append(nueva)
        print(f"Tarea agregada: {nueva}")

    def mostrar_tareas(self):
        if not self.tasks:
            print("No hay tareas.")
            return
        for i, t in enumerate(self.tasks):
            print(f"{i}: {t}")

    def eliminar_tarea(self, indice):
        try:
            eliminado = self.tasks.pop(indice)
            print(f"Tarea eliminada: {eliminado}")
        except IndexError:
            print("Índice inválido.")


def menu(): # mismo menú que en estructurado.py pero usando la clases definidas arriba
    gestor = GestorTareas() # instancia de la clase GestorTareas para usar sus métodos
    while True:
        print("\n Gestor de tareas (OOP) ")
        print("1. Agregar  2. Mostrar  3. Eliminar  4. Salir")
        opt = input("Elige una opción: ").strip()

        if opt == '1':
            desc = input("Descripción de la tarea: ").strip()
            gestor.agregar_tarea(desc)

        elif opt == '2':
            gestor.mostrar_tareas()

        elif opt == '3':
            gestor.mostrar_tareas()
            try:
                idx = int(input("Índice a eliminar: ").strip())
                gestor.eliminar_tarea(idx)
            except ValueError:
                print("¡Por favor ingresa un número!")

        elif opt == '4':
            print("Gracias por utilizar el gestor de tareas :)")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
