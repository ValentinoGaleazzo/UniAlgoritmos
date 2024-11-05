#2)A)
class Grafo:
    def __init__(self):
        self.vertices = {}  # Diccionario de personajes y sus conexiones

    def agregar_personaje(self, nombre):
        if nombre not in self.vertices:
            self.vertices[nombre] = {}

    def agregar_conexion(self, personaje1, personaje2, episodios):
        self.agregar_personaje(personaje1)
        self.agregar_personaje(personaje2)
        # Añadimos la conexión en ambas direcciones, ya que es un grafo no dirigido
        self.vertices[personaje1][personaje2] = episodios
        self.vertices[personaje2][personaje1] = episodios

    def obtener_episodios_compartidos(self):
        max_episodios = 0
        personajes = ()
        for personaje1 in self.vertices:
            for personaje2 in self.vertices[personaje1]:
                if personaje1 != personaje2:
                    episodios = self.vertices[personaje1][personaje2]
                    if episodios > max_episodios:
                        max_episodios = episodios
                        personajes = (personaje1, personaje2)
        return max_episodios, personajes

    def prim(self):
        import heapq

        # Usamos un min-heap para seleccionar la conexión de menor peso
        mst = []
        visitados = set()
        if not self.vertices:
            return mst

        # Comenzamos con el primer personaje
        primer_personaje = next(iter(self.vertices))
        visitados.add(primer_personaje)
        edges = [
            (peso, primer_personaje, vecino)
            for vecino, peso in self.vertices[primer_personaje].items()
        ]
        heapq.heapify(edges)

        while edges:
            peso, personaje1, personaje2 = heapq.heappop(edges)
            if personaje2 not in visitados:
                visitados.add(personaje2)
                mst.append((personaje1, personaje2, peso))
                for vecino, peso in self.vertices[personaje2].items():
                    if vecino not in visitados:
                        heapq.heappush(edges, (peso, personaje2, vecino))

        return mst

    def contiene_yoda(self, mst):
        return any("Yoda" in (p1, p2) for p1, p2, _ in mst)

# Creando el grafo
grafo = Grafo()

# D) Agregando personajes y sus conexiones (episodios compartidos)
grafo.agregar_conexion("Luke Skywalker", "Darth Vader", 5)
grafo.agregar_conexion("Luke Skywalker", "Yoda", 4)
grafo.agregar_conexion("Yoda", "Darth Vader", 2)
grafo.agregar_conexion("Boba Fett", "Han Solo", 3)
grafo.agregar_conexion("Leia", "Han Solo", 6)
grafo.agregar_conexion("Rey", "Kylo Ren", 4)
grafo.agregar_conexion("Chewbacca", "Han Solo", 5)
grafo.agregar_conexion("C-3PO", "R2-D2", 7)
grafo.agregar_conexion("BB-8", "Rey", 3)

# C) Hallar el número máximo de episodios que comparten dos personajes
max_episodios, personajes = grafo.obtener_episodios_compartidos()
print(f"El número máximo de episodios que comparten dos personajes es {max_episodios} entre {personajes[0]} y {personajes[1]}.")

# B) Hallar el árbol de expansión mínimo
arbol_expansion_minimo = grafo.prim()
print("Árbol de expansión mínimo:")
for p1, p2, peso in arbol_expansion_minimo:
    print(f"{p1} - {p2}: {peso}")

# B) Verificar si contiene a Yoda
if grafo.contiene_yoda(arbol_expansion_minimo):
    print("El árbol de expansión mínimo contiene a Yoda.")
else:
    print("El árbol de expansión mínimo no contiene a Yoda.")