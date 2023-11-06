import random

# reparto de las cartas
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

# checkear el ganador
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

# resultados
def crear_resultado(manojugador,manodistribuidor):
    if total(manojugador)==21:
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nBlackjack: jugador gana!"
        return resultado
    elif total(manodistribuidor)==21:
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nBlackjack: distribuidor gana!"
        return resultado
    elif total(manodistribuidor)>21:
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\ndistribuidor revienta! jugador gana!"
        return resultado
    elif total(manojugador)>21:
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\njugador revienta! distribuidor gana!"
        return resultado
    elif 21-total(manojugador)<21-total(manodistribuidor):
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\njugador gana!"
        return resultado
    elif 21-total(manodistribuidor)<21-total(manojugador):
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\ndistribuidor gana!"
        return resultado
    elif 21-total(manojugador)==21-total(manodistribuidor):
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nempate!"
        return resultado

if __name__=="__main__":
    # entidades
    jugador=input("nombre del jugador: ")
    distribuidor=input("nombre del distribuidor: ")
    # cubierta de las cartas y cartas del jugador y del distribuidor
    cubierta = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]
    manojugador=[]
    manodistribuidor=[]
    # bucle del juego
    for i in range(2): # se repite el proceso 'repartir_carta' dos veces por cada entidad
        # el distribuidor coje dos cartas
        turno=repartir_cartasjugador(manodistribuidor)
        # el jugador coje dos cartas
        turno=repartir_cartasdistribuidor(manojugador)
        while jugador or distribuidor:
            # se revela la mano del jugador
            revelacionmanojugador=revelar_mano_jugador(manojugador)
            mensajejugador="\njugador tiene "+str(revelacionmanojugador)+" y X"
            print(mensajejugador)
            if distribuidor:
                selecciondistribuidor=input("opcion 1: permanecer\nopcion 2: atacar\nelije una opcion: ")
                if selecciondistribuidor==1:
                    # el distribuidor no hace nada
                    distribuidor=False
                elif selecciondistribuidor==2:
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
                seleccionjugador=input("opcion 1: permanecer\nopcion 2: atacar\nelije una opcion: ")
                if seleccionjugador==1:
                    # el jugador no hace nada
                    jugador=False
                elif seleccionjugador==2:
                    # el distribuidor coje una carta
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
            elif total(distribuidor)>16:
                turno=repartir_cartasjugador(manojugador)
            if total(manojugador)>=21:
                jugador=False
            elif total(manodistribuidor)>=21:
                distribuidor=False
    resultado=crear_resultado(manojugador,manodistribuidor)
    print (resultado)
