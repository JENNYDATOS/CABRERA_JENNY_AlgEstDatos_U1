
# pila.py
# Pila enlazada para guardar el historial de acciones.
# Principio LIFO: último en entrar, primero en salir.
# push y pop: O(1).

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
        nuevo = NodoPila(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamano += 1

    def pop(self):
        if self.esta_vacia():
            return None

        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamano -= 1
        return dato

    def peek(self):
        if self.esta_vacia():
            return None
        return self.tope.dato

    def __len__(self):
        return self.tamano
