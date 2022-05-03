import dataIO
import datetime

# funkcije za pretragu rezervacija


def pregled_rezervacije(korisnik):
    rezervacije = dataIO.load_rezervacija()
    ret_val = []
    for rezervacija in rezervacije:
        if korisnik['username'] in rezervacija['korisnickoime']:
            ret_val.append(rezervacija)

    return ret_val

def nezapocete(korisnik):
    rezervacije = dataIO.load_rezervacija()
    ret_val = []
    for rezervacija in rezervacije:
        if korisnik['username']  in rezervacija['korisnickoime'] and rezervacija['status'] == "nezapoceta":
            ret_val.append(rezervacija)
    return ret_val

def u_toku(korisnik):
    rezervacije = dataIO.load_rezervacija()
    ret_val = []
    for rezervacija in rezervacije:
        if korisnik['username']  in rezervacija['korisnickoime'] and rezervacija['status'] == "u toku":
            ret_val.append(rezervacija)
    return ret_val


# funkcije za rezervaciju, provera  da li je datum prijave i odj veci od trenutnog datuma

def provera_datuma_prijave():
    while True:
        uneto = input("unesitre datum prijave: ")
        trenutni_datum = datetime.datetime.now()
        try:
            datum_Prijave = datetime.datetime.strptime(uneto, "%Y-%m-%d")
            if datum_Prijave >= trenutni_datum:
                return uneto
            else:
                print("Uneli ste datum iz proslosti")
        except:
            print("Los format")

def provera_datuma_odjave(datum_Prijave):
    while True:
        uneto = input("Unesite datum odjave: ")
        trenutni_datum = datetime.datetime.now()
        try:
            datum_Odjave = datetime.datetime.strptime(uneto, "%Y-%m-%d")
            if datum_Odjave >= trenutni_datum and datum_Odjave >= datetime.datetime.strptime(datum_Prijave, "%Y-%m-%d"):
                return uneto
            else:
                print("Uneli ste datum koji je manji od datuma prijave", datum_Prijave)
        except:
            print("Los format")
def provera_da_ne(ispis):
    unos = input(ispis).lower()
    while unos.strip() != "da" and unos.strip() != "ne":
        unos = input(ispis).lower()

    return unos


def unos_broja(ispis):
    while True:
        broj = input(ispis)
        if broj.isdigit():
            broj = int(broj)
            if broj > 0:
                return broj
