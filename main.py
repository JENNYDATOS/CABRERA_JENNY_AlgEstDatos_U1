"""Aplicación de consola: gestor de turnos del taller CarUPS."""

from pila import Pila
from cola import Cola
from lista import ListaClientes


def mostrar_cliente(cliente):
    print(f"DNI: {cliente['dni']} | Nombre: {cliente['nombre']}")


def solicitar_cliente():
    dni = input("DNI: ").strip()
    nombre = input("Nombre completo: ").strip()
    if not dni or not nombre:
        print("El DNI y el nombre son obligatorios.")
        return None
    return {"dni": dni, "nombre": nombre}


def ejecutar():
    historial = Pila()
    turnos = Cola()
    clientes = ListaClientes()

    while True:
        print("\\n=== TALLER CARUPS: GESTOR DE TURNOS ===")
        print("1. Registrar cliente y turno")
        print("2. Atender siguiente turno")
        print("3. Mostrar turnos pendientes")
        print("4. Buscar cliente por nombre")
        print("5. Mostrar clientes registrados")
        print("6. Deshacer última acción")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cliente = solicitar_cliente()
            if cliente is None:
                continue
            if any(c["dni"] == cliente["dni"] for c in clientes.listar()):
                print("Ya existe un cliente registrado con ese DNI.")
                continue
            clientes.agregar(cliente)             # agregar cliente: O(n)
            turnos.enqueue(cliente)                # enqueue: O(1)
            historial.push(("registrar", cliente)) # push: O(1)
            print("Cliente registrado y turno agregado correctamente.")

        elif opcion == "2":
            cliente = turnos.dequeue()             # dequeue: O(1)
            if cliente is None:
                print("No hay turnos pendientes.")
            else:
                historial.push(("atender", cliente)) # push: O(1)
                print("Turno atendido:")
                mostrar_cliente(cliente)

        elif opcion == "3":
            pendientes = turnos.listar()            # listar cola: O(n)
            if not pendientes:
                print("No hay turnos pendientes.")
            else:
                print("\\nTurnos pendientes (orden de llegada):")
                for cliente in pendientes:
                    mostrar_cliente(cliente)

        elif opcion == "4":
            nombre = input("Nombre o parte del nombre a buscar: ").strip()
            if not nombre:
                print("Escriba un nombre para buscar.")
                continue
            encontrados = clientes.buscar_por_nombre(nombre) # buscar: O(n)
            if encontrados:
                for cliente in encontrados:
                    mostrar_cliente(cliente)
            else:
                print("No se encontraron clientes.")

        elif opcion == "5":
            registrados = clientes.listar()         # recorrer lista: O(n)
            if not registrados:
                print("No hay clientes registrados.")
            else:
                print("\\nClientes registrados:")
                for cliente in registrados:
                    mostrar_cliente(cliente)

        elif opcion == "6":
            accion = historial.pop()                # pop: O(1)
            if accion is None:
                print("No hay acciones para deshacer.")
            else:
                tipo, cliente = accion
                if tipo == "registrar":
                    turnos.remove_by_dni(cliente["dni"]) # eliminar pendiente: O(n)
                    clientes.eliminar_por_dni(cliente["dni"]) # eliminar registro: O(n)
                    print(f"Se deshizo el registro de {cliente['nombre']}.")
                elif tipo == "atender":
                    turnos.enqueue_front(cliente)   # restaurar turno al frente: O(1)
                    print(f"Se deshizo la atención de {cliente['nombre']}; volvió al inicio de la cola.")

        elif opcion == "0":
            print("Gracias por usar el gestor de turnos de CarUPS.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    try:
        ejecutar()
    except (KeyboardInterrupt, EOFError):
        print("\\nPrograma finalizado.")
