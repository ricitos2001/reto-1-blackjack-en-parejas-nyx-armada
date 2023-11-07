import random

# iniciar modo de juego
def iniciar_modo(modo):
    verificarmodo=int(modo)
    if verificarmodo==1:
        mododejuego="iniciando modo solitario\n"
        return mododejuego
    elif verificarmodo==2:
        mododejuego="iniciando modo multijugador\n"
        return mododejuego
    raise ValueError (str(modo)+": solo se permite introducir 1 o 2. intentalo de nuevo: ")

# reparto de cartas
def repartir_cartasjugador(turno):
    carta=random.choice(cubierta)
    turno.append(carta)
    cubierta.remove(carta)
    return turno

def repartir_cartasdistribuidor(turno):
    carta=random.choice(cubierta)
    turno.append(carta)
    cubierta.remove(carta)
    return turno

# checkeo del ganador
def revelar_mano_distribuidor(manodistribuidor):
    if len(manodistribuidor)==2:
        return manodistribuidor[0]
    elif len(manodistribuidor)>2:
        return manodistribuidor[0], manodistribuidor[1]

def revelar_mano_jugador(manojugador):
    if len(manojugador)==2:
        return manojugador[0]
    elif len(manojugador)>2:
        return manojugador[0], manojugador[1]

# claculo del total de cada mano
def total(turno):
    total=0
    cara=["J", "K", "Q"]
    for carta in turno:
        if carta in range(1,11):
            total += carta
        elif carta in cara:
            total += 10
        else:
            if total > 11:
                total+=1
            else:
                total+=11
    return total

# resultados
def crear_resultadosolitario(manojugador,manodistribuidor):
    if total(manojugador)==21:
        resultadosolitario="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nBlackjack: has ganado!"
        return resultadosolitario
    elif total(manodistribuidor)==21:
        resultadosolitario="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nBlackjack: ditribuidor gana!"
        return resultadosolitario
    elif total(manojugador)>21:
        resultadosolitario="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nhas reventado! distribuidor gana!"
        return resultadosolitario
    elif total(manodistribuidor)>21:
        resultadosolitario="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\ndistribuidor revienta! has ganado!"
        return resultadosolitario
    elif 21-total(manojugador)<21-total(manodistribuidor):
        resultadosolitario="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nhas ganado!"
        return resultadosolitario
    elif 21-total(manodistribuidor)<21-total(manojugador):
        resultadosolitario="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\ndistribuidor gana!"
        return resultadosolitario
    elif 21-total(manojugador)==21-total(manodistribuidor):
        resultadosolitario="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nempate!"
        return resultadosolitario

def crear_resultadomultijugador(manojugador,manodistribuidor):
    if total(manojugador)==21:
        resultadomultijugador="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nBlackjack: jugador gana!"
        return resultadomultijugador
    elif total(manodistribuidor)==21:
        resultadomultijugador="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nBlackjack: distribuidor gana!"
        return resultadomultijugador
    elif total(manojugador)>21:
        resultadomultijugador="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\njugador revienta! distribuidor gana!"
        return resultadomultijugador
    elif total(manodistribuidor)>21:
        resultadomultijugador="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\ndistribuidor revienta! jugador gana!"
        return resultadomultijugador
    elif 21-total(manojugador)<21-total(manodistribuidor):
        resultadomultijugador="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\njugador gana!"
        return resultadomultijugador
    elif 21-total(manodistribuidor)<21-total(manojugador):
        resultadomultijugador="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\ndistribuidor gana!"
        return resultadomultijugador
    elif 21-total(manojugador)==21-total(manodistribuidor):
        resultadomultijugador="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nempate!"
        return resultadomultijugador

if __name__=="__main__":
    error="solo esta permitido introducir 1 o 2\n"
    modo = 'error'
    while modo == 'error':
        try:
            menu="---------------BLACKJACK---------------\n\n\tmodo 1: modo solitario\n\tmodo 2: modo multijugador\n\n---------------------------------------\n"
            print (menu)
            modo=int(input("selecciona modo de juego: "))
            if modo==1:
                modosolitario=iniciar_modo(modo)
                print (modosolitario)
                # entidades
                jugador=True
                distribuidor=True
                # cubierta de las cartas y cartas del jugador y del distribuidor
                cubierta = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]
                manojugador=[]
                manodistribuidor=[]
                # bucle del juego
                for i in range(2):
                    # el distribuidor coje dos cartas
                    turno=repartir_cartasjugador(manodistribuidor)
                    # el jugador coje dos cartas
                    turno=repartir_cartasdistribuidor(manojugador)
                # se revela la mano del distribuidor
                while jugador or distribuidor:
                    revelacionmanodistribuidor=revelar_mano_distribuidor(manodistribuidor)
                    mensajedistribuidor="distribuidor tiene "+str(revelacionmanodistribuidor)+" y X"
                    mensajejugador="tu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos" 
                    # se imprime la mano del distribuidor
                    print(mensajedistribuidor)
                    # se imprime la mano del jugador
                    print (mensajejugador)
                    # elige una opcion
                    if jugador:
                        seleccion=input("opcion 1: permanecer\nopcion 2: atacar\nelije una opcion: ")
                        if seleccion=='1':
                            # el jugador no hace nada
                            jugador=False
                        elif seleccion=='2':
                            # el jugador coje una carta
                            turno=repartir_cartasjugador(manojugador)
                        else:
                            seleccionerrorea="solo esta permitido introducir 1 o 2. intentalo de nuevo\n"
                            print (seleccionerrorea)
                    if total(manojugador)>16:
                        # el distribuidor no hace nada
                        distribuidor=False
                    else:
                        # el distribuidor coje una carta (se repite el proceso de reparto)
                        turno=repartir_cartasdistribuidor(manodistribuidor)
                    if total(manojugador)>=21:
                        jugador=False
                    elif total(manodistribuidor)>=21:
                        distribuidor=False
                resultadosolitario=crear_resultadosolitario(manojugador,manodistribuidor)
                print (resultadosolitario)
            elif modo==2:
                modomultijugador=iniciar_modo(modo)
                print (modomultijugador)
                # nombre del jugador
                jugador=input("nombre del jugador: ")
                # nombre del distribuidor
                distribuidor=input("nombre del distribuidor: ")
                # cubierta de las cartas y cartas del jugador y del distribuidor
                cubierta = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]
                manojugador=[]
                manodistribuidor=[]
                # bucle del juego
                for i in range(2):
                    # el distribuidor coje dos cartas
                    turno=repartir_cartasjugador(manodistribuidor)
                    # el jugador coje dos cartas
                    turno=repartir_cartasdistribuidor(manojugador)
                while jugador or distribuidor:
                    # se revela la mano del jugador
                    revelacionmanojugador=revelar_mano_jugador(manojugador)
                    mensajejugador="\njugador tiene "+str(revelacionmanojugador)+" y X"
                    print(mensajejugador)
                    # distribuidor elige una opcion
                    if distribuidor:
                        selecciondistribuidor=input("opcion 1: permanecer\nopcion 2: atacar\nelije una opcion: ")
                        if selecciondistribuidor=="1":
                            # el distribuidor no hace nada
                            distribuidor=False
                        elif selecciondistribuidor=="2":
                            # el distribuidor coje una carta
                            turno=repartir_cartasjugador(manojugador)
                        else:
                            seleccionerrorea="solo esta permitido introducir 1 o 2. intentalo de nuevo\n"
                            print (seleccionerrorea)
                    # se revela la mano del distribuidor
                    revelacionmanodistribuidor=revelar_mano_distribuidor(manodistribuidor)
                    mensajedistribuidor="\ndistribuidor tiene "+str(revelacionmanodistribuidor)+" y X"
                    print(mensajedistribuidor)
                    if jugador:
                        # jugador elije una opcion
                        seleccionjugador=input("opcion 1: permanecer\nopcion 2: atacar\nelije una opcion: ")
                        if seleccionjugador=="1":
                            # el jugador no hace nada
                            jugador=False
                        elif seleccionjugador=="2":
                            # el jugador coje una carta
                            turno=repartir_cartasjugador(manojugador)
                        else:
                            seleccionerrorea="solo esta permitido introducir 1 o 2. intentalo de nuevo\n"
                            print (seleccionerrorea)
                    if total(manojugador)>16:
                        distribuidor=False
                    elif total (manojugador)<16:
                        turno=repartir_cartasdistribuidor(manodistribuidor)
                    elif total(distribuidor)>16:
                        totaljugador=False
                    elif total(distribuidor)<16:
                        turno=repartir_cartasjugador(manojugador)
                    if total(manojugador)>=21:
                        jugador=False
                    elif total(manodistribuidor)>=21:
                        distribuidor=False
                resultadomultijugador=crear_resultadomultijugador(manojugador,manodistribuidor)
                print (resultadomultijugador)
        except ValueError:
            print(str(modo)+": solo se permite introducir 1 o 2. intentalo de nuevo: ")