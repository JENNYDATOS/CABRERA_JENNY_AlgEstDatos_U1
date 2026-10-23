"""Pila enlazada para el historial de acciones (LIFO)."""

class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.tope = None
        self.tamano = 0

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):
        """Agrega una acción al tope. Complejidad: O(1)."""
        nuevo = NodoPila(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamano += 1

    def pop(self):
        """Retira y devuelve la última acción. Complejidad: O(1)."""
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamano -= 1
        return dato

    def peek(self):
        """Consulta la acción más reciente. Complejidad: O(1)."""
        return None if self.esta_vacia() else self.tope.dato

    def __len__(self):
        return self.tamano
