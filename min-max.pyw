


def minmax(noPalos, jugador, profundidad):
    ganadas = [0,0,0]
    
    #print("\t"*profundidad + "Profundidad > " + str(profundidad))
    #print("\t"*profundidad + 'Palos Restantes: ' + str(noPalos))
    #ALGUIEN GANA
    if noPalos >= 2 and noPalos <= 4:
        for i in range(2,5,+1):
            if noPalos == i:
                #print("\t"*profundidad + jugador + " toma: !"+str(abs(1-i))+"\n")
                if jugador == "PC":
                    return abs(1-i)
                else:
                    return 0
    if noPalos <= 1:
        return 1
    for i in range(1,4,+1):
        #print("\t"*profundidad + jugador +" toma: "+ str(i)+"\n")
        if jugador == 'PC':
            x = minmax(noPalos - i, 'Jugador', profundidad + 1)
            if x == 0:
                ganadas[i-1] += 1
            elif isinstance(x,list):
                for j in range(3):
                    ganadas[i-1] += x[j]
        else:
            x = minmax(noPalos - i, 'PC', profundidad + 1)
            if x == 0:
                ganadas[i-1] += 1
            elif isinstance(x,list):
                for j in range(3):
                    ganadas[i-1] += x[j]
    #print("---"*10)
    return ganadas
    



def IniciarPartida():
    pc_incia = ''
    while True:
        print("\n¿Quién inicia?\n1 - Computadora\n2 - Tu")
        pc_incia = input()

        if pc_incia == '1':
            pc_incia = True
            break
        elif pc_incia == '2':
            pc_incia = False
            break

    palos_restantes = 0

    while True:
        print("\nIngrese la cantidad de palos")
        palos_restantes = int(input())
        if palos_restantes > 0:
            break
    
    while True:
        #print("Palos Restantes: " + str(palos_restantes)+"\n")
        if pc_incia:
            if palos_restantes < 20:
                jugada = minmax(palos_restantes, 'PC',0)
                if isinstance(jugada,list):
                    palos_restantes -= jugada.index(min(jugada)) + 1
                    print("PC ha tomado " + str(jugada.index(min(jugada)) + 1) + " palos")
                else:
                    palos_restantes -= jugada
                    print("PC ha tomado " + str(jugada) + " palo(s)")
            else:
                palos_restantes -= 3
                print("PC ha tomado 3 palo(s)")
            print("Palos Restantes: " + str(palos_restantes)+"\n")    
        else:
            while True:
                print("\nTu turno, ¿Cuántos palos vas a tomar?")
                jugada = int(input())
                if jugada < 1 or jugada > 3:
                    print("\nERROR > Ingresa un numero entre 1 y 3")
                else:
                    palos_restantes -= jugada
                    print("Haz tomado " + str(jugada) + " palo(s)")
                    print("Palos Restantes: " + str(palos_restantes)+"\n")
                    break
        
        if palos_restantes <= 0:
            if pc_incia:
                print("Ganaste!!")
            else:
                print("Computadora Gana!!")
            return
        
        pc_incia = not pc_incia


IniciarPartida()

print('\n\nPresiona enter para salir...')
input()

