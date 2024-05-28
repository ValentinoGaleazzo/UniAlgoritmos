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


def interseccion_pilas(pila1, pila2):
    interseccion = Pila()
    aux = Pila()

    while not pila1.esta_vacia():
        aux.apilar(pila1.desapilar())

    while not aux.esta_vacia():
        elemento = aux.desapilar()
        if elemento in pila2.items:
            interseccion.apilar(elemento)

    return interseccion

pila_episodio_v = Pila()
pila_episodio_v.apilar("Luke Skywalker")
pila_episodio_v.apilar("Han Solo")
pila_episodio_v.apilar("Leia Organa")
pila_episodio_v.apilar("Darth Vader")
pila_episodio_v.apilar("Lando Calrissian")

pila_episodio_vii = Pila()
pila_episodio_vii.apilar("Rey")
pila_episodio_vii.apilar("Finn")
pila_episodio_vii.apilar("Kylo Ren")
pila_episodio_vii.apilar("Leia Organa")
pila_episodio_vii.apilar("Luke Skywalker")

interseccion = interseccion_pilas(pila_episodio_v, pila_episodio_vii)

print("Personajes en la intersección de los episodios V y VII:")
while not interseccion.esta_vacia():
    print(interseccion.desapilar())