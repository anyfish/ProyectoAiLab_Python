import csv
import random
from venv.GAME.Aimons import *

listadeUsuarios = []
contPotAimon = 0
contPotRival = 0

def inicio():
    global listadeUsuarios

    with open("bd_usuarios.csv") as bd:
        lector = csv.reader(bd, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
        for renglon in lector:
            if len(renglon) != 0:
                listadeUsuarios.append(renglon)

    while True:
        print("""
            .::AIMONS GAME::.
            1. Iniciar Sección
            2. Usuario Nuevo
            
            0. Salir
            """)

        seleccion = int(input('Elige una opción: '))

        if seleccion == 1:
            validarUsuario()
        elif seleccion == 2:
            nuevoUsuario()
        elif seleccion == 0:
            break
        else:
            print("Elije una opción correcta")

def menu():
    while True:
        print("""
            .:: Modos de Juego ::.
            1. Historia
            2. Entrenamiento
            3. AimonDex
            
            0. Salir
            """)

        eleccion = int(input("Elige opción: "))
        if eleccion == 1:
            print("Escribe tu historia ")
            modoHistoria()
        elif eleccion == 2:
            print("Entrenemos para volvermos más fuertes")
            modoEntrenamiento()
        elif eleccion == 3:
            print("Aprende sobre los Aimons")
            aimonDex()

        elif eleccion == 0:
            inicio()
        else:
            print("Elige una opcion valida")
            break

def bd():
    global listadeUsuarios

    archivo = open('bd_usuarios.csv', 'w')
    with archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(listadeUsuarios)

def validarUsuario():
    global listadeUsuarios

    nombre = input("Ingresa tu Usuario: ")
    contrasena = input("Ingresa Contraseña: ")
    usuario = [nombre, contrasena]

    if usuario in listadeUsuarios:
        for i in listadeUsuarios:
            if i != usuario:
                continue
            else:
                menu()
    else:
        print(f"\nEl usuario {usuario[0]} no existe\n")
        inicio()

def nuevoUsuario():
    global listadeUsuarios

    nombre = input("Ingresa tu Usuario: ")
    contrasena = input("Ingresa Contraseña: ")
    usuario = [nombre, contrasena]
    listadeUsuarios.append(usuario)
    print("\nUsuario creado\n")
    bd()
    inicio()

def modoHistoria():
    global aimonRival
    aimonRival = None

    elegirAimon()

    print("----------------------------------------------------------------------")
    aimonRival = aquarder
    print(f"\n.:: Round 1::. \n{aimon.nombre} vs {aimonRival.nombre}")
    modificarAtaques()
    batalla()
    ganador()
    pocima()

    print("----------------------------------------------------------------------")
    aimonRival = firesor
    print(f"\n.:: Round 2::. \n{aimon.nombre} vs {aimonRival.nombre}")
    modificarAtaques()
    batalla()
    pocima()

    print("----------------------------------------------------------------------")
    aimonRival = electder
    print(f"\n.:: Round 3::. \n{aimon.nombre} vs {aimonRival.nombre}")
    modificarAtaques()
    batalla()
    ganador()
    pocima()

    print("----------------------------------------------------------------------")
    aimonRival = mousebug
    print(f"\n.:: Round 4::. \n{aimon.nombre} vs {aimonRival.nombre}")
    modificarAtaques()
    batalla()
    ganador()
    pocima()

    print("----------------------------------------------------------------------")
    aimonRival = splat
    print(f"\n.:: Round 5::. \n{aimon.nombre} vs {aimonRival.nombre}")
    modificarAtaques()
    batalla()
    ganador()
    pocima()

    print("----------------------------------------------------------------------")
    aimonRival = rockdog
    print(f"\n.:: Round 6::. \n{aimon.nombre} vs {aimonRival.nombre}")
    modificarAtaques()
    batalla()
    ganador()

    print("""FUE UN CAMINO DIFICIL PERO COMPLETASTE EL MODO HISTORIA
        FELICIDADES!!!""")

def modoEntrenamiento():
    elegirAimon()
    elegirAimonRival()
    modificarAtaques()
    batalla()

def elegirAimon():
    global aimon
    aimon = None

    while True:
        print("""
            .:Aimons:.
            1. Aquarder
            2. Firesor
            3. Electder
            4. Mousebug
            5. Splant
            6. Rockdog
            
            0. Salir
            """)

        eleccion = int(input("Elige un Aimon: "))

        if eleccion == 1:
            aimon = aquarder
            break
        elif eleccion == 2:
            aimon = firesor
            break
        elif eleccion == 3:
            aimon = electder
            break
        elif eleccion == 4:
            aimon = mousebug
            break
        elif eleccion == 5:
            aimon = splat
            break
        elif eleccion == 6:
            aimon = rockdog
            break
        elif eleccion == 0:
            menu()
        else:
            print("Elige una opción valida")

def elegirAimonRival():
    global aimonRival
    aimonRival = None

    while True:
        print("""
            .:Aimons:.
            1. Aquarder
            2. Firesor
            3. Electder
            4. Mousebug
            5. Splant
            6. Rockdog
                 
            """)

        eleccion = int(input("Elige el Aimon rival: "))

        if eleccion == 1:
            aimonRival = aquarder
            break
        elif eleccion == 2:
            aimonRival = firesor
            break
        elif eleccion == 3:
            aimonRival = electder
            break
        elif eleccion == 4:
            aimonRival = mousebug
            break
        elif eleccion == 5:
            aimonRival = splat
            break
        elif eleccion == 6:
            aimonRival = rockdog
            break
        else:
            print("Elige una opción valida")

def modificarAtaques():
    if aimonRival.tipo in aimon.ventajas:
        aimon.ventajadeTipo = True
        aimon.ataque1[1] += 2
        print(f"> El puntaje de daño de {aimon.nombre} aumento")
        print(f"> Ahora {aimon.ataque1[0]} tiene {aimon.ataque1[1]} de daño\n")
    elif aimonRival.tipo in aimon.desventajas:
        aimon.ventajadeTipo = False
        aimon.ataque1[1] -= 1
        print(f"> El puntaje de daño {aimon.nombre} disminuyo")
        print(f"> Ahora {aimon.ataque1[0]} tiene {aimon.ataque1[1]} de daño\n")

    if aimon.tipo in aimonRival.ventajas:
        aimonRival.ventajadeTipo = True
        aimonRival.ataque1[1] += 2
        print(f"> El puntaje de daño de {aimonRival.nombre} aumento")
        print(f"> Ahora {aimonRival.ataque1[0]} tiene {aimonRival.ataque1[1]} de daño\n")
    elif aimon.tipo in aimonRival.desventajas:
        aimon.ventajadeTipo = False
        aimonRival.ataque1[1] -= 1
        print(f"> El puntaje de daño {aimonRival.nombre} disminuyo")
        print(f"> Ahora {aimonRival.ataque1[0]} tiene {aimonRival.ataque1[1]} de daño\n")

def batalla():
    print("Vamos a la batalla!!\n")

    eleccionTurno = random.randint(1, 2)
    if eleccionTurno == 1:
        print(f"El primer movimiento es tuyo\n")
        while aimon.hp > 0 and aimonRival.hp > 0:
            print(f"HP Actuales\n.: Tu: {aimon.hp} .::. CPU: {aimonRival.hp}:.\n")
            potenciador()
            turnoProtagonista()
            turnoRival()
        ganador()
    elif eleccionTurno == 2:
        print(f"El primer movimiento es de tu Rival\n")
        while aimon.hp > 0 and aimonRival.hp > 0:
            print(f"HP Actuales\n.: Tu: {aimon.hp}  .::.  CPU: {aimonRival.hp} :.\n")
            potenciador()
            turnoRival()
            turnoProtagonista()
        ganador()

def turnoProtagonista():
    global contPotAimon
    while True:
        if contPotAimon > 1:
            print(f"""\n{aimon.nombre} estas son tus habilidades
                            .:Ménu:.
                            1. {aimon.ataque1[0]}
                            2. {aimon.ataque2[0]}
                            3. {aimon.ataque3[0]}
                            """)
        else:
            print(f"""\n{aimon.nombre} estas son tus habilidades
                .:Ménu:.
                1. {aimon.ataque1[0]}
                2. {aimon.ataque2[0]}
                3. {aimon.ataque3[0]}
                4. {aimon.potenciador[0]}
                """)

        eleccion = int(input("Elige una Habilidad: "))

        if eleccion == 1:
            aimonRival.hp -= aimon.ataque1[1]
            break
        elif eleccion == 2:
            aimonRival.hp -= aimon.ataque2[1]
            break
        elif eleccion == 3:
            aimonRival.hp -= aimon.ataque3[1]
            break
        elif eleccion == 4:
            contPotAimon += 1
            aimon.ataque1[1] += 2
            print(f"""Se Activo Potenciador {aimon.potenciador[0]}
                {aimon.ataque1[0]} tendra {aimon.ataque1[1]} de daño por 2 turnos""")
            break
        else:
            print("Elige una opción valida")

def turnoRival():
    global contPotRival
    while True:
        print(f"\nTurno de {aimonRival.nombre}")
        if contPotRival > 1:
            eleccion = random.randint(1, 3)
        else:
            eleccion = random.randint(1, 4)

        if eleccion == 1:
            print(f'Eligió {aimonRival.ataque1[0]}\n')
            aimon.hp -= aimonRival.ataque1[1]
            break
        elif eleccion == 2:
            print(f'Eligió {aimonRival.ataque2[0]}\n')
            aimon.hp -= aimonRival.ataque2[1]
            break
        elif eleccion == 3:
            print(f'Eligió {aimonRival.ataque3[0]}\n')
            aimon.hp -= aimonRival.ataque3[1]
            break
        elif eleccion == 4:
            contPotRival += 1
            aimonRival.ataque1[1] += 2
            print(f"""Se Activo Potenciador {aimonRival.potenciador[0]}
                {aimonRival.ataque1[0]} tendra {aimonRival.ataque1[1]} de daño por 2 turnos""")
            break

def potenciador():
    global contPotAimon
    global contPotRival

    if contPotAimon > 0:
        print("\nPotenciador Activado")
        contPotAimon += 1
        if contPotAimon == 4:
            print("\nPotenciador Desactivado")
            aimon.ataque1[1] -= 2
            contPotAimon = 0
    else:
        pass

    if contPotRival > 0:
        print("\nPotenciador Rival Activado")
        contPotRival += 1
        if contPotRival == 4:
            print("\nPotenciador Rival Desactivado")
            aimonRival.ataque1[1] -= 2
            contPotRival = 0
    else:
        pass

def ganador():
    if aimon.hp > aimonRival.hp:
        print(f"\nGANASTE LA BATALLA, ahora {aimon.nombre} es más fuerte")
    elif aimonRival.hp > aimon.hp:
        print("\nFIN DE LA BATALLA")
        print(f"{aimonRival.nombre} vencio a {aimon.nombre}")
        menu()

def pocima():
    aimon.hp = 25
    aimon.ataque1[1] = 3
    aimonRival.hp = 25
    aimonRival.ataque1[1] = 3

def aimonDex():
    while True:
        print(f"""
            ..:: AIMONDEX ::..
            1. {AQUARDER}
            2. {FIRESOR}
            3. {ELECTDER}
            4. {MOUSEBUG}
            5. {SPLAT}
            6. {ROCKDOG}
            
            0. Salir
            """)

        eleccion = int(input("Elije una opción: "))

        if eleccion == 1:
            detallesAquader()
            print("Mira las habilidades de otro Aimon..")
        elif eleccion == 2:
            detallesFiresor()
            print("Mira las habilidades de otro Aimon..")
        elif eleccion == 3:
            detallesElectder()
            print("Mira las habilidades de otro Aimon..")
        elif eleccion == 4:
            detallesMousebug()
            print("Mira las habilidades de otro Aimon..")
        elif eleccion == 5:
            detallesSplat()
            print("Mira las habilidades de otro Aimon..")
        elif eleccion == 6:
            detallesRockdog()
            print("Mira las habilidades de otro Aimon..")
        elif eleccion == 0:
            menu()
        else:
            print("Elige una opción valida: ")

if __name__ == '__main__':
    inicio()
