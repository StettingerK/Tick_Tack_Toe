from rich import print

def eingabe_spieler() -> list:
    spieler = []
    while len(spieler) < 2:

        #Abfrage von Namen der Spieler
        name_spieler = input(f"Geben Sie den Namen für Spieler {len(spieler)+1} ein: ")
        if name_spieler != "":
            spieler.append(name_spieler)
    
    return spieler

def eingabe_zug() -> tuple[str, int]:
    while True:
        zeile = input("Bitte gib an welche Zeile (a,b,c): ").lower()
        if (zeile == "a" or zeile == "b" or zeile == "c") :
            break
        else:
            print("keine richtige Eingabe bitte gib a oder b oder c ein ")
    while True:
        spalte = input("Bitte gib an welche Spalte (1,2,3): ")
        if (spalte == "1" or spalte == "2" or spalte == "3"):
            break
        else:
            print("keine richtige Eingabe bitte gib 1 oder 2 oder 3 ein ")
    return zeile,int(spalte)-1

def print_spiel(spielfeld:dict[list[str]]):
    print("\n    1   2   3  ")
    print("  +---+---+---+")
    print(f"a | {farbe(spielfeld["a"][0])} | {farbe(spielfeld["a"][1])} | {farbe(spielfeld["a"][2])} |")
    print("  +---+---+---+")
    print(f"b | {farbe(spielfeld["b"][0])} | {farbe(spielfeld["b"][1])} | {farbe(spielfeld["b"][2])} |")
    print("  +---+---+---+")
    print(f"c | {farbe(spielfeld["c"][0])} | {farbe(spielfeld["c"][1])} | {farbe(spielfeld["c"][2])} |")
    print("  +---+---+---+\n")

def ausgabe(inp:str):
    print(inp)

def farbe(zeichen: str) -> str:
    if zeichen == "x":
        return "[bold red]X[/bold red]"
    if zeichen == "0":
        return "[bold blue]O[/bold blue]"
    return " "

if __name__ == "__main__":
    #print(eingabe_spieler())
    #print(eingabe_zug())
    spiel = {"a":["0"," ","0"],"b":[" ","x"," "],"c":[" ","x"," "]}
    print_spiel(spiel)