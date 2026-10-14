from collections import deque


class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(
                    nodo_actual.izquierdo, valor
                )
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(
                    nodo_actual.derecho, valor
                )

    def bfs(self):
        resultado = []

        if self.raiz is None:
            return resultado

        cola = deque([self.raiz])

        while cola:
            nodo_actual = cola.popleft()
            resultado.append(nodo_actual.valor)

            if nodo_actual.izquierdo is not None:
                cola.append(nodo_actual.izquierdo)

            if nodo_actual.derecho is not None:
                cola.append(nodo_actual.derecho)

        return resultado

arbol = ArbolBinarioBusqueda()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(numero)

print("Recorrido por niveles (BFS):", arbol.bfs())
