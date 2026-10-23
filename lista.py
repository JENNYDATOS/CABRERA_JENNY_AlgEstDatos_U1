"""Lista simplemente enlazada de clientes registrados."""

class NodoCliente:
    def __init__(self, dni, nombre):
        self.dni = str(dni).strip()
        self.nombre = nombre.strip()
        self.siguiente = None


class ListaClientes:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def agregar(self, dni, nombre):
        """Agrega un cliente al final. Complejidad: O(n)."""
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

    def buscar_por_nombre(self, nombre):
        """Busca por nombre ignorando mayúsculas/minúsculas. Complejidad: O(n)."""
        objetivo = nombre.strip().casefold()
        actual = self.cabeza
        while actual is not None:
            if actual.nombre.casefold() == objetivo:
                return {"dni": actual.dni, "nombre": actual.nombre}
            actual = actual.siguiente
        return None

    def buscar_por_dni(self, dni):
        """Busca por DNI. Complejidad: O(n)."""
        objetivo = str(dni).strip()
        actual = self.cabeza
        while actual is not None:
            if actual.dni == objetivo:
                return {"dni": actual.dni, "nombre": actual.nombre}
            actual = actual.siguiente
        return None

    def obtener_todos(self):
        """Recorre la lista desde la cabeza. Complejidad: O(n)."""
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append({"dni": actual.dni, "nombre": actual.nombre})
            actual = actual.siguiente
        return resultado
