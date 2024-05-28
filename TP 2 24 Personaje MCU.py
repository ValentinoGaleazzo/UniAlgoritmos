class PersonajeMCU:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas


class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]


def posicion_rocket_y_groot(pila):
    posicion = 0
    aux = Pila()

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje.nombre == "Rocket Raccoon" or personaje.nombre == "Groot":
            return posicion + 1
        aux.apilar(personaje)
        posicion += 1

    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())


def personajes_mas_de_5_peliculas(pila):
    personajes = []
    aux = Pila()

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje.peliculas > 5:
            personajes.append((personaje.nombre, personaje.peliculas))
        aux.apilar(personaje)

    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

    return personajes


def peliculas_black_widow(pila):
    peliculas = 0
    aux = Pila()

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje.nombre == "Viuda Negra":
            peliculas = personaje.peliculas
            break
        aux.apilar(personaje)

    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

    return peliculas


def personajes_con_iniciales(pila, iniciales):
    personajes = []

    for personaje in pila.items:
        if personaje.nombre[0] in iniciales:
            personajes.append(personaje.nombre)

    return personajes


pila_mcu = Pila()
pila_mcu.apilar(PersonajeMCU("Iron Man", 6))
pila_mcu.apilar(PersonajeMCU("Viuda Negra", 7))
pila_mcu.apilar(PersonajeMCU("Thor", 7))
pila_mcu.apilar(PersonajeMCU("Rocket Raccoon", 5))
pila_mcu.apilar(PersonajeMCU("Groot", 4))
pila_mcu.apilar(PersonajeMCU("Capitán América", 6))
pila_mcu.apilar(PersonajeMCU("Doctor Strange", 3))
pila_mcu.apilar(PersonajeMCU("Hulk", 4))
pila_mcu.apilar(PersonajeMCU("Black Panther", 4))

# A
print("Posición de Rocket Raccoon y Groot en las pilas:", posicion_rocket_y_groot(pila_mcu))

# B
print("Personajes en más de 5 peliculas:")
print(personajes_mas_de_5_peliculas(pila_mcu))

# C
print("Peliculas en las que aparece Black Widow:", peliculas_black_widow(pila_mcu))

# D
print("Personajes con nombres que empiezan con C, D y G:")
print(personajes_con_iniciales(pila_mcu, ['C', 'D', 'G']))