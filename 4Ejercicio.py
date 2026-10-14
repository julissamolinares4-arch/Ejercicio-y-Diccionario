
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

    def es_completo(self):
        return self._es_completo_recursivo(self.raiz)

    def _es_completo_recursivo(self, nodo):
        if nodo is None:
            return True

        tiene_izquierdo = nodo.izquierdo is not None
        tiene_derecho = nodo.derecho is not None

        
        if tiene_izquierdo != tiene_derecho:
            return False

        return (
            self._es_completo_recursivo(nodo.izquierdo)
            and self._es_completo_recursivo(nodo.derecho)
        )

arbol1 = ArbolBinarioBusqueda()

for numero in [4, 2, 6, 1, 3, 5, 7]:
    arbol1.insertar(numero)

print("Árbol 1:", arbol1.es_completo())

arbol2 = ArbolBinarioBusqueda()

for numero in [4, 2, 6, 1, 3, 5]:
    arbol2.insertar(numero)

print("Árbol 2:", arbol2.es_completo())
