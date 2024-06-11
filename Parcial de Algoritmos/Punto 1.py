def lista_inversa(lista):
    if not lista: 
        return []
    else:
        return lista_inversa(lista[1:]) + [lista[0]]
    
# Ej:
listita = [1, 2, 3, 4, 5]
print("Lista og", listita, lista_inversa(listita), "y esta es la lista invertida.")