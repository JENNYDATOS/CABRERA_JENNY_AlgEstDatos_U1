"""Cola enlazada de turnos con referencias head y tail (FIFO)."""

class NodoCola:
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None


class Cola:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamano = 0

    def esta_vacia(self):
        return self.head is None

    def enqueue(self, cliente):
        """Inserta al final. Complejidad: O(1)."""
        nuevo = NodoCola(cliente)
        if self.esta_vacia():
            self.head = self.tail = nuevo
        else:
            self.tail.siguiente = nuevo
            self.tail = nuevo
        self.tamano += 1

    def dequeue(self):
        """Retira el primero. Complejidad: O(1)."""
        if self.esta_vacia():
            return None
        cliente = self.head.cliente
        self.head = self.head.siguiente
        if self.head is None:
            self.tail = None
        self.tamano -= 1
        return cliente

    def enqueue_front(self, cliente):
        """Restaura al frente al deshacer una atención. Complejidad: O(1)."""
        nuevo = NodoCola(cliente)
        if self.esta_vacia():
            self.head = self.tail = nuevo
        else:
            nuevo.siguiente = self.head
            self.head = nuevo
        self.tamano += 1

    def remove_by_dni(self, dni):
        """Elimina un cliente pendiente por DNI. Complejidad: O(n)."""
        anterior = None
        actual = self.head
        while actual is not None:
            if actual.cliente["dni"] == dni:
                if anterior is None:
                    self.head = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                if actual is self.tail:
                    self.tail = anterior
                self.tamano -= 1
                if self.head is None:
                    self.tail = None
                return actual.cliente
            anterior, actual = actual, actual.siguiente
        return None

    def listar(self):
        """Devuelve los clientes pendientes en orden FIFO. Complejidad: O(n)."""
        clientes = []
        actual = self.head
        while actual is not None:
            clientes.append(actual.cliente)
            actual = actual.siguiente
        return clientes

    def __len__(self):
        return self.tamano
