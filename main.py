from termcolor import cprint
import sys
import random

import Carta

print("vuoi giocare?")

cprint('g per GIOCA', 'blue')
cprint('n per NO', 'yellow')

exit = 'e\n'
stand = 's\n'
hit = 'h\n'


def vediCarteUtente(listaCarteUtente):
    somma = 0
    for carta in listaCarteUtente:
        cprint(carta.toString(), 'cyan')
        somma += carta.getVal()
    if somma == 11:
        somma = 21

    return somma


def vediCarteBanco(listaCarteBanco):
    somma = 0
    for carta in listaCarteBanco:
        cprint(carta.toString(), 'magenta')
        somma += carta.getVal()
    if somma == 11:
        somma = 21

    return somma


def daiCarte(carteDistribuite):
    c = random.randint(0, len(carte) - 1)
    carteDistribuite.append(carte[c])
    carte.remove(carte[c])


def giochiamo(first_input, punteggioUtente, punteggioBanco):
    daiCarte(carteUtente)
    daiCarte(carteUtente)
    daiCarte(carteBanco)
    daiCarte(carteBanco)
    while first_input.lower() != exit and len(carte) > 0:
        print("Le tue carte: ")
        punteggioUtente += vediCarteUtente(carteUtente)
        print("\n")
        print("Le carte del banco: ")
        punteggioBanco += vediCarteBanco(carteBanco)
        print("\n")
        cprint("La somma delle tue Carte è: " + str(punteggioUtente), 'cyan')
        cprint("La somma del banco è: " + str(punteggioBanco), 'magenta')
        print("\n")

        if (punteggioUtente == 21):
            cprint("HAI VINTO, hai fatto ->" + str(punteggioUtente), 'green')
            first_input = exit
            break
        if (punteggioBanco == 21):
            cprint("HAI PERSO, il banco ha raggiunto ->" + str(punteggioBanco), 'red')
            first_input = exit
            break
        if (punteggioUtente > 21):
            cprint("HAI PERSO, hai superato 21 con ->" + str(punteggioUtente), 'red')
            first_input = exit
            break
        if (punteggioBanco > 21):
            cprint("HAI VINTO, il banco ha superato 21 con->" + str(punteggioBanco), 'green')
            first_input = exit
            break

        while (punteggioUtente <= 21 and first_input != stand):
            cprint("se vuoi richiedere carta, inserisci la lettere h di HIT ME", 'blue')
            cprint("oppure se vuoi stare, inserisci la lettere s di STAND", 'yellow')
            first_input = sys.stdin.readline()

            if (first_input == hit):
                daiCarte(carteUtente)
                punteggioUtente = 0
                punteggioUtente += vediCarteUtente(carteUtente)
                cprint("ora il tuo punteggio è: " + str(punteggioUtente), 'cyan')
                print("\n")
            if (first_input == stand):
                print("le tue carte sono: ")
                vediCarteUtente(carteUtente)
                cprint("ora il tuo punteggio è: " + str(punteggioUtente), 'cyan')
                print("\n")
            if (punteggioUtente == 21):
                cprint("HAI VINTO, hai raggiunto ->" + str(punteggioUtente), 'cyan')
                print("\n")
                punteggioBanco = 22
                first_input = exit
                break
            if (punteggioUtente > 21):
                cprint("HAI PERSO, hai superato 21 con ->" + str(punteggioUtente), 'red')
                print("\n")
                punteggioBanco = 50
                first_input = exit
                break

        if (punteggioBanco <= punteggioUtente):
            if (punteggioUtente < 21):
                if (punteggioBanco == punteggioUtente):
                    punteggioUtente += vediCarteBanco(carteBanco)
                    cprint(
                        "HAI PERSO perchè hai pareggiato, il banco ha raggiunto ->" + str(
                            punteggioBanco) + " e tu hai -> " + str(
                            punteggioUtente), 'red')
                    print("\n")
                else:
                    while (punteggioBanco < 19):
                        if (punteggioBanco <= punteggioUtente):
                            cprint("il banco richiede carta", 'magenta')
                            daiCarte(carteBanco)
                            punteggioBanco = 0
                            punteggioBanco += vediCarteBanco(carteBanco)
                            print("\n")
                            cprint("ora il punteggio del banco è: " + str(punteggioBanco), 'magenta')
                            print("\n")

                            if (punteggioBanco == punteggioUtente):
                                vediCarteBanco(carteBanco)
                                cprint(
                                    "HAI PERSO perchè hai pareggiato, il banco ha raggiunto ->" + str(
                                        punteggioBanco) + " e tu hai -> " + str(
                                        punteggioUtente), 'red')
                                print("\n")
                                first_input = exit
                                break

                            if (punteggioBanco == 11):
                                cprint("HAI PERSO, il banco ha raggiunto ->" + str(punteggioBanco), 'red')
                                print("\n")
                                first_input = exit
                            if (punteggioBanco == 21):
                                cprint("HAI PERSO, il banco ha raggiunto ->" + str(punteggioBanco), 'red')
                                print("\n")
                                first_input = exit
                            if (punteggioBanco > 21):
                                cprint("HAI VINTO, il banco ha superato 21 con->" + str(punteggioBanco), 'green')
                                print("\n")
                                break
                            if (punteggioBanco >= 19 and punteggioBanco <= 21):
                                if (punteggioBanco < punteggioUtente):
                                    cprint("HAI VINTO, hai fatto ->" + str(punteggioUtente), 'green')
                                    print("\n")
                                    break
                                else:
                                    cprint("HAI PERSO, il banco ha raggiunto ->" + str(punteggioBanco), 'red')
                                    print("\n")
                                    break
                        else:
                            cprint("HAI PERSO, il banco ha raggiunto ->" + str(punteggioBanco) + " e tu hai -> " + str(
                                punteggioUtente),
                                   'red')
                            print("\n")
                            first_input = exit
                            break
            if (punteggioUtente == 21):
                cprint("HAI VINTO, hai raggiunto 21 con->" + str(punteggioBanco), 'green')
                print("\n")
                break
        else:
            if punteggioUtente < 21:
                punteggioBanco = 0
                punteggioBanco += vediCarteBanco(carteBanco)
                cprint("HAI PERSO, il banco ha raggiunto ->" + str(punteggioBanco) + " e tu hai -> " + str(
                    punteggioUtente),
                       'red')
                print("\n")
                first_input = exit
        first_input = exit

#inizio gioco
first_input = sys.stdin.readline()

while first_input.lower() != 'n\n':
    carte = [Carta.assoC, Carta.assoF, Carta.assoQ, Carta.assoP,
             Carta.dueC, Carta.dueF, Carta.dueQ, Carta.dueP,
             Carta.treC, Carta.treF, Carta.treQ, Carta.treP,
             Carta.quattroC, Carta.quattroF, Carta.quattroQ, Carta.quattroP,
             Carta.cinqueC, Carta.cinqueF, Carta.cinqueQ, Carta.cinqueP,
             Carta.seiC, Carta.seiF, Carta.seiQ, Carta.seiP,
             Carta.setteC, Carta.setteF, Carta.setteQ, Carta.setteP,
             Carta.ottoC, Carta.ottoF, Carta.ottoQ, Carta.ottoP,
             Carta.noveC, Carta.noveF, Carta.noveQ, Carta.noveP,
             Carta.dieciC, Carta.dieciF, Carta.dieciQ, Carta.dieciP,
             Carta.jackC, Carta.jackF, Carta.jackQ, Carta.jackP,
             Carta.donnaC, Carta.donnaF, Carta.donnaQ, Carta.donnaP,
             Carta.reC, Carta.reF, Carta.reQ, Carta.reP]
    carteUtente = []
    carteBanco = []
    punteggioUtente = 0
    punteggioBanco = 0
    if first_input.lower() == 'g\n':
        giochiamo(first_input, punteggioUtente, punteggioBanco)
    else:
        print("errore nell'inserimento, riavvia il programma")
    print("se vuoi smettere di giocare digita n, altrimenti digita g")
    first_input = sys.stdin.readline()
