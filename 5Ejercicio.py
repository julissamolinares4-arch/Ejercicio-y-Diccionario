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

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)

    def balancear_arbol(self):
        valores = self.inorden()
        nuevo_arbol = ArbolBinarioBusqueda()

        def construir(inicio, fin):
            if inicio > fin:
                return

            medio = (inicio + fin) // 2
            nuevo_arbol.insertar(valores[medio])

            construir(inicio, medio - 1)
            construir(medio + 1, fin)

        construir(0, len(valores) - 1)

        return nuevo_arbol

    def altura(self, nodo=None):
        if self.raiz is None:
            return -1

        if nodo is None:
            nodo = self.raiz

        return 1 + max(
            self._altura_recursiva(nodo.izquierdo),
            self._altura_recursiva(nodo.derecho)
        )

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return -1

        return 1 + max(
            self._altura_recursiva(nodo.izquierdo),
            self._altura_recursiva(nodo.derecho)
        )

arbol = ArbolBinarioBusqueda()

for numero in [1, 2, 3, 4, 5, 6, 7]:
    arbol.insertar(numero)

print("Árbol original:", arbol.inorden())
print("Altura original:", arbol.altura())

arbol_balanceado = arbol.balancear_arbol()

print("Árbol balanceado:", arbol_balanceado.inorden())
print("Altura balanceada:", arbol_balanceado.altura())

print("Árbol original conservado:", arbol.inorden())