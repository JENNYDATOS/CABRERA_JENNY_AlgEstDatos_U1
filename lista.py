
# lista.py
# Lista simplemente enlazada de clientes.
# Agregar, buscar, listar y eliminar: O(n).

class NodoCliente:
    def __init__(self, dni, nombre):
        self.dni = str(dni)
        self.nombre = str(nombre)
        self.siguiente = None


class ListaClientes:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None

    def agregar(self, dni, nombre=None):
        # Permite recibir un diccionario o DNI y nombre por separado.
        if isinstance(dni, dict) and nombre is None:
            cliente = dni
            dni = cliente.get("dni", "")
            nombre = cliente.get("nombre", "")

        dni = str(dni).strip()
        nombre = str(nombre or "").strip()

        if not dni or not nombre:
            raise ValueError("El DNI y el nombre son obligatorios.")

        if self.buscar_por_dni(dni) is not None:
            raise ValueError("Ya existe un cliente con ese DNI.")

        nuevo = NodoCliente(dni, nombre)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        self.tamano += 1
        return nuevo

    def buscar_por_dni(self, dni):
        dni = str(dni).strip()
        actual = self.cabeza

        while actual is not None:
            if actual.dni == dni:
                return actual
            actual = actual.siguiente

        return None

    def buscar_por_nombre(self, nombre):
        # Devuelve los clientes cuyo nombre contiene el texto buscado.
        termino = str(nombre).strip().casefold()
        encontrados = []

        if not termino:
            return encontrados

        actual = self.cabeza

        while actual is not None:
            if termino in actual.nombre.casefold():
                encontrados.append({
                    "dni": actual.dni,
                    "nombre": actual.nombre
                })

            actual = actual.siguiente

        return encontrados

    def mostrar_todos(self):
        clientes = []
        actual = self.cabeza

        while actual is not None:
            clientes.append({
                "dni": actual.dni,
                "nombre": actual.nombre
            })
            actual = actual.siguiente

        return clientes

    def listar(self):
        return self.mostrar_todos()

    def eliminar_por_dni(self, dni):
        dni = str(dni).strip()
        anterior = None
        actual = self.cabeza

        while actual is not None:
            if actual.dni == dni:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                self.tamano -= 1
                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def __len__(self):
        return self.tamano
