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

def crear_resultado(manojugador,manodistribuidor):
    if total(manojugador)==21:
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nBlackjack: has ganado!"
        return resultado
    elif total(manodistribuidor)==21:
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nBlackjack: ditribuidor gana!"
        return resultado
    elif total(manojugador)>21:
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nhas reventado! distribuidor gana!"
        return resultado
    elif total(manodistribuidor)>21:
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\ndistribuidor revienta! has ganado!"
        return resultado
    elif 21-total(manojugador)<21-total(manodistribuidor):
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nhas ganado!"
        return resultado
    elif 21-total(manodistribuidor)<21-total(manojugador):
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\ndistribuidor gana!"
        return resultado
    elif 21-total(manojugador)==21-total(manodistribuidor):
        resultado="\ntu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos y el distribuidor tiene "+str(manodistribuidor)+" para un total de "+str(total(manodistribuidor))+" puntos\nempate!"
        return resultado

if __name__=="__main__":
    # entidades
    jugador=True
    distribuidor=True
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
    # se revela la mano del distribuidor
    while jugador or distribuidor:
        revelacionmanodistribuidor=revelar_mano_distribuidor(manodistribuidor)
        mensajedistribuidor="distribuidor tiene "+str(revelacionmanodistribuidor)+" y X"
        mensajejugador="tu tienes "+str(manojugador)+" para un total de "+str(total(manojugador))+" puntos" 
        # se ejecuta la definicion de total
        print(mensajedistribuidor) # se imprime la mano del distribuidor
        print (mensajejugador) # se imprime la mano del jugador
        # elige una opcion
        if jugador:
            seleccion=input("opcion 1: permanecer\nopcion 2: atacar\nelije una opcion: ")
            if seleccion=='1':
                # el jugador no hace nada
                jugador=False
            elif seleccion=='2':
                turno=repartir_cartasjugador(manojugador)
            else:
                seleccionerrorea="solo esta permitido introducir 1 o 2. intentalo de nuevo\n"
                print (seleccionerrorea)
            # el jugador coje una carta (se repite el proceso de reparto)
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
    resultado=crear_resultado(manojugador,manodistribuidor)
    print (resultado)
    
