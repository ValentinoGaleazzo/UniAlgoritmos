class NodoCriatura:
    def __init__(self, nombre, derrotado_por=None, capturada_por=None, descripcion=""):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.capturada_por = capturada_por
        self.descripcion = descripcion
        self.izquierda = None
        self.derecha = None

class ArbolCriaturas:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, derrotado_por=None, descripcion=""):
        nuevo_nodo = NodoCriatura(nombre, derrotado_por, descripcion)
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, actual, nuevo_nodo):
        if nuevo_nodo.nombre < actual.nombre:
            if actual.izquierda is None:
                actual.izquierda = nuevo_nodo
            else:
                self._insertar_recursivo(actual.izquierda, nuevo_nodo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo_nodo
            else:
                self._insertar_recursivo(actual.derecha, nuevo_nodo)

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append((nodo.nombre, nodo.derrotado_por))
            self._inorden_recursivo(nodo.derecha, resultado)

    def buscar(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre)

    def _buscar_recursivo(self, nodo, nombre):
        if not nodo:
            return None
        if nodo.nombre == nombre:
            return nodo
        elif nombre < nodo.nombre:
            return self._buscar_recursivo(nodo.izquierda, nombre)
        else:
            return self._buscar_recursivo(nodo.derecha, nombre)

    def criaturas_derrotadas_por(self, heroe):
        resultado = []
        self._criaturas_derrotadas_por_recursivo(self.raiz, heroe, resultado)
        return resultado

    def _criaturas_derrotadas_por_recursivo(self, nodo, heroe, resultado):
        if nodo:
            if nodo.derrotado_por == heroe:
                resultado.append(nodo.nombre)
            self._criaturas_derrotadas_por_recursivo(nodo.izquierda, heroe, resultado)
            self._criaturas_derrotadas_por_recursivo(nodo.derecha, heroe, resultado)

    def criaturas_no_derrotadas(self):
        resultado = []
        self._criaturas_no_derrotadas_recursivo(self.raiz, resultado)
        return resultado

    def _criaturas_no_derrotadas_recursivo(self, nodo, resultado):
        if nodo:
            if nodo.derrotado_por is None:
                resultado.append(nodo.nombre)
            self._criaturas_no_derrotadas_recursivo(nodo.izquierda, resultado)
            self._criaturas_no_derrotadas_recursivo(nodo.derecha, resultado)

    def criaturas_capturadas_por(self, heroe):
        resultado = []
        self._criaturas_capturadas_por_recursivo(self.raiz, heroe, resultado)
        return resultado

    def _criaturas_capturadas_por_recursivo(self, nodo, heroe, resultado):
        if nodo:
            if nodo.capturada_por == heroe:
                resultado.append(nodo.nombre)
            self._criaturas_capturadas_por_recursivo(nodo.izquierda, resultado)
            self._criaturas_capturadas_por_recursivo(nodo.derecha, resultado)

    def modificar_nombre(self, nombre_actual, nombre_nuevo):
        nodo = self.buscar(nombre_actual)
        if nodo:
            nodo.nombre = nombre_nuevo

    def modificar_descripcion(self, nombre, descripcion):
        nodo = self.buscar(nombre)
        if nodo:
            nodo.descripcion = descripcion

    def eliminar(self, nombre):
        self.raiz = self._eliminar_recursivo(self.raiz, nombre)

    def _eliminar_recursivo(self, nodo, nombre):
        if not nodo:
            return nodo
        if nombre < nodo.nombre:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, nombre)
        elif nombre > nodo.nombre:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nombre)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            temp = self._min_valor_nodo(nodo.derecha)
            nodo.nombre = temp.nombre
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, temp.nombre)
        return nodo

    def _min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

    def listar_por_nivel(self):
        if not self.raiz:
            return []
        nivel = [self.raiz]
        resultado = []
        while nivel:
            siguiente_nivel = []
            nivel_nombres = [nodo.nombre for nodo in nivel]
            resultado.append(nivel_nombres)
            for nodo in nivel:
                if nodo.izquierda:
                    siguiente_nivel.append(nodo.izquierda)
                if nodo.derecha:
                    siguiente_nivel.append(nodo.derecha)
            nivel = siguiente_nivel
        return resultado

# Crear el árbol e insertar criaturas
arbol = ArbolCriaturas()
arbol.insertar("Ceto")
arbol.insertar("Cerda de Cromión", "Teseo")
arbol.insertar("Tifón", "Zeus")
arbol.insertar("Equidna", "Argos Panoptes")
# Continuar agregando todas las criaturas de la tabla...

# Actualizaciones y consultas específicas
arbol.modificar_nombre("Ladón", "Dragón Ladón")
arbol.modificar_descripcion("Talos", "Un guardián de bronce gigante derrotado por Medea")
arbol.buscar("Talos").capturada_por = "Medea"

# Consultas
print("Listado inorden de criaturas y derrotador:")
print(arbol.inorden())

print("Descripción de Talos:")
talos = arbol.buscar("Talos")
print(talos.descripcion if talos else "No encontrado")

print("Criaturas derrotadas por Heracles:")
print(arbol.criaturas_derrotadas_por("Heracles"))

print("Criaturas no derrotadas:")
print(arbol.criaturas_no_derrotadas())

print("Criaturas capturadas por Heracles:")
print(arbol.criaturas_capturadas_por("Heracles"))

print("Listado por nivel del árbol:")
print(arbol.listar_por_nivel())