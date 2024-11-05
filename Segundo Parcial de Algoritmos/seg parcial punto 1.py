# Lista de Pokémon
pokemons = [
    {"numero": 448, "nombre": "Lucario", "tipos": ["Lucha", "Acero"]},
    {"numero": 25, "nombre": "Pikachu", "tipos": ["Eléctrico"]},
    {"numero": 850, "nombre": "Sizzlipede", "tipos": ["Fuego", "Bicho"]},
    {"numero": 196, "nombre": "Espeon", "tipos": ["Psíquico"]},
    {"numero": 6, "nombre": "Charizard", "tipos": ["Fuego", "Volador"]},
    {"numero": 809, "nombre": "Melmetal", "tipos": ["Acero"]},
    {"numero": 387, "nombre": "Turtwig", "tipos": ["Planta"]},
    {"numero": 131, "nombre": "Lapras", "tipos": ["Agua", "Hielo"]},
    {"numero": 94, "nombre": "Gengar", "tipos": ["Fantasma", "Veneno"]},
    {"numero": 808, "nombre": "Meltan", "tipos": ["Acero"]},
    {"numero": 135, "nombre": "Jolteon", "tipos": ["Eléctrico"]},
    {"numero": 745, "nombre": "Lycanroc", "tipos": ["Roca"]},
    {"numero": 697, "nombre": "Tyrantrum", "tipos": ["Roca", "Dragón"]},
]

#---------------------

# 1)A)
class NodoPokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.izquierda = None
        self.derecha = None

class ArbolPokemon:
    def __init__(self, indice):
        self.raiz = None
        self.indice = indice  # Indica el campo por el que se ordena el árbol

    def insertar(self, pokemon):
        if self.raiz is None:
            self.raiz = NodoPokemon(pokemon)
        else:
            self._insertar_recursivo(self.raiz, pokemon)

    def _insertar_recursivo(self, nodo, pokemon):
        # Determina el valor del índice en función del atributo de ordenación
        valor_pokemon = pokemon[self.indice] if self.indice != "tipos" else pokemon["tipos"][0]
        valor_nodo = nodo.pokemon[self.indice] if self.indice != "tipos" else nodo.pokemon["tipos"][0]

        # Comparación de acuerdo al valor
        if valor_pokemon < valor_nodo:
            if nodo.izquierda is None:
                nodo.izquierda = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.izquierda, pokemon)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.derecha, pokemon)

    def mostrar_en_orden(self):
        self._mostrar_en_orden_recursivo(self.raiz)

    def _mostrar_en_orden_recursivo(self, nodo):
        if nodo is not None:
            self._mostrar_en_orden_recursivo(nodo.izquierda)
            print(nodo.pokemon)
            self._mostrar_en_orden_recursivo(nodo.derecha)

# Crear árboles por nombre, número y tipo
arbol_por_nombre = ArbolPokemon("nombre")
arbol_por_numero = ArbolPokemon("numero")
arbol_por_tipo = ArbolPokemon("tipos")

# Insertar Pokémon en cada árbol
for pokemon in pokemons:
    arbol_por_nombre.insertar(pokemon)
    arbol_por_numero.insertar(pokemon)
    arbol_por_tipo.insertar(pokemon)

#---------------------

# Mostrar los Pokémon en orden para cada árbol
print("Pokémon ordenados por nombre:")
arbol_por_nombre.mostrar_en_orden()

print("\nPokémon ordenados por número:")
arbol_por_numero.mostrar_en_orden()

print("\nPokémon ordenados por tipo (primer tipo):")
arbol_por_tipo.mostrar_en_orden()

#---------------------

# 1)B)
class NodoPokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.izquierda = None
        self.derecha = None

class ArbolPokemon:
    def __init__(self, indice):
        self.raiz = None
        self.indice = indice  # Indica el campo por el que se ordena el árbol

    def insertar(self, pokemon):
        if self.raiz is None:
            self.raiz = NodoPokemon(pokemon)
        else:
            self._insertar_recursivo(self.raiz, pokemon)

    def _insertar_recursivo(self, nodo, pokemon):
        # Determina el valor del índice en función del atributo de ordenación
        valor_pokemon = pokemon[self.indice] if self.indice != "tipos" else pokemon["tipos"][0]
        valor_nodo = nodo.pokemon[self.indice] if self.indice != "tipos" else nodo.pokemon["tipos"][0]

        if valor_pokemon < valor_nodo:
            if nodo.izquierda is None:
                nodo.izquierda = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.izquierda, pokemon)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.derecha, pokemon)

    def mostrar_en_orden(self):
        self._mostrar_en_orden_recursivo(self.raiz)

    def _mostrar_en_orden_recursivo(self, nodo):
        if nodo is not None:
            self._mostrar_en_orden_recursivo(nodo.izquierda)
            print(nodo.pokemon)
            self._mostrar_en_orden_recursivo(nodo.derecha)

    def buscar_por_numero(self, numero):
        """Buscar Pokémon por número exacto."""
        return self._buscar_por_numero_recursivo(self.raiz, numero)

    def _buscar_por_numero_recursivo(self, nodo, numero):
        if nodo is None:
            return None
        if nodo.pokemon["numero"] == numero:
            return nodo.pokemon
        elif numero < nodo.pokemon["numero"]:
            return self._buscar_por_numero_recursivo(nodo.izquierda, numero)
        else:
            return self._buscar_por_numero_recursivo(nodo.derecha, numero)

    def buscar_por_nombre_aproximado(self, texto):
        """Buscar Pokémon por nombre aproximado (contiene 'texto')."""
        resultados = []
        self._buscar_por_nombre_aproximado_recursivo(self.raiz, texto.lower(), resultados)
        return resultados

    def _buscar_por_nombre_aproximado_recursivo(self, nodo, texto, resultados):
        if nodo is not None:
            nombre_pokemon = nodo.pokemon["nombre"].lower()
            if texto in nombre_pokemon:
                resultados.append(nodo.pokemon)
            self._buscar_por_nombre_aproximado_recursivo(nodo.izquierda, texto, resultados)
            self._buscar_por_nombre_aproximado_recursivo(nodo.derecha, texto, resultados)

            # Crear el árbol por número y nombre para búsquedas
arbol_por_numero = ArbolPokemon("numero")
arbol_por_nombre = ArbolPokemon("nombre")

# Insertar Pokémon en cada árbol
for pokemon in pokemons:
    arbol_por_numero.insertar(pokemon)
    arbol_por_nombre.insertar(pokemon)

#---------------------

# Buscar por número exacto
numero_a_buscar = 25
resultado_numero = arbol_por_numero.buscar_por_numero(numero_a_buscar)
print(f"Resultado de búsqueda por número ({numero_a_buscar}): {resultado_numero}")

# Buscar por nombre aproximado
nombre_a_buscar = "lu"
resultados_nombre = arbol_por_nombre.buscar_por_nombre_aproximado(nombre_a_buscar)
print(f"\nResultados de búsqueda por nombre aproximado ('{nombre_a_buscar}'):")
for pokemon in resultados_nombre:
    print(pokemon)

#---------------------

#1)C)
class NodoPokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.izquierda = None
        self.derecha = None

class ArbolPokemon:
    def __init__(self, indice):
        self.raiz = None
        self.indice = indice  # Indica el campo por el que se ordena el árbol

    def insertar(self, pokemon):
        if self.raiz is None:
            self.raiz = NodoPokemon(pokemon)
        else:
            self._insertar_recursivo(self.raiz, pokemon)

    def _insertar_recursivo(self, nodo, pokemon):
        valor_pokemon = pokemon[self.indice] if self.indice != "tipos" else pokemon["tipos"][0]
        valor_nodo = nodo.pokemon[self.indice] if self.indice != "tipos" else nodo.pokemon["tipos"][0]

        if valor_pokemon < valor_nodo:
            if nodo.izquierda is None:
                nodo.izquierda = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.izquierda, pokemon)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.derecha, pokemon)

    def mostrar_en_orden(self):
        self._mostrar_en_orden_recursivo(self.raiz)

    def _mostrar_en_orden_recursivo(self, nodo):
        if nodo is not None:
            self._mostrar_en_orden_recursivo(nodo.izquierda)
            print(nodo.pokemon)
            self._mostrar_en_orden_recursivo(nodo.derecha)

    def buscar_por_tipo(self, tipo):
        """Buscar todos los nombres de Pokémon que tengan el tipo especificado."""
        resultados = []
        self._buscar_por_tipo_recursivo(self.raiz, tipo.capitalize(), resultados)
        return resultados

    def _buscar_por_tipo_recursivo(self, nodo, tipo, resultados):
        if nodo is not None:
            # Verificar si el tipo está en la lista de tipos del Pokémon
            if tipo in nodo.pokemon["tipos"]:
                resultados.append(nodo.pokemon["nombre"])
            self._buscar_por_tipo_recursivo(nodo.izquierda, tipo, resultados)
            self._buscar_por_tipo_recursivo(nodo.derecha, tipo, resultados)


# Crear el árbol por tipo para búsquedas por tipo
arbol_por_tipo = ArbolPokemon("tipos")

# Insertar Pokémon en el árbol
for pokemon in pokemons:
    arbol_por_tipo.insertar(pokemon)

#---------------------

# Buscar Pokémon de tipo Agua
tipo_a_buscar = "Agua"
resultados_tipo = arbol_por_tipo.buscar_por_tipo(tipo_a_buscar)
print(f"Pokémon de tipo '{tipo_a_buscar}': {resultados_tipo}")

#---------------------

#1)D)
from collections import deque

class NodoPokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.izquierda = None
        self.derecha = None

class ArbolPokemon:
    def __init__(self, indice):
        self.raiz = None
        self.indice = indice  # Indica el campo por el que se ordena el árbol

    def insertar(self, pokemon):
        if self.raiz is None:
            self.raiz = NodoPokemon(pokemon)
        else:
            self._insertar_recursivo(self.raiz, pokemon)

    def _insertar_recursivo(self, nodo, pokemon):
        valor_pokemon = pokemon[self.indice] if self.indice != "tipos" else pokemon["tipos"][0]
        valor_nodo = nodo.pokemon[self.indice] if self.indice != "tipos" else nodo.pokemon["tipos"][0]

        if valor_pokemon < valor_nodo:
            if nodo.izquierda is None:
                nodo.izquierda = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.izquierda, pokemon)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.derecha, pokemon)

    def mostrar_en_orden(self):
        """Muestra los Pokémon en orden ascendente."""
        elementos = []
        self._mostrar_en_orden_recursivo(self.raiz, elementos)
        return elementos

    def _mostrar_en_orden_recursivo(self, nodo, elementos):
        if nodo is not None:
            self._mostrar_en_orden_recursivo(nodo.izquierda, elementos)
            elementos.append(nodo.pokemon)
            self._mostrar_en_orden_recursivo(nodo.derecha, elementos)

    def mostrar_por_nivel(self):
        """Muestra los Pokémon por nivel en el árbol."""
        if self.raiz is None:
            return []

        resultados = []
        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            resultados.append(nodo.pokemon)

            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)

        return resultados
    
    # Crear árboles por número y por nombre
arbol_por_numero = ArbolPokemon("numero")
arbol_por_nombre = ArbolPokemon("nombre")

# Insertar Pokémon en cada árbol
for pokemon in pokemons:
    arbol_por_numero.insertar(pokemon)
    arbol_por_nombre.insertar(pokemon)

#---------------------

# Listado en orden ascendente por número
print("Listado en orden ascendente por número:")
lista_ordenada_numero = arbol_por_numero.mostrar_en_orden()
for pokemon in lista_ordenada_numero:
    print(pokemon)

# Listado en orden ascendente por nombre
print("\nListado en orden ascendente por nombre:")
lista_ordenada_nombre = arbol_por_nombre.mostrar_en_orden()
for pokemon in lista_ordenada_nombre:
    print(pokemon)

# Listado por nivel por nombre
print("\nListado por nivel (búsqueda por nombre):")
lista_por_nivel_nombre = arbol_por_nombre.mostrar_por_nivel()
for pokemon in lista_por_nivel_nombre:
    print(pokemon)

#---------------------

#1)E)
class NodoPokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.izquierda = None
        self.derecha = None

class ArbolPokemon:
    def __init__(self, indice):
        self.raiz = None
        self.indice = indice  # Indica el campo por el que se ordena el árbol

    def insertar(self, pokemon):
        if self.raiz is None:
            self.raiz = NodoPokemon(pokemon)
        else:
            self._insertar_recursivo(self.raiz, pokemon)

    def _insertar_recursivo(self, nodo, pokemon):
        valor_pokemon = pokemon[self.indice] if self.indice != "tipos" else pokemon["tipos"][0]
        valor_nodo = nodo.pokemon[self.indice] if self.indice != "tipos" else nodo.pokemon["tipos"][0]

        if valor_pokemon < valor_nodo:
            if nodo.izquierda is None:
                nodo.izquierda = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.izquierda, pokemon)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.derecha, pokemon)

    def buscar_por_nombres(self, nombres):
        """Busca Pokémon por nombres específicos y devuelve sus datos completos."""
        resultados = []
        for nombre in nombres:
            resultado = self._buscar_por_nombre_recursivo(self.raiz, nombre.capitalize())
            if resultado:
                resultados.append(resultado)
        return resultados

    def _buscar_por_nombre_recursivo(self, nodo, nombre):
        if nodo is None:
            return None
        if nodo.pokemon["nombre"].lower() == nombre.lower():
            return nodo.pokemon
        elif nombre < nodo.pokemon["nombre"]:
            return self._buscar_por_nombre_recursivo(nodo.izquierda, nombre)
        else:
            return self._buscar_por_nombre_recursivo(nodo.derecha, nombre)

# Crear árbol por nombre para realizar búsqueda por nombre
arbol_por_nombre = ArbolPokemon("nombre")

# Insertar Pokémon en el árbol
for pokemon in pokemons:
    arbol_por_nombre.insertar(pokemon)

#---------------------

# Buscar datos de Jolteon, Lycanroc y Tyrantrum
nombres_a_buscar = ["Jolteon", "Lycanroc", "Tyrantrum"]
resultados = arbol_por_nombre.buscar_por_nombres(nombres_a_buscar)

print("Datos de los Pokémon especificados:")
for pokemon in resultados:
    print(pokemon)

#---------------------

#1)F)
class NodoPokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.izquierda = None
        self.derecha = None

class ArbolPokemon:
    def __init__(self, indice):
        self.raiz = None
        self.indice = indice  # Indica el campo por el que se ordena el árbol

    def insertar(self, pokemon):
        if self.raiz is None:
            self.raiz = NodoPokemon(pokemon)
        else:
            self._insertar_recursivo(self.raiz, pokemon)

    def _insertar_recursivo(self, nodo, pokemon):
        valor_pokemon = pokemon[self.indice] if self.indice != "tipos" else pokemon["tipos"][0]
        valor_nodo = nodo.pokemon[self.indice] if self.indice != "tipos" else nodo.pokemon["tipos"][0]

        if valor_pokemon < valor_nodo:
            if nodo.izquierda is None:
                nodo.izquierda = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.izquierda, pokemon)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoPokemon(pokemon)
            else:
                self._insertar_recursivo(nodo.derecha, pokemon)
                
    def contar_por_tipo(self, tipo):
        """Cuenta cuántos Pokémon tienen el tipo especificado."""
        return self._contar_por_tipo_recursivo(self.raiz, tipo.capitalize())

    def _contar_por_tipo_recursivo(self, nodo, tipo):
        if nodo is None:
            return 0
        # Verificar si el tipo está en la lista de tipos del Pokémon
        count = 1 if tipo in nodo.pokemon["tipos"] else 0
        # Sumar recursivamente los conteos en los subárboles
        count += self._contar_por_tipo_recursivo(nodo.izquierda, tipo)
        count += self._contar_por_tipo_recursivo(nodo.derecha, tipo)
        return count
    
# Crear árbol por tipos para realizar búsqueda por tipo
arbol_por_tipo = ArbolPokemon("tipos")

# Insertar Pokémon en el árbol
for pokemon in pokemons:
    arbol_por_tipo.insertar(pokemon)

#---------------------

# Contar Pokémon de tipo Eléctrico y Acero
conteo_electrico = arbol_por_tipo.contar_por_tipo("Eléctrico")
conteo_acero = arbol_por_tipo.contar_por_tipo("Acero")

print(f"Número de Pokémon de tipo Eléctrico: {conteo_electrico}")
print(f"Número de Pokémon de tipo Acero: {conteo_acero}")

#---------------------