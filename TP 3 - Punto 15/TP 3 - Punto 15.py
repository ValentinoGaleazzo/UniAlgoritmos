from Lista_Entrenadores import entrenadores

# A
def cantidad_pokemones(entrenador):
    for ent in entrenadores:
        if ent['nombre'] == entrenador:
            return len(ent['equipo'])
    return 0 

# Ej.
cantidad_ash = cantidad_pokemones("Ash Ketchum")
print(f"Ash Ketchum tiene {cantidad_ash} Pokémon(s).")

# B
entrenadores_mas_de_tres_torneos = [ent['nombre'] for ent in entrenadores if ent['torneos_ganados'] > 3]
print("Entrenadores que han ganado más de tres torneos:", entrenadores_mas_de_tres_torneos)

# C
max_torneos_ganados = max(entrenadores, key=lambda x: x['torneos_ganados'])
equipo_max_torneos = max_torneos_ganados['equipo']

pokemon_mayor_nivel = max(equipo_max_torneos, key=lambda x: x['nivel'])

print(f"El entrenador con más torneos ganados es {max_torneos_ganados['nombre']} y su Pokémon de mayor nivel es {pokemon_mayor_nivel['nombre']} (nivel {pokemon_mayor_nivel['nivel']}).")

# D
def mostrar_datos_entrenador(nombre):
    for ent in entrenadores:
        if ent['nombre'] == nombre:
            print("Datos del entrenador:")
            for key, value in ent.items():
                if key != 'equipo':
                    print(f"{key}: {value}")
            print("\nEquipo Pokémon:")
            for pokemon in ent['equipo']:
                print("Nombre:", pokemon['nombre'])
                print("Nivel:", pokemon['nivel'])
                print("Tipo:", pokemon['tipo'])
                print("Subtipo:", pokemon['subtipo'])
                print() 

# Ej.
mostrar_datos_entrenador("Leon")

# E
def porcentaje_batallas_ganadas(entrenador):
    for ent in entrenadores:
        if ent['nombre'] == entrenador:
            batallas_ganadas = ent['batallas_ganadas']
            batallas_perdidas = ent['batallas_perdidas']
            total_batallas = batallas_ganadas + batallas_perdidas
            porcentaje_ganadas = (batallas_ganadas / total_batallas) * 100
            return porcentaje_ganadas

# Ej.
entrenadores_altos_porcentaje = [ent['nombre'] for ent in entrenadores if porcentaje_batallas_ganadas(ent['nombre']) > 79]
print("Entrenadores con porcentaje de batallas ganadas mayor al 79%:", entrenadores_altos_porcentaje)

# F
def tiene_tipos_especificos(entrenador):
    tipos_especificos = ["Fuego", "Planta", "Agua", "Volador"]
    for pokemon in entrenador['equipo']:
        if pokemon['tipo'] in tipos_especificos or pokemon['subtipo'] in tipos_especificos:
            return True
    return False

entrenadores_tipos_especificos = [ent['nombre'] for ent in entrenadores if tiene_tipos_especificos(ent)]
print("Entrenadores con Pokémon de tipo fuego y planta o agua/volador:", entrenadores_tipos_especificos)

# G
def promedio_nivel(entrenador):
    for ent in entrenadores:
        if ent['nombre'] == entrenador:
            equipo = ent['equipo']
            if len(equipo) == 0:
                return 0 
            suma_niveles = sum(pokemon['nivel'] for pokemon in equipo)
            return suma_niveles / len(equipo)

# Ej.
promedio_ash = promedio_nivel("Ash Ketchum")
print(f"El promedio de nivel de los Pokémon de Ash Ketchum es {promedio_ash:.2f}")

# H
def cuantos_entrenadores_tienen_pokemon(nombre_pokemon):
    count = 0
    for ent in entrenadores:
        for pokemon in ent['equipo']:
            if pokemon['nombre'] == nombre_pokemon:
                count += 1
                break  
    return count

# Ej.
cantidad_charizard = cuantos_entrenadores_tienen_pokemon("Charizard")
print(f"Charizard es poseído por {cantidad_charizard} entrenador(es).")

# I
def tiene_pokemones_repetidos(entrenador):
    nombres_pokemon = []
    for pokemon in entrenador['equipo']:
        nombre = pokemon['nombre']
        if nombre in nombres_pokemon:
            return True
        nombres_pokemon.append(nombre)
    return False

entrenadores_con_pokemones_repetidos = [ent['nombre'] for ent in entrenadores if tiene_pokemones_repetidos(ent)]
print("Entrenadores que tienen Pokémon repetidos:", entrenadores_con_pokemones_repetidos)

# J
def tiene_pokemon_especifico(entrenador, pokemon_buscado):
    for pokemon in entrenador['equipo']:
        if pokemon['nombre'] == pokemon_buscado:
            return True
    return False

pokemones_buscados = ["Tyrantrum", "Terrakion", "Wingull"]
entrenadores_con_pokemon_especifico = []

for ent in entrenadores:
    for pokemon in pokemones_buscados:
        if tiene_pokemon_especifico(ent, pokemon):
            entrenadores_con_pokemon_especifico.append(ent['nombre'])
            break 

entrenadores_con_pokemon_especifico = list(set(entrenadores_con_pokemon_especifico)) 
print("Entrenadores que tienen al menos uno de Tyrantrum, Terrakion o Wingull:", entrenadores_con_pokemon_especifico)

# K
def entrenador_tiene_pokemon(nombre_entrenador, nombre_pokemon):
    for ent in entrenadores:
        if ent['nombre'] == nombre_entrenador:
            for pokemon in ent['equipo']:
                if pokemon['nombre'] == nombre_pokemon:
                    return True, ent, pokemon
            break  

    return False, None, None

# Ej.
entrenador = "Ash Ketchum"
pokemon = "Pikachu"

tiene_pokemon, datos_entrenador, datos_pokemon = entrenador_tiene_pokemon(entrenador, pokemon)

if tiene_pokemon:
    print(f"{datos_entrenador['nombre']} tiene a {datos_pokemon['nombre']} en su equipo:")
    print("Datos del entrenador:")
    for key, value in datos_entrenador.items():
        if key != 'equipo':
            print(f"{key}: {value}")
    print("\nDatos del Pokémon:")
    for key, value in datos_pokemon.items():
        print(f"{key}: {value}")
else:
    print(f"{entrenador} no tiene a {pokemon} en su equipo.")
    