
# cola.py
# Cola enlazada de turnos: FIFO.
# Encolar y desencolar: O(1).

class NodoCola:
    def __init__(self, turno):
        self.turno = turno
        self.siguiente = None


class ColaTurnos:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None

    def encolar(self, turno):
        nuevo = NodoCola(turno)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

        self.tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            return None

        turno = self.cabeza.turno
        self.cabeza = self.cabeza.siguiente

        if self.cabeza is None:
            self.cola = None

        self.tamano -= 1
        return turno

    def encolar_frente(self, turno):
        nuevo = NodoCola(turno)

        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

        self.tamano += 1

    def obtener_turnos(self):
        turnos = []
        actual = self.cabeza

        while actual is not None:
            turnos.append(actual.turno)
            actual = actual.siguiente

        return turnos

    def eliminar_por_dni(self, dni):
        anterior = None
        actual = self.cabeza

        while actual is not None:
            if str(actual.turno["dni"]) == str(dni):
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                if actual is self.cola:
                    self.cola = anterior

                self.tamano -= 1

                if self.cabeza is None:
                    self.cola = None

                return actual.turno

            anterior = actual
            actual = actual.siguiente

        return None

    # Alias para compatibilidad con el código anterior.
    def enqueue(self, turno):
        self.encolar(turno)

    def dequeue(self):
        return self.desencolar()

    def enqueue_front(self, turno):
        self.encolar_frente(turno)

    def remove_by_dni(self, dni):
        return self.eliminar_por_dni(dni)

    def listar(self):
        return self.obtener_turnos()

    def __len__(self):
        return self.tamano
