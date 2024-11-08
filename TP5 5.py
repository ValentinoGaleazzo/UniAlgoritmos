class NodoPersonaje:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izquierda = None
        self.derecha = None

class ArbolPersonajes:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        nuevo_nodo = NodoPersonaje(nombre, es_heroe)
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

    def listar_villanos(self):
        villanos = []
        self._listar_villanos_recursivo(self.raiz, villanos)
        return sorted(villanos)

    def _listar_villanos_recursivo(self, nodo, villanos):
        if nodo:
            self._listar_villanos_recursivo(nodo.izquierda, villanos)
            if not nodo.es_heroe:
                villanos.append(nodo.nombre)
            self._listar_villanos_recursivo(nodo.derecha, villanos)

    def listar_heroes_con_C(self):
        heroes_C = []
        self._listar_heroes_con_C_recursivo(self.raiz, heroes_C)
        return heroes_C

    def _listar_heroes_con_C_recursivo(self, nodo, heroes_C):
        if nodo:
            self._listar_heroes_con_C_recursivo(nodo.izquierda, heroes_C)
            if nodo.es_heroe and nodo.nombre.startswith("C"):
                heroes_C.append(nodo.nombre)
            self._listar_heroes_con_C_recursivo(nodo.derecha, heroes_C)

    def contar_heroes(self):
        return self._contar_heroes_recursivo(self.raiz)

    def _contar_heroes_recursivo(self, nodo):
        if not nodo:
            return 0
        count = 1 if nodo.es_heroe else 0
        return count + self._contar_heroes_recursivo(nodo.izquierda) + self._contar_heroes_recursivo(nodo.derecha)

    def buscar_proximidad(self, nombre):
        return self._buscar_proximidad_recursivo(self.raiz, nombre)

    def _buscar_proximidad_recursivo(self, nodo, nombre):
        if not nodo:
            return None
        if nombre.lower() in nodo.nombre.lower():
            return nodo
        izquierda = self._buscar_proximidad_recursivo(nodo.izquierda, nombre)
        if izquierda:
            return izquierda
        return self._buscar_proximidad_recursivo(nodo.derecha, nombre)

    def listar_heroes_descendente(self):
        heroes = []
        self._listar_heroes_descendente_recursivo(self.raiz, heroes)
        return sorted(heroes, reverse=True)

    def _listar_heroes_descendente_recursivo(self, nodo, heroes):
        if nodo:
            self._listar_heroes_descendente_recursivo(nodo.izquierda, heroes)
            if nodo.es_heroe:
                heroes.append(nodo.nombre)
            self._listar_heroes_descendente_recursivo(nodo.derecha, heroes)

    def generar_bosque(self):
        arbol_heroes = ArbolPersonajes()
        arbol_villanos = ArbolPersonajes()
        self._generar_bosque_recursivo(self.raiz, arbol_heroes, arbol_villanos)
        return arbol_heroes, arbol_villanos

    def _generar_bosque_recursivo(self, nodo, arbol_heroes, arbol_villanos):
        if nodo:
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            self._generar_bosque_recursivo(nodo.izquierda, arbol_heroes, arbol_villanos)
            self._generar_bosque_recursivo(nodo.derecha, arbol_heroes, arbol_villanos)

    def contar_nodos(self):
        return self._contar_nodos_recursivo(self.raiz)

    def _contar_nodos_recursivo(self, nodo):
        if not nodo:
            return 0
        return 1 + self._contar_nodos_recursivo(nodo.izquierda) + self._contar_nodos_recursivo(nodo.derecha)

    def barrido_alfabetico(self):
        return self._barrido_alfabetico_recursivo(self.raiz, [])

    def _barrido_alfabetico_recursivo(self, nodo, resultado):
        if nodo:
            self._barrido_alfabetico_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.nombre)
            self._barrido_alfabetico_recursivo(nodo.derecha, resultado)
        return resultado

# Crear el árbol de personajes e insertar algunos personajes de prueba
arbol = ArbolPersonajes()
arbol.insertar("Iron Man", True)
arbol.insertar("Thanos", False)
arbol.insertar("Captain America", True)
arbol.insertar("Loki", False)
arbol.insertar("Doctor Strange", True)
arbol.insertar("Red Skull", False)

# Consultas específicas
# b. Listar villanos alfabéticamente
print("Villanos ordenados alfabéticamente:")
print(arbol.listar_villanos())

# c. Mostrar superhéroes que empiezan con "C"
print("Superhéroes que empiezan con 'C':")
print(arbol.listar_heroes_con_C())

# d. Contar superhéroes en el árbol
print("Cantidad de superhéroes en el árbol:")
print(arbol.contar_heroes())

# e. Corregir "Doctor Strange" con búsqueda de proximidad
doctor_strange = arbol.buscar_proximidad("Doctor Strange")
if doctor_strange:
    doctor_strange.nombre = "Doctor Stephen Strange"
print("Nombre corregido de Doctor Strange:", doctor_strange.nombre)

# f. Listar héroes ordenados de manera descendente
print("Héroes ordenados en forma descendente:")
print(arbol.listar_heroes_descendente())

# g. Generar bosque y resolver consultas
arbol_heroes, arbol_villanos = arbol.generar_bosque()

print("Cantidad de nodos en el árbol de héroes:", arbol_heroes.contar_nodos())
print("Cantidad de nodos en el árbol de villanos:", arbol_villanos.contar_nodos())

print("Barrido alfabético de héroes:")
print(arbol_heroes.barrido_alfabetico())

print("Barrido alfabético de villanos:")
print(arbol_villanos.barrido_alfabetico())