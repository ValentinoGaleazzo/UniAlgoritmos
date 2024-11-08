class Personaje:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __str__(self):
        return f"{self.nombre} - {self.planeta}"

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, personaje):
        self.items.append(personaje)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise Exception("La cola está vacía")

    def esta_vacia(self):
        return len(self.items) == 0

    def tamaño(self):
        return len(self.items)

    def frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            raise Exception("La cola está vacía")

    def mostrar(self):
        for item in self.items:
            print(item)

    def obtener_elementos(self):
        return [item for item in self.items]

    def vaciar(self):
        self.items = []

# Función para mostrar personajes de Alderaan, Endor y Tatooine
def mostrar_personajes_por_planetas(cola, planetas):
    personajes_planetas = []
    for personaje in cola.obtener_elementos():
        if personaje.planeta in planetas:
            personajes_planetas.append(str(personaje))
    return personajes_planetas

# Función para indicar el planeta natal de personajes específicos
def indicar_planeta_personajes(cola, nombres):
    planetas_personajes = {}
    for personaje in cola.obtener_elementos():
        if personaje.nombre in nombres:
            planetas_personajes[personaje.nombre] = personaje.planeta
    return planetas_personajes

# Función para insertar un personaje antes de otro específico
def insertar_antes_de(cola, nuevo_personaje, nombre_objetivo):
    cola_aux = Cola()
    insertado = False
    while not cola.esta_vacia():
        personaje_actual = cola.desencolar()
        if personaje_actual.nombre == nombre_objetivo and not insertado:
            cola_aux.encolar(nuevo_personaje)
            insertado = True
        cola_aux.encolar(personaje_actual)
    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

# Función para eliminar el personaje después de uno específico
def eliminar_despues_de(cola, nombre_objetivo):
    cola_aux = Cola()
    encontrado = False
    while not cola.esta_vacia():
        personaje_actual = cola.desencolar()
        cola_aux.encolar(personaje_actual)
        if encontrado:
            cola_aux.desencolar()  # Elimina el siguiente personaje
            encontrado = False
        if personaje_actual.nombre == nombre_objetivo:
            encontrado = True
    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

# Crear cola de personajes y cargar datos de ejemplo
cola_personajes = Cola()
cola_personajes.encolar(Personaje("Luke Skywalker", "Tatooine"))
cola_personajes.encolar(Personaje("Leia Organa", "Alderaan"))
cola_personajes.encolar(Personaje("Han Solo", "Corellia"))
cola_personajes.encolar(Personaje("Yoda", "Dagobah"))
cola_personajes.encolar(Personaje("Chewbacca", "Kashyyyk"))
cola_personajes.encolar(Personaje("Jar Jar Binks", "Naboo"))

# a. Mostrar personajes de Alderaan, Endor y Tatooine
print("Personajes de Alderaan, Endor y Tatooine:")
print(mostrar_personajes_por_planetas(cola_personajes, ["Alderaan", "Endor", "Tatooine"]))

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
print("\nPlaneta natal de Luke Skywalker y Han Solo:")
print(indicar_planeta_personajes(cola_personajes, ["Luke Skywalker", "Han Solo"]))

# c. Insertar un nuevo personaje antes del maestro Yoda
nuevo_personaje = Personaje("Obi-Wan Kenobi", "Stewjon")
insertar_antes_de(cola_personajes, nuevo_personaje, "Yoda")
print("\nCola de personajes después de insertar a Obi-Wan antes de Yoda:")
cola_personajes.mostrar()

# d. Eliminar el personaje ubicado después de Jar Jar Binks
eliminar_despues_de(cola_personajes, "Jar Jar Binks")
print("\nCola de personajes después de eliminar el personaje después de Jar Jar Binks:")
cola_personajes.mostrar()