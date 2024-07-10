# A.
class Pokemon:
    def __init__(self, numero, nombre, tipos, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos
        self.nivel = nivel

    def __str__(self):
        return f"{self.numero}: {self.nombre} - Tipos: {', '.join(self.tipos)} - Nivel: {self.nivel}"

# B.
class Pokedex:
    def __init__(self):
        self.hash_tipo = {}
        self.hash_ultimo_digito = {}
        self.hash_nivel = [[] for _ in range(10)]

# C.
    def hash_func_tipo(self, tipos):
        for tipo in tipos:
            if tipo not in self.hash_tipo:
                self.hash_tipo[tipo] = []
            self.hash_tipo[tipo].append(Pokemon)

    def hash_func_ultimo_digito(self, pokemon):
        ultimo_digito = pokemon.numero % 10
        if ultimo_digito not in self.hash_ultimo_digito:
            self.hash_ultimo_digito[ultimo_digito] = []
        self.hash_ultimo_digito[ultimo_digito].append(pokemon)

    def hash_func_nivel(self, pokemon):
        posicion = pokemon.nivel % 10
        self.hash_nivel[posicion].append(pokemon)

# D.
    def agregar_pokemon(self, pokemon):
        # Agregar a la tabla hash por tipo
        self.hash_func_tipo(pokemon.tipos)

        # Agregar a la tabla hash por último dígito del número
        self.hash_func_ultimo_digito(pokemon)

        # Agregar a la tabla hash por nivel
        self.hash_func_nivel(pokemon)

# E.
    def mostrar_por_ultimo_digito(self, digitos):
        for digito in digitos:
            if digito in self.hash_ultimo_digito:
                for pokemon in self.hash_ultimo_digito[digito]:
                    print(pokemon)
# F.
    def mostrar_por_nivel_multiplo(self, multiplos):
        for posicion in multiplos:
            for pokemon in self.hash_nivel[posicion]:
                print(pokemon)
# G.
    def mostrar_por_tipo(self, tipos):
        for tipo in tipos:
            if tipo in self.hash_tipo:
                for pokemon in self.hash_tipo[tipo]:
                    print(pokemon)


# Ej.
pokedex = Pokedex()

# Le damos pokes.
p1 = Pokemon(25, "Pikachu", ["Eléctrico"], 50)
p2 = Pokemon(6, "Charizard", ["Fuego", "Volador"], 75)
p3 = Pokemon(131, "Lapras", ["Agua", "Hielo"], 60)
p4 = Pokemon(149, "Dragonite", ["Dragón", "Volador"], 80)
p5 = Pokemon(212, "Scizor", ["Bicho", "Acero"], 70)

pokedex.agregar_pokemon(p1)
pokedex.agregar_pokemon(p2)
pokedex.agregar_pokemon(p3)
pokedex.agregar_pokemon(p4)
pokedex.agregar_pokemon(p5)

# E. 3, 7 y 9
print("Pokémons cuyos números terminan en 3, 7 y 9:")
pokedex.mostrar_por_ultimo_digito([3, 7, 9])

# F. Múltiplos de 2, 5 y 10
print("\nPokémons cuyos niveles son múltiplos de 2, 5 y 10:")
pokedex.mostrar_por_nivel_multiplo([0, 5])

# G. Acero, Fuego, Eléctrico, Hielo
print("\nPokémons de tipo Acero, Fuego, Eléctrico, Hielo:")
pokedex.mostrar_por_tipo(["Acero", "Fuego", "Eléctrico", "Hielo"])