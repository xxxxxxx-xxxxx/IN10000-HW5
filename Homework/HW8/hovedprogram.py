from verden import Verden

def hovedprogram():
    try:
        print("Oppretter en verden...")
        print("Oppgi antall rader og kolonner...")
        rader = int(input("Rader: "))
        kolonner = int(input("Kolonner: "))
    except Exception:
        print("Kan kun ta inn heltall...")
        return
    
    verden = Verden(rader, kolonner)
    verden.tegn()

    while True:
        x = input("\nEnter for å oppdatere og 'q/Q' for å stoppe...")
        if x == 'q' or x == 'Q':
            print("Avslutter...")
            break
        verden.oppdatering()
        verden.tegn()

if __name__ == "__main__":
    hovedprogram()
    pass

# starte hovedprogrammet
hovedprogram()