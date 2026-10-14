
class Palabra:
    """Representa una palabra y su definicion."""

    def __init__(self, texto, definicion):
        self.texto = texto.strip().lower()
        self.definicion = definicion.strip()

    def __str__(self):
        return f"{self.texto}: {self.definicion}"


class NodoArbol:
    """Representa un nodo del arbol."""

    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    """Administra las palabras mediante un arbol binario de busqueda."""

    def __init__(self):
        self.raiz = None

    def insertar(self, palabra):
        if self.raiz is None:
            self.raiz = NodoArbol(palabra)
        else:
            self._insertar_recursivo(self.raiz, palabra)

    def _insertar_recursivo(self, nodo, palabra):
        if palabra.texto < nodo.palabra.texto:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(palabra)
            else:
                self._insertar_recursivo(nodo.izquierdo, palabra)

        elif palabra.texto > nodo.palabra.texto:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(palabra)
            else:
                self._insertar_recursivo(nodo.derecho, palabra)

        else:
            nodo.palabra.definicion = palabra.definicion

    def buscar(self, texto):
        texto = texto.strip().lower()
        return self._buscar_recursivo(self.raiz, texto)

    def _buscar_recursivo(self, nodo, texto):
        if nodo is None:
            return None

        if texto == nodo.palabra.texto:
            return nodo.palabra

        if texto < nodo.palabra.texto:
            return self._buscar_recursivo(nodo.izquierdo, texto)

        return self._buscar_recursivo(nodo.derecho, texto)

    def obtener_todos(self):
        palabras = []
        self._obtener_todos_recursivo(self.raiz, palabras)
        return palabras

    def _obtener_todos_recursivo(self, nodo, palabras):
        if nodo is not None:
            self._obtener_todos_recursivo(nodo.izquierdo, palabras)
            palabras.append(nodo.palabra)
            self._obtener_todos_recursivo(nodo.derecho, palabras)

    def buscar_por_prefijo(self, prefijo):
        prefijo = prefijo.strip().lower()

        if not prefijo:
            return []

        resultados = []
        self._buscar_prefijo_recursivo(
            self.raiz, prefijo, resultados
        )
        return resultados

    def _buscar_prefijo_recursivo(self, nodo, prefijo, resultados):
        if nodo is not None:
            self._buscar_prefijo_recursivo(
                nodo.izquierdo, prefijo, resultados
            )

            if nodo.palabra.texto.startswith(prefijo):
                resultados.append(nodo.palabra)

            self._buscar_prefijo_recursivo(
                nodo.derecho, prefijo, resultados
            )

def cargar_diccionario(arbol):
    palabras = [
        ("algoritmo", "Conjunto de pasos para resolver un problema."),
        ("almacenamiento", "Proceso de guardar informacion."),
        ("analisis", "Estudio detallado de datos o situaciones."),
        ("aplicacion", "Programa informatico para realizar tareas."),
        ("archivo", "Conjunto de datos guardados con un nombre."),
        ("arbol", "Estructura de datos formada por nodos relacionados."),
        ("arreglo", "Estructura que almacena varios elementos."),
        ("atributo", "Caracteristica o propiedad de un objeto."),
        ("autenticacion", "Proceso de verificar una identidad."),
        ("base", "Fundamento sobre el que se construye algo."),
        ("base de datos", "Conjunto organizado de datos relacionados."),
        ("bit", "Unidad minima de informacion digital."),
        ("byte", "Unidad de informacion formada normalmente por ocho bits."),
        ("busqueda", "Proceso de localizar un elemento."),
        ("cadena", "Secuencia de caracteres de texto."),
        ("campo", "Unidad de informacion dentro de un registro."),
        ("caracter", "Simbolo que forma parte de un texto."),
        ("ciberseguridad", "Proteccion de sistemas y datos frente a amenazas."),
        ("cliente", "Persona o sistema que solicita un servicio."),
        ("codigo", "Instrucciones escritas para un programa."),
        ("compilador", "Programa que traduce codigo fuente."),
        ("computadora", "Dispositivo electronico que procesa datos."),
        ("condicional", "Instruccion que permite tomar decisiones."),
        ("consola", "Interfaz de texto para interactuar con un programa."),
        ("contraseña", "Secreto utilizado para verificar el acceso."),
        ("dato", "Representacion de un hecho o valor."),
        ("depuracion", "Proceso de localizar y corregir errores."),
        ("diccionario", "Coleccion de palabras con sus definiciones."),
        ("direccion", "Referencia que indica donde se encuentra un recurso."),
        ("disco", "Dispositivo utilizado para almacenar informacion."),
        ("documento", "Archivo que contiene informacion."),
        ("encapsulamiento", "Principio que protege los datos de un objeto."),
        ("entrada", "Informacion que recibe un programa."),
        ("estructura", "Forma en que se organizan los elementos."),
        ("etiqueta", "Marca que identifica un elemento."),
        ("funcion", "Bloque de codigo que realiza una tarea."),
        ("hardware", "Componentes fisicos de una computadora."),
        ("herencia", "Mecanismo para reutilizar caracteristicas de una clase."),
        ("informacion", "Datos organizados que tienen significado."),
        ("insercion", "Operacion de agregar un elemento."),
        ("interfaz", "Medio de comunicacion entre usuario y sistema."),
        ("internet", "Red mundial de redes interconectadas."),
        ("iteracion", "Repeticion de un conjunto de instrucciones."),
        ("lenguaje", "Sistema de simbolos y reglas para comunicarse."),
        ("lista", "Coleccion ordenada de elementos."),
        ("memoria", "Componente que almacena datos e instrucciones."),
        ("metodo", "Funcion definida dentro de una clase."),
        ("modulo", "Archivo o componente que agrupa funcionalidades."),
        ("nodo", "Elemento que almacena datos y enlaces en una estructura."),
        ("objeto", "Instancia de una clase."),
        ("operador", "Simbolo que realiza una operacion."),
        ("ordenamiento", "Proceso de organizar elementos segun un criterio."),
        ("palabra", "Unidad del lenguaje formada por caracteres."),
        ("parametro", "Variable que recibe un valor en una funcion."),
        ("programacion", "Proceso de crear instrucciones para una computadora."),
        ("programa", "Conjunto de instrucciones ejecutables."),
        ("python", "Lenguaje de programacion de alto nivel."),
        ("registro", "Conjunto de campos relacionados."),
        ("recorrido", "Visita organizada de los nodos de una estructura."),
        ("recursividad", "Tecnica en la que una funcion se llama a si misma."),
        ("red", "Conjunto de dispositivos conectados."),
        ("servidor", "Sistema que ofrece servicios a otros equipos."),
        ("software", "Conjunto de programas y componentes logicos."),
        ("sistema", "Conjunto de elementos que trabajan relacionados."),
        ("teclado", "Dispositivo utilizado para introducir texto."),
        ("terminal", "Interfaz para ejecutar comandos."),
        ("texto", "Secuencia de caracteres que transmite informacion."),
        ("variable", "Nombre asociado a un valor que puede cambiar."),
        ("verificacion", "Proceso de comprobar que algo es correcto."),
        ("virus", "Programa malicioso que puede afectar un sistema."),
    ]

    for texto, definicion in palabras:
        arbol.insertar(Palabra(texto, definicion))


def mostrar_menu():
    print("\n" + "=" * 45)
    print("       DICCIONARIO INTELIGENTE")
    print("=" * 45)
    print("1. Buscar una palabra exacta")
    print("2. Buscar palabras por prefijo")
    print("3. Mostrar diccionario en orden alfabetico")
    print("4. Mostrar cantidad de palabras")
    print("5. Salir")
    print("=" * 45)


def main():
    arbol = ArbolBinarioBusqueda()
    cargar_diccionario(arbol)

    print("Diccionario cargado correctamente.")
    print("Total de palabras:", len(arbol.obtener_todos()))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            texto = input("Escriba la palabra: ").strip()
            resultado = arbol.buscar(texto)

            if resultado is not None:
                print("\nPalabra encontrada:")
                print(resultado)
            else:
                print("\nLa palabra no se encuentra en el diccionario.")

        elif opcion == "2":
            prefijo = input("Escriba el prefijo: ").strip()
            resultados = arbol.buscar_por_prefijo(prefijo)

            if resultados:
                print("\nPalabras encontradas:")
                for palabra in resultados:
                    print(palabra)
            else:
                print("\nNo se encontraron palabras con ese prefijo.")

        elif opcion == "3":
            print("\nDICCIONARIO EN ORDEN ALFABETICO")
            print("-" * 45)

            for palabra in arbol.obtener_todos():
                print(palabra)

        elif opcion == "4":
            print(
                "\nCantidad de palabras:",
                len(arbol.obtener_todos())
            )

        elif opcion == "5":
            print("\nGracias por utilizar el Diccionario Inteligente.")
            break

        else:
            print("\nOpcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()
