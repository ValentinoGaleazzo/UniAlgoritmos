import heapq
from datetime import datetime

class Actividad:
    def __init__(self, encargado, descripcion, hora, prioridad, stormtroopers=None):
        self.encargado = encargado
        self.descripcion = descripcion
        self.hora = hora
        self.prioridad = prioridad
        self.stormtroopers = stormtroopers or 0

    # Definir la comparación para ordenar por prioridad (menor valor = mayor prioridad)
    def __lt__(self, other):
        return self.prioridad < other.prioridad

    def __str__(self):
        return f"{self.hora} - {self.encargado}: {self.descripcion} (Prioridad {self.prioridad}, Stormtroopers: {self.stormtroopers})"

class ColaDePrioridad:
    def __init__(self):
        self.items = []

    def encolar(self, actividad):
        heapq.heappush(self.items, actividad)

    def desencolar(self):
        if not self.esta_vacia():
            return heapq.heappop(self.items)
        else:
            raise Exception("La cola está vacía")

    def esta_vacia(self):
        return len(self.items) == 0

# Crear la cola de operaciones
cola_operaciones = ColaDePrioridad()

# Función para agregar actividades con niveles de prioridad específicos
def agregar_actividad(encargado, descripcion, prioridad, stormtroopers=None):
    hora_actual = datetime.now().strftime("%H:%M:%S")
    actividad = Actividad(encargado, descripcion, hora_actual, prioridad, stormtroopers)
    cola_operaciones.encolar(actividad)

# Cargar actividades iniciales
agregar_actividad("Líder Supremo Snoke", "Revisión de armamento", prioridad=3)
agregar_actividad("Kylo Ren", "Entrenamiento de la Fuerza", prioridad=3)
agregar_actividad("Capitán Phasma", "Revisión de seguridad del perímetro", prioridad=2, stormtroopers=10)
agregar_actividad("Capitán Phasma", "Inspección de Stormtroopers", prioridad=2, stormtroopers=15)
agregar_actividad("Capitán Phasma", "Reparación de barreras de seguridad", prioridad=2)
agregar_actividad("Capitán Phasma", "Análisis de fallas de sistemas", prioridad=2)
agregar_actividad("General Hux", "Informe semanal de operaciones", prioridad=1)
agregar_actividad("General Hux", "Planificación de defensa", prioridad=1)
agregar_actividad("General Hux", "Revisión de recursos", prioridad=1)
agregar_actividad("General Hux", "Entrenamiento básico de soldados", prioridad=1)

# Atender las operaciones en orden de prioridad
print("Atendiendo operaciones en orden de prioridad:\n")
contador_atenciones = 0

while not cola_operaciones.esta_vacia():
    operacion = cola_operaciones.desencolar()
    contador_atenciones += 1
    print(f"Atendiendo operación {contador_atenciones}: {operacion}")

    # Después de atender la quinta operación, agregar operación de Capitán Phasma
    if contador_atenciones == 5:
        agregar_actividad("Capitán Phasma", "Revisión de intrusos en el hangar B7", prioridad=2, stormtroopers=25)
        print("\n[Agregada nueva operación de Capitán Phasma: Revisión de intrusos en el hangar B7]\n")

    # Después de atender la sexta operación, agregar operación del Líder Supremo Snoke
    if contador_atenciones == 6:
        agregar_actividad("Líder Supremo Snoke", "Destrucción del planeta Takodana", prioridad=3)
        print("\n[Agregada nueva operación de Líder Supremo Snoke: Destrucción del planeta Takodana]\n")

print("\nTodas las operaciones han sido atendidas.")