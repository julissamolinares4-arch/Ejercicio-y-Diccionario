
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

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(
                nodo.izquierdo, valor
            )
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(
                nodo.derecho, valor
            )
        else:
            
            if nodo.izquierdo is None:
                return nodo.derecho

            if nodo.derecho is None:
                return nodo.izquierdo

            sucesor = nodo.derecho

            while sucesor.izquierdo is not None:
                sucesor = sucesor.izquierdo

            nodo.valor = sucesor.valor

            nodo.derecho = self._eliminar_recursivo(
                nodo.derecho, sucesor.valor
            )

        return nodo


arbol = ArbolBinarioBusqueda()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(numero)

print("Árbol original:", arbol.inorden())

arbol.eliminar(20)
print("Después de eliminar 20:", arbol.inorden())

arbol.insertar(25)
arbol.eliminar(30)
print("Después de eliminar 30:", arbol.inorden())

arbol.eliminar(70)
print("Después de eliminar 70:", arbol.inorden())
   