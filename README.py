# Gestor de turnos CarUPS — Unidad 1

Programa de consola en Python que administra clientes y turnos utilizando tres estructuras lineales implementadas mediante nodos.

## Requisitos
- Python 3.10 o superior (no requiere instalar paquetes externos).
- Archivos `main.py`, `pila.py`, `cola.py` y `lista.py` en la misma carpeta.

## Como ejecutar
En una terminal, dentro de la carpeta del proyecto:

```bash
python main.py
```

En algunos equipos Windows también puede usarse:

```bash
py main.py
```

## Como ejecutar las pruebas

```bash
python -m unittest -v
```

Las pruebas verifican LIFO en la pila, FIFO y restauración del primer turno en la cola, y las operaciones de agregar, buscar, listar y eliminar en la lista enlazada.

## Estructuras implementadas

- **Pila (`pila.py`)**: registra las acciones de operador. `push` agrega una acción y `pop` permite deshacer la acción más reciente. LIFO es adecuado porque la última acción realizada es la primera que se debe revertir.
- **Cola (`cola.py`)**: mantiene los turnos pendientes con referencias `head` y `tail`. `enqueue` inserta al final y `dequeue` retira desde el frente, siguiendo FIFO. Ambas operaciones son O(1).
- **Lista enlazada (`lista.py`)**: guarda clientes registrados (DNI y nombre). Permite agregar, buscar por nombre y mostrar todos los clientes mediante un recorrido desde la cabeza.

## Tabla de complejidades

| Operación | Estructura | Complejidad | Justificación |
|---|---|---:|---|
| `push` / `pop` / `peek` | Pila | O(1) | Solo se modifica o consulta el nodo del tope. |
| `enqueue` / `dequeue` | Cola | O(1) | `tail` y `head` permiten insertar al final y retirar del frente sin recorrer nodos. |
| Restaurar al frente (`enqueue_front`) | Cola | O(1) | Se enlaza un nuevo nodo antes de `head`. |
| Listar turnos pendientes | Cola | O(n) | Se visita cada nodo de la cola. |
| Agregar cliente | Lista enlazada | O(n) | La implementación recorre hasta el último nodo porque solo mantiene la cabeza. |
| Buscar por nombre | Lista enlazada | O(n) | En el peor caso se revisan todos los clientes. |
| Mostrar clientes registrados | Lista enlazada | O(n) | Se recorre cada nodo desde la cabeza. |
| Eliminar por DNI | Lista/cola | O(n) | Se busca el nodo que contiene el DNI recorriendo la estructura. |
| Validar DNI duplicado en el menú | Lista enlazada | O(n) | Se recorre la lista de clientes registrados. |

## Menú
1. Registrar cliente y turno.
2. Atender siguiente turno.
3. Mostrar turnos pendientes.
4. Buscar cliente por nombre.
5. Mostrar clientes registrados.
6. Deshacer última acción.
0. Salir.

El historial guarda acciones de registro y atención. Al deshacer un registro, el cliente se elimina de la lista y de la cola pendiente. Al deshacer una atención, el cliente vuelve al frente de la cola para conservar el orden de llegada.

## Repositorio GitHub
Nombre solicitado por la actividad: `apellido_nombre_AlgEstDatos_U1`.

Después de crear el repositorio público, reemplace el enlace de ejemplo en el informe PDF por el enlace real. No se ha creado ni publicado un repositorio desde este archivo local.
