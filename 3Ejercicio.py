
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

    def sumar_elementos(self):
        return self._sumar_recursivo(self.raiz)

    def _sumar_recursivo(self, nodo):
        if nodo is None:
            return 0

        return (
            nodo.valor
            + self._sumar_recursivo(nodo.izquierdo)
            + self._sumar_recursivo(nodo.derecho)
        )

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)


arbol = ArbolBinarioBusqueda()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(numero)

print("Elementos del árbol:", arbol.inorden())
print("Suma de todos los elementos:", arbol.sumar_elementos())
print("Árbol original después de sumar:", arbol.inorden())
