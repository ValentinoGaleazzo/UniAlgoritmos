import networkx as nx

class Maravilla:
    def __init__(self, nombre, paises, tipo):
        self.nombre = nombre
        self.paises = paises  # lista de países en los que se encuentra la maravilla
        self.tipo = tipo  # tipo: 'natural' o 'arquitectónica'

class GrafoMaravillas:
    def __init__(self):
        self.grafo_natural = nx.Graph()
        self.grafo_arquitectonico = nx.Graph()
        self.maravillas = []

    def agregar_maravilla(self, maravilla, conexiones):
        # Agrega la maravilla al grafo correspondiente y las conexiones con las distancias
        self.maravillas.append(maravilla)
        
        if maravilla.tipo == 'natural':
            grafo = self.grafo_natural
        elif maravilla.tipo == 'arquitectónica':
            grafo = self.grafo_arquitectonico
        else:
            raise ValueError("Tipo de maravilla no válido.")
        
        grafo.add_node(maravilla.nombre, paises=maravilla.paises, tipo=maravilla.tipo)
        
        # Agregar conexiones con distancia a las otras maravillas del mismo tipo
        for destino, distancia in conexiones.items():
            grafo.add_edge(maravilla.nombre, destino, weight=distancia)
    
    def arbol_expansion_minimo(self, tipo):
        if tipo == 'natural':
            return nx.minimum_spanning_tree(self.grafo_natural)
        elif tipo == 'arquitectónica':
            return nx.minimum_spanning_tree(self.grafo_arquitectonico)
        else:
            raise ValueError("Tipo de maravilla no válido.")
    
    def paises_con_ambos_tipos(self):
        paises_arquitectonicos = set()
        paises_naturales = set()

        for maravilla in self.maravillas:
            if maravilla.tipo == 'natural':
                paises_naturales.update(maravilla.paises)
            elif maravilla.tipo == 'arquitectónica':
                paises_arquitectonicos.update(maravilla.paises)
        
        return paises_arquitectonicos & paises_naturales

    def paises_con_multiples_maravillas(self, tipo):
        contador_paises = {}
        
        for maravilla in self.maravillas:
            if maravilla.tipo == tipo:
                for pais in maravilla.paises:
                    if pais in contador_paises:
                        contador_paises[pais] += 1
                    else:
                        contador_paises[pais] = 1
        
        return {pais: count for pais, count in contador_paises.items() if count > 1}

# Ejemplo de uso
grafo = GrafoMaravillas()

# Agregar maravillas arquitectónicas (nombre, paises, tipo)
grafo.agregar_maravilla(Maravilla("Gran Muralla China", ["China"], "arquitectónica"), {
    "Petra": 1000, "Coliseo": 1200, "Chichen Itza": 1400, "Machu Picchu": 1500, "Taj Mahal": 1300, "Cristo Redentor": 1600
})

# Agregar maravillas naturales (nombre, paises, tipo)
grafo.agregar_maravilla(Maravilla("Amazonia", ["Brasil", "Perú", "Colombia"], "natural"), {
    "Bahía de Ha Long": 2000, "Cataratas del Iguazú": 2100, "Isla Jeju": 2500, "Parque Nacional de Komodo": 2300,
    "Río subterráneo de Puerto Princesa": 2400, "Montaña de la Mesa": 2200
})

# Árbol de expansión mínimo de maravillas arquitectónicas
arbol_min_arquitectonico = grafo.arbol_expansion_minimo("arquitectónica")
print("Árbol de expansión mínimo (Arquitectónicas):")
print(arbol_min_arquitectonico.edges(data=True))

# Árbol de expansión mínimo de maravillas naturales
arbol_min_natural = grafo.arbol_expansion_minimo("natural")
print("Árbol de expansión mínimo (Naturales):")
print(arbol_min_natural.edges(data=True))

# Países que tienen maravillas de ambos tipos
print("Países con maravillas de ambos tipos:")
print(grafo.paises_con_ambos_tipos())

# Países con más de una maravilla del mismo tipo
print("Países con múltiples maravillas arquitectónicas:")
print(grafo.paises_con_multiples_maravillas("arquitectónica"))
print("Países con múltiples maravillas naturales:")
print(grafo.paises_con_multiples_maravillas("natural"))