import gui
import random
import os

def spieler_zeichen_ermitteln(player_counter: int) -> str:
    return "0" if player_counter == 0 else "x"

def ist_gleich(values:list[str]) -> bool:
    value1 = values[0]
    for value in values:
        if value == value1 and value != " ":
            continue
        else:
            return False
    return True

def gewonnen_ermitteln(spielfeld:dict[list[str]]) -> bool:
    for zeile in spielfeld: #zeilen abgleich
        values = []
        for spalte in spielfeld[zeile]:
            values.append(spalte)
        if ist_gleich(values):
            return True
    for i in range(len(spielfeld)): #spalten gleich
        values = []
        for zeile in spielfeld:
            values.append(spielfeld[zeile][i])
        if ist_gleich(values):
            return True
        
    # diagonal links oben nach rechts unten
    values = []
    zeilen_counter = 0
    for zeile in spielfeld:
        values.append(spielfeld[zeile][zeilen_counter])
        zeilen_counter+=1
    if ist_gleich(values):
        return True
    # diagonal links unten nach rechts oben
    values = []
    zeilen_counter = len(spielfeld)-1
    for zeile in spielfeld:
        values.append(spielfeld[zeile][zeilen_counter])
        zeilen_counter-=1
    if ist_gleich(values):
        return True
    return False #nicht gewonnen

def unentschieden_ermitteln(spielfeld:dict[list[str]]) -> bool:
    for zeile in spielfeld:
        for spalte in spielfeld[zeile]:
            if spalte == " ":
                return False
        

def main():
    player = ["Kevin","Oli"]#gui.eingabe_spieler()
    #player_eingabe = {player[0]:[],player[1]:[]}
    playing = True
    player_counter = random.randint(0,1) #zufällig wer anfangen darf
    spielfeld = {"a":[" "," "," "],"b":[" "," "," "],"c":[" "," "," "]}
    while playing:
        gui.ausgabe(f'Spieler "{player[player_counter]}" ist an der Reihe')
        gui.print_spiel(spielfeld)
        while True: #solange bis Spieler richtige eingabe gemacht hat
            zeile, spalte = gui.eingabe_zug()
            if spielfeld[zeile][spalte] == " ":
                spielfeld[zeile][spalte] = spieler_zeichen_ermitteln(player_counter)
                break
            else:
                gui.ausgabe("Feld schon belegt bitte geben Sie ein anderes Feld ein")
                continue
        if gewonnen_ermitteln(spielfeld):
            gui.print_spiel(spielfeld)
            gui.ausgabe(f'Spieler "{player[player_counter]}" hat Gewonnen')
            with open("Gewinner.txt", "a")as file:
                file.write(f'Spieler "{player[player_counter]}" hat Gewonnen')
            break
        if unentschieden_ermitteln(spielfeld):
            gui.ausgabe(f'Unentschieden keiner hat Gewonnen')
            break
        player_counter = 0 if player_counter == 1 else 1
        os.system("cls" if os.name == "nt" else "clear")



if __name__ == "__main__":
    main()
