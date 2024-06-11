from jedi import jedis

# Punto A

jedis_ordenados_por_nombre = sorted(jedis, key=lambda x: x['name'])

def custom_sort(jedi):
    species = jedi.get('species')
    if species is None:
        return 'zzz'
    return species

jedis_ordenados_por_especie = sorted(jedis, key=custom_sort)


print("Listado ordenado por nombre:")
for jedi in jedis_ordenados_por_nombre:
    print(jedi['name'], "-", jedi['species'])

print("\nListado ordenado por especie:")
for jedi in jedis_ordenados_por_especie:
    print(jedi['name'], "-", jedi['species'])

# Punto B

for jedi in jedis:
    if jedi['name'] == 'Ahsoka Tano' or jedi['name'] == 'Kit Fisto':
        print("\nInformación de", jedi['name'] + ":")
        for key, value in jedi.items():
            print(key.capitalize() + ":", value)

# Punto C

padawan_de_yoda = []
padawan_de_luke = []

for jedi in jedis:
    if jedi['master'] == 'Yoda':
        padawan_de_yoda.append(jedi['name'])
    elif jedi['master'] == 'Luke Skywalker':
        padawan_de_luke.append(jedi['name'])

print("Padawan de Yoda:")
for padawan in padawan_de_yoda:
    print(padawan)

print("\nPadawan de Luke Skywalker:")
for padawan in padawan_de_luke:
    print(padawan)

# Punto D

jedi_humanos = []
jedi_twi_lek = []

for jedi in jedis:
    if jedi['species'] == 'Human':
        jedi_humanos.append(jedi)
    elif jedi['species'] == "Twi'lek":
        jedi_twi_lek.append(jedi)

print("Jedi de especie humana:")
for jedi in jedi_humanos:
    print(jedi['name'])

print("\nJedi de especie Twi'lek:")
for jedi in jedi_twi_lek:
    print(jedi['name'])

# Punto E

jedi_con_A = []

for jedi in jedis:
    if jedi['name'].startswith('A'):
        jedi_con_A.append(jedi['name'])

print("Jedi cuyos nombres comienzan con A:")
for jedi in jedi_con_A:
    print(jedi)

# Punto F

jedi_multicolores = []

for jedi in jedis:
    lightsaber_color = jedi['lightsaber_color']
    if lightsaber_color is not None:
        colores_sable = lightsaber_color.split('/')
        if len(colores_sable) > 1:
            jedi_multicolores.append(jedi['name'])

print("Jedi que han usado sables de luz de más de un color:")
for jedi in jedi_multicolores:
    print(jedi)

#Punto G

jedi_amarillo_violeta = []

for jedi in jedis:
    lightsaber_color = jedi['lightsaber_color']
    if lightsaber_color is not None and ('Yellow' in lightsaber_color or 'Purple' in lightsaber_color):
        jedi_amarillo_violeta.append(jedi['name'])


print("Jedi que utilizaron sable de luz amarillo o violeta:")
for jedi in jedi_amarillo_violeta:
    print(jedi)

# Punto H

padawans_quigon = []
padawans_windu = []

for jedi in jedis:
    if jedi["master"] == "Qui-Gon Jinn" and jedi["rank"] == "Padawan":
        padawans_quigon.append(jedi["name"])
    elif jedi["master"] == "Mace Windu" and jedi["rank"] == "Padawan":
        padawans_windu.append(jedi["name"])

print("Padawans de Qui-Gon Jinn:")
if padawans_quigon:
    print(padawans_quigon)
else:
    print("Qui-Gon Jinn no tiene padawans.")

print("Padawans de Mace Windu:")
if padawans_windu:
    print(padawans_windu)
else:
    print("Mace Windu no tiene padawans.")

#Punto I

grand_masters = []

for jedi in jedis:
    if jedi['rank'] == 'Grand Master':
        grand_masters.append(jedi['name'])

print("Jedi con el rango de Grand Master:")
for jedi in grand_masters:
    print(jedi)