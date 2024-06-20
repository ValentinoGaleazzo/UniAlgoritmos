"TP3 Punto 6"

superheroes = {
    "Spider-Man": {
        "nombre": "Spider-Man",
        "anio_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "Peter Parker obtiene sus poderes tras ser picado por una araña radiactiva."
    },
    "Batman": {
        "nombre": "Batman",
        "anio_aparicion": 1939,
        "casa_comic": "DC",
        "biografia": "Bruce Wayne, tras presenciar el asesinato de sus padres, se convierte en Batman."
    },
    "Superman": {
        "nombre": "Superman",
        "anio_aparicion": 1938,
        "casa_comic": "DC",
        "biografia": "Kal-El es enviado a la Tierra desde el planeta Krypton y se convierte en Superman."
    },
    "Linterna Verde": {
        "nombre": "Linterna Verde",
        "anio_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Hal Jordan es elegido por un anillo de poder para ser Linterna Verde."
    },
    "Wolverine": {
        "nombre": "Wolverine",
        "anio_aparicion": 1974,
        "casa_comic": "Marvel",
        "biografia": "Logan, conocido como Wolverine, es un mutante con garras retractiles y factor curativo."
    },
    "Dr. Strange": {
        "nombre": "Dr. Strange",
        "anio_aparicion": 1963,
        "casa_comic": "DC",
        "biografia": "Stephen Strange se convierte en el Hechicero Supremo tras un accidente que daña sus manos."
    },
    "Capitana Marvel": {
        "nombre": "Capitana Marvel",
        "anio_aparicion": 1968,
        "casa_comic": "Marvel",
        "biografia": "Carol Danvers obtiene poderes cósmicos y se convierte en Capitana Marvel."
    },
    "Mujer Maravilla": {
        "nombre": "Mujer Maravilla",
        "anio_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Diana Prince es una princesa amazona con habilidades y armas místicas."
    },
    "Flash": {
        "nombre": "Flash",
        "anio_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Barry Allen obtiene velocidad sobrehumana tras un accidente con químicos y un rayo."
    },
    "Star-Lord": {
        "nombre": "Star-Lord",
        "anio_aparicion": 1976,
        "casa_comic": "Marvel",
        "biografia": "Peter Quill se convierte en Star-Lord tras ser abducido por alienígenas."
    }
}

# A
if "Linterna Verde" in superheroes:
    del superheroes["Linterna Verde"]

# B
print(f"Año de aparición de Wolverine: {superheroes['Wolverine']['anio_aparicion']}")

# C
superheroes["Dr. Strange"]["casa_comic"] = "Marvel"

# D
print("Superhéroes con 'traje' o 'armadura' en su biografía:")
for nombre, info in superheroes.items():
    if 'traje' in info['biografia'].lower() or 'armadura' in info['biografia'].lower():
        print(f"- {info['nombre']}")

# E
print("Superhéroes cuya fecha de aparición es anterior a 1963:")
for nombre, info in superheroes.items():
    if info['anio_aparicion'] < 1963:
        print(f"- {info['nombre']} ({info['casa_comic']})")

# F
for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
    print(f"{nombre} pertenece a la casa de cómics: {superheroes[nombre]['casa_comic']}")

# G
for nombre in ["Flash", "Star-Lord"]:
    print(f"Información de {nombre}:")
    for clave, valor in superheroes[nombre].items():
        print(f"- {clave}: {valor}")

# H
letras_interesantes = ['B', 'M', 'S']
print("Superhéroes que comienzan con B, M y S:")
for nombre, info in superheroes.items():
    if nombre[0] in letras_interesantes:
        print(f"- {info['nombre']}")

# I
contador_marvel = sum(1 for heroe in superheroes.values() if heroe['casa_comic'] == "Marvel")
contador_dc = sum(1 for heroe in superheroes.values() if heroe['casa_comic'] == "DC")

print(f"Número de superhéroes de Marvel: {contador_marvel}")
print(f"Número de superhéroes de DC: {contador_dc}")