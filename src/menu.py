def iniciar_modo(modo):
    verificarmodo=int(modo)
    if verificarmodo==1:
        mododejuego="iniciando modo solitario"
        return mododejuego
    elif verificarmodo==2:
        mododejuego="iniciando modo multijugador"
        return mododejuego
    raise ValueError (str(modo)+": solo se permite introducir 1 o 2. intentalo de nuevo: ")

if __name__=="__main__":
    # entrada
    error="solo esta permitido introducir 1 o 2\n"
    modo = 'error'
    while modo == 'error':
        try:
            menu="---------------BLACKJACK---------------\n\n\tmodo 1: modo solitario\n\tmodo 2: modo solitario\n\n---------------------------------------\n"
            print (menu)
            modo=int(input("selecciona modo de juego: "))
            # procesamiento
            mododejuego=iniciar_modo(modo)
            # salida
            print(mododejuego)
        except ValueError:
            print(str(modo)+": solo se permite introducir 1 o 2. intentalo de nuevo: ")
