
# main.py
# Gestor de turnos del taller CarUPS.
# Integra una pila, una cola y una lista enlazada.

from pila import Pila
from cola import ColaTurnos
from lista import ListaClientes


def mostrar_cliente(cliente):
    print(
        f"DNI: {cliente['dni']} | "
        f"Nombre: {cliente['nombre']}"
    )


def solicitar_cliente():
    dni = input("DNI: ").strip()
    nombre = input("Nombre completo: ").strip()

    if not dni or not nombre:
        print("El DNI y el nombre son obligatorios.")
        return None

    return {"dni": dni, "nombre": nombre}


def ejecutar():
    historial = Pila()
    turnos = ColaTurnos()
    clientes = ListaClientes()

    while True:
        print("\n=== TALLER CARUPS: GESTOR DE TURNOS ===")
        print("1. Registrar cliente y turno")
        print("2. Atender siguiente turno")
        print("3. Mostrar turnos pendientes")
        print("4. Buscar cliente por nombre")
        print("5. Mostrar clientes registrados")
        print("6. Deshacer última acción")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        # OPCIÓN 1: registrar cliente y turno
        if opcion == "1":
            cliente = solicitar_cliente()

            if cliente is None:
                continue

            if clientes.buscar_por_dni(cliente["dni"]) is not None:
                print("Ya existe un cliente con ese DNI.")
                continue

            clientes.agregar(
                cliente["dni"],
                cliente["nombre"]
            )  # Agregar cliente: O(n)

            turnos.encolar(cliente)  # Encolar: O(1)

            historial.push(
                ("registrar", cliente)
            )  # Guardar acción: O(1)

            print("Cliente registrado y turno agregado correctamente.")

        # OPCIÓN 2: atender siguiente turno
        elif opcion == "2":
            cliente = turnos.desencolar()  # Desencolar: O(1)

            if cliente is None:
                print("No hay turnos pendientes.")
            else:
                historial.push(
                    ("atender", cliente)
                )  # Guardar acción: O(1)

                print("Turno atendido:")
                mostrar_cliente(cliente)

        # OPCIÓN 3: mostrar turnos pendientes
        elif opcion == "3":
            pendientes = turnos.obtener_turnos()  # O(n)

            if not pendientes:
                print("No hay turnos pendientes.")
            else:
                print("\n--- TURNOS PENDIENTES ---")
                for cliente in pendientes:
                    mostrar_cliente(cliente)

        # OPCIÓN 4: buscar cliente por nombre
        elif opcion == "4":
            nombre = input(
                "Ingrese el nombre o parte del nombre: "
            ).strip()

            encontrados = clientes.buscar_por_nombre(nombre)  # O(n)

            if encontrados:
                print("\n--- CLIENTES ENCONTRADOS ---")
                for cliente in encontrados:
                    mostrar_cliente(cliente)
            else:
                print("No se encontraron clientes.")

        # OPCIÓN 5: mostrar clientes registrados
        elif opcion == "5":
            registrados = clientes.mostrar_todos()  # O(n)

            if not registrados:
                print("No hay clientes registrados.")
            else:
                print("\n--- CLIENTES REGISTRADOS ---")
                for cliente in registrados:
                    mostrar_cliente(cliente)

        # OPCIÓN 6: deshacer la última acción
        elif opcion == "6":
            accion = historial.pop()  # Pop: O(1)

            if accion is None:
                print("No hay acciones para deshacer.")
                continue

            tipo, cliente = accion
            dni = cliente["dni"]

            if tipo == "registrar":
                # Eliminar el turno pendiente si todavía existe: O(n).
                turnos.eliminar_por_dni(dni)

                # Eliminar el cliente registrado: O(n).
                clientes.eliminar_por_dni(dni)

                print(
                    f"Se deshizo el registro de {cliente['nombre']}."
                )

            elif tipo == "atender":
                # Restaurar el turno al principio: O(1).
                turnos.encolar_frente(cliente)

                print(
                    f"Se deshizo la atención de {cliente['nombre']}; "
                    "el turno volvió al inicio de la cola."
                )

        # OPCIÓN 0: salir
        elif opcion == "0":
            print("Gracias por usar el gestor de turnos de CarUPS.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    try:
        ejecutar()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")
