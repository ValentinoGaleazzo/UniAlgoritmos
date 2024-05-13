def usar_la_fuerza(mochila, indice=0, objetos_sacados=0):
    # Caso base: si hemos revisado todos los objetos de la mochila
    if indice == len(mochila):
        print("No se encontró un sable de luz en la mochila.")
        return False, objetos_sacados
    
    # Verificar si el objeto actual es un sable de luz
    if mochila[indice] == "sable de luz":
        print(f"¡Se encontró un sable de luz en la posición {indice + 1} de la mochila!")
        return True, objetos_sacados + 1
    
    # Si no es un sable de luz, seguir revisando los objetos restantes
    print(f"Sacando objeto en la posición {indice + 1} de la mochila...")
    
    # Llamada recursiva para revisar el siguiente objeto
    encontrado, objetos_sacados = usar_la_fuerza(mochila, indice + 1, objetos_sacados + 1)
    return encontrado, objetos_sacados