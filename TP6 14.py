import networkx as nx

# Crear el grafo no dirigido
grafo = nx.Graph()

# Definir los ambientes de la casa
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", 
             "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

# Agregar vértices al grafo
for ambiente in ambientes:
    grafo.add_node(ambiente)

# Agregar aristas con pesos (distancias en metros) a cada vértice
aristas = [
    ("cocina", "comedor", 3),
    ("cocina", "baño 1", 4),
    ("cocina", "habitación 1", 5),
    ("comedor", "sala de estar", 7),
    ("comedor", "terraza", 4),
    ("comedor", "cocina", 3),
    ("cochera", "quincho", 6),
    ("cochera", "patio", 10),
    ("cochera", "terraza", 8),
    ("quincho", "terraza", 3),
    ("quincho", "baño 2", 6),
    ("baño 1", "habitación 1", 2),
    ("baño 2", "habitación 2", 5),
    ("habitación 1", "sala de estar", 8),
    ("habitación 2", "terraza", 7),
    ("sala de estar", "patio", 6),
    ("terraza", "patio", 5),
]

# Cargar aristas en el grafo con sus pesos
for origen, destino, distancia in aristas:
    grafo.add_edge(origen, destino, weight=distancia)

# Obtener el árbol de expansión mínima para determinar los metros de cables necesarios
arbol_expansion_minima = nx.minimum_spanning_tree(grafo)
total_metros_cable = sum(data['weight'] for _, _, data in arbol_expansion_minima.edges(data=True))

print("Árbol de expansión mínima:")
for edge in arbol_expansion_minima.edges(data=True):
    print(f"{edge[0]} - {edge[1]}: {edge[2]['weight']} metros")

print(f"Total de metros de cable para conectar todos los ambientes: {total_metros_cable} metros")

# Determinar el camino más corto desde 'habitación 1' hasta 'sala de estar'
camino_corto = nx.shortest_path(grafo, source="habitación 1", target="sala de estar", weight="weight")
distancia_camino_corto = nx.shortest_path_length(grafo, source="habitación 1", target="sala de estar", weight="weight")

print("\nCamino más corto desde 'habitación 1' hasta 'sala de estar':")
print(" -> ".join(camino_corto))
print(f"Metros de cable necesarios para conectar el router con el Smart TV: {distancia_camino_corto} metros")