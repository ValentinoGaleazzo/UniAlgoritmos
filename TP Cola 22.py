class PersonajeMCU:
    def __init__(self, nombre, superheroe, genero):
        self.nombre = nombre
        self.superheroe = superheroe
        self.genero = genero

    def __str__(self):
        return f"{self.nombre} ({self.superheroe}) - {self.genero}"

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

    def obtener_elementos(self):
        return [item for item in self.items]

    def vaciar(self):
        self.items = []

# Función para encontrar el nombre del personaje de un superhéroe específico
def obtener_personaje_por_superheroe(cola, superheroe):
    for personaje in cola.obtener_elementos():
        if personaje.superheroe == superheroe:
            return personaje.nombre
    return None

# Función para mostrar nombres de los superhéroes femeninos
def mostrar_superheroes_femeninos(cola):
    return [personaje.superheroe for personaje in cola.obtener_elementos() if personaje.genero == 'F']

# Función para mostrar nombres de los personajes masculinos
def mostrar_personajes_masculinos(cola):
    return [personaje.nombre for personaje in cola.obtener_elementos() if personaje.genero == 'M']

# Función para encontrar el superhéroe de un personaje específico
def obtener_superheroe_por_personaje(cola, nombre_personaje):
    for personaje in cola.obtener_elementos():
        if personaje.nombre == nombre_personaje:
            return personaje.superheroe
    return None

# Función para mostrar todos los datos de personajes o superhéroes que comienzan con una letra específica
def mostrar_datos_por_inicial(cola, inicial):
    return [str(personaje) for personaje in cola.obtener_elementos() if personaje.nombre.startswith(inicial) or personaje.superheroe.startswith(inicial)]

# Función para verificar si un personaje está en la cola y obtener su superhéroe si existe
def verificar_personaje(cola, nombre_personaje):
    for personaje in cola.obtener_elementos():
        if personaje.nombre == nombre_personaje:
            return personaje.superheroe
    return None

# Crear la cola de personajes MCU y cargar datos de ejemplo
cola_personajes_mcu = Cola()
cola_personajes_mcu.encolar(PersonajeMCU("Tony Stark", "Iron Man", "M"))
cola_personajes_mcu.encolar(PersonajeMCU("Steve Rogers", "Capitán América", "M"))
cola_personajes_mcu.encolar(PersonajeMCU("Natasha Romanoff", "Black Widow", "F"))
cola_personajes_mcu.encolar(PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"))
cola_personajes_mcu.encolar(PersonajeMCU("Scott Lang", "Ant-Man", "M"))
cola_personajes_mcu.encolar(PersonajeMCU("Wanda Maximoff", "Scarlet Witch", "F"))

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
print("a. Personaje de Capitana Marvel:", obtener_personaje_por_superheroe(cola_personajes_mcu, "Capitana Marvel"))

# b. Mostrar los nombres de los superhéroes femeninos
print("\nb. Superhéroes femeninos:", mostrar_superheroes_femeninos(cola_personajes_mcu))

# c. Mostrar los nombres de los personajes masculinos
print("\nc. Personajes masculinos:", mostrar_personajes_masculinos(cola_personajes_mcu))

# d. Determinar el nombre del superhéroe del personaje Scott Lang
print("\nd. Superhéroe de Scott Lang:", obtener_superheroe_por_personaje(cola_personajes_mcu, "Scott Lang"))

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
print("\ne. Personajes o superhéroes con inicial 'S':", mostrar_datos_por_inicial(cola_personajes_mcu, "S"))

# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
superheroe_carol = verificar_personaje(cola_personajes_mcu, "Carol Danvers")
if superheroe_carol:
    print("\nf. Carol Danvers está en la cola y su superhéroe es:", superheroe_carol)
else:
    print("\nf. Carol Danvers no está en la cola")