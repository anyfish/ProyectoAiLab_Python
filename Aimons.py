from venv.GAME.Constantes import *

class Aimon:
    def __init__(aimon, nombre, hp, tipo, ventajas, desventajas, normal, ataque1, ataque2, ataque3, potenciador):
        aimon.nombre = nombre
        aimon.hp = hp
        aimon.tipo = tipo
        aimon.ventajas = ventajas
        aimon.desventajas = desventajas
        aimon.normal = normal
        aimon.ataque1 = ataque1
        aimon.ataque2 = ataque2
        aimon.ataque3 = ataque3
        aimon.potenciador = potenciador

aquarder = Aimon(AQUARDER, 25, AGUA, [ROCA, FUEGO], [ELECTRICO, PLANTA],
                 [AGUA, ESCARABAJO], [AQUAJET, 3], [COLAFERREA, 2],
                 [CABEZAZO, 2], [LLUVIA])

firesor = Aimon(FIRESOR, 25, FUEGO, [PLANTA, ESCARABAJO], [AGUA, ROCA],
                [ELECTRICO, FUEGO], [LLAMARADA, 3], [EMBESTIDA, 2],
                [MORDISCO, 2], [DIASOLEADO])

electder = Aimon(ELECTDER, 25, ELECTRICO, [AGUA, ESCARABAJO], [ROCA, PLANTA],
                [ELECTRICO, FUEGO], [TRUENO, 3], [ARANAZO, 3],
                [MORDISCO, 3], [CAMPOMAGNETICO])

mousebug = Aimon(MOUSEBUG, 25, ESCARABAJO, [PLANTA, ROCA], [FUEGO, ELECTRICO],
                [ESCARABAJO, AGUA], [PICOTAZO, 3], [EMBESTIDA, 2],
                [CABEZAZO, 2], [ESPORAS])

splat = Aimon(SPLAT, 25, PLANTA, [ROCA, AGUA, ELECTRICO], [FUEGO, ESCARABAJO],
                [PLANTA], [HOJANAVAJA, 3], [MORDISCO, 2],
                [CABEZAZO, 2], [RAYOSOLAR])

rockdog = Aimon(ROCKDOG, 25, ROCA, [FUEGO, ELECTRICO], [AGUA, PLANTA],
                [ROCA, ESCARABAJO], [ROCAAFILADA, 3], [VELOCIDAD, 2],
                [COLAFERREA, 2], [RAYOSOLAR])

def detallesAquader():
    print(f"""
    {aquarder.nombre}: Tipo {aquarder.tipo}
    Ventajas con: {aquarder.ventajas[0]}, {aquarder.ventajas[1]}
    Desventajas con: {aquarder.desventajas[0]}, {aquarder.ventajas[1]}
    Normal con: {aquarder.normal[0]}, {aquarder.ventajas[1]}""")
    print(f"""
    Habilidad   | Norm | At vent | At desv | Pot norm | Pot vent | Pot desv |
    {aquarder.ataque1[0]}    | 3 pt |   5 pt  |   2 pt  |   5 pt   |   7 pt   |   4 pt   |
    {aquarder.ataque2[0]} | 2 pt |
    {aquarder.ataque3[0]}    | 2 pt |
    {aquarder.potenciador[0]}      | Potenciador de campo, 1 vez cada 3 turnos. Dura 2 turnos.
    """)

def detallesFiresor():
    print(f"""
    {firesor.nombre}: Tipo {firesor.tipo}
    Ventajas con: {firesor.ventajas[0]}, {firesor.ventajas[1]}
    Desventajas con: {firesor.desventajas[0]}, {firesor.ventajas[1]}
    Normal con: {firesor.normal[0]}, {firesor.ventajas[1]}""")
    print(f"""
    Habilidad   | Norm | At vent | At desv | Pot norm | Pot vent | Pot desv |
    {firesor.ataque1[0]}   | 3 pt |   5 pt  |   2 pt  |   5 pt   |   7 pt   |   4 pt   |
    {firesor.ataque2[0]}   | 2 pt |
    {firesor.ataque3[0]}    | 2 pt |
    {firesor.potenciador[0]} | Potenciador de campo, 1 vez cada 3 turnos. Dura 2 turnos.
    """)

def detallesElectder():
    print(f"""
    {electder.nombre}: Tipo {electder.tipo}
    Ventajas con: {electder.ventajas[0]}, {electder.ventajas[1]}
    Desventajas con: {electder.desventajas[0]}, {electder.ventajas[1]}
    Normal con: {electder.normal[0]}, {electder.ventajas[1]}""")
    print(f"""
    Habilidad | Norm | At vent | At desv | Pot norm | Pot vent | Pot desv |
    {electder.ataque1[0]}    | 3 pt |   5 pt  |   2 pt  |   5 pt   |   7 pt   |   4 pt   |
    {electder.ataque2[0]}   | 3 pt |
    {electder.ataque3[0]}  | 3 pt |
    {electder.potenciador[0]} | Potenciador de campo, 1 vez cada 3 turnos. Dura 2 turnos.
    """)

def detallesMousebug():
    print(f"""
    {mousebug.nombre}: Tipo {mousebug.tipo}
    Ventajas con: {mousebug.ventajas[0]}, {mousebug.ventajas[1]}
    Desventajas con: {mousebug.desventajas[0]}, {mousebug.ventajas[1]}
    Normal con: {mousebug.normal[0]}, {mousebug.ventajas[1]}""")
    print(f"""
    Habilidad | Norm | At vent | At desv | Pot norm | Pot vent | Pot desv |
    {mousebug.ataque1[0]}  | 3 pt |   5 pt  |   2 pt  |   5 pt   |   7 pt   |   4 pt   |
    {mousebug.ataque2[0]} | 2 pt |
    {mousebug.ataque3[0]}  | 2 pt |
    {mousebug.potenciador[0]}   | Potenciador de campo, 1 vez cada 3 turnos. Dura 2 turnos.
    """)

def detallesSplat():
    print(f"""
    {splat.nombre}: Tipo {splat.tipo}
    Ventajas con: {splat.ventajas[0]}, {splat.ventajas[1]}
    Desventajas con: {splat.desventajas[0]}, {splat.ventajas[1]}
    Normal con: {splat.normal[0]}, {splat.ventajas[1]}""")
    print(f"""
    Habilidad   | Norm | At vent | At desv | Pot norm | Pot vent | Pot desv |
    {splat.ataque1[0]} | 3 pt |   5 pt  |   2 pt  |   5 pt   |   7 pt   |   4 pt   |
    {splat.ataque2[0]}    | 2 pt |
    {splat.ataque3[0]}    | 2 pt |
    {splat.potenciador[0]}  | Potenciador de campo, 1 vez cada 3 turnos. Dura 2 turnos.
    """)

def detallesRockdog():
    print(f"""
    {rockdog.nombre}: Tipo {rockdog.tipo}
    Ventajas con: {rockdog.ventajas[0]}, {rockdog.ventajas[1]}
    Desventajas con: {rockdog.desventajas[0]}, {rockdog.ventajas[1]}
    Normal con: {rockdog.normal[0]}, {rockdog.ventajas[1]}""")
    print(f"""
    Habilidad    | Norm | At vent | At desv | Pot norm | Pot vent | Pot desv |
    {rockdog.ataque1[0]} | 3 pt |   5 pt  |   2 pt  |   5 pt   |   7 pt   |   4 pt   |
    {rockdog.ataque2[0]}    | 2 pt |
    {rockdog.ataque3[0]}  | 2 pt |
    {rockdog.potenciador[0]}   | Potenciador de campo, 1 vez cada 3 turnos. Dura 2 turnos.
    """)