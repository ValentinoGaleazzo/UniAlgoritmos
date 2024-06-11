from dino import dinosaurios
import hashlib

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items.peek()

def contar_especies(dinosaurios): #Punto A
    especies = Stack()
    especies_vistas = set() 
    for dinosaurio in dinosaurios:
        especie = dinosaurio["especie"]
        if especie not in especies_vistas:
            especies_vistas.add(especie)
            especies.push(especie)
    return len(especies.items)

num_especies = contar_especies(dinosaurios)
print("Cantidad de especies de dinosaurios:", num_especies)

def contar_descubridores(dinosaurios): #Punto B
    descubridores = Stack()
    descubridores_vistos = set()
    for dinosaurio in dinosaurios:
        descubridor = dinosaurio["descubridor"]
        if descubridor not in descubridores_vistos:
            descubridores_vistos.add(descubridor)
            descubridores.push(descubridor)
    return len(descubridores.items)

num_descubridores = contar_descubridores(dinosaurios)
print("Cantidad de descubridores de dinosaurios:", num_descubridores)

def dinosaurios_con_T(dinosaurios): #Punto C
    dinosaurios_con_t = Stack()
    for dinosaurio in dinosaurios:
        nombre = dinosaurio["nombre"]
        if nombre.startswith("T"):
            dinosaurios_con_t.push(dinosaurio)
    
    while not dinosaurios_con_t.is_empty():
        print(dinosaurios_con_t.pop())

print("Dinosaurios cuyos nombres empiezan con T:")
dinosaurios_con_T(dinosaurios)

def dinosaurios_livianos(dinosaurios): #Punto D
    dinosaurios_livianos = Stack()
    for dinosaurio in dinosaurios:
        peso = int(dinosaurio["peso"].split()[0])
        if peso < 275:
            dinosaurios_livianos.push(dinosaurio)
        
    while not dinosaurios_livianos.is_empty():
        print(dinosaurios_livianos.pop())

print("Dinosaurios que pesan menos de 275 kg:")
dinosaurios_livianos(dinosaurios)

def dinosaurios_letras_especificas(dinosaurios): #Punto E
    dinosaurios_especificos = Stack()
    for dinosaurio in dinosaurios:
        nombre = dinosaurio["nombre"]
        if nombre.startswith(("A", "Q", "S")):
            print(dinosaurio) 
            dinosaurios_especificos.push(dinosaurio)
    
    return dinosaurios_especificos

print("Dinosaurios cuyos nombres empiezan con A, Q o S:")
pila_dinosaurios_letras_especificas = dinosaurios_letras_especificas(dinosaurios)

