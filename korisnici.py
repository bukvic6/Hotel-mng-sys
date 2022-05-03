import korisniciIO

def za_login(username, password):
    lista_korisnika = korisniciIO.load_korisnici()
    for korisnik in lista_korisnika:
        if korisnik['username'] == username and korisnik['password'] == password:
            return korisnik
    print('pogresan unos')



lista_korisnika = korisniciIO.load_korisnici()

def dodajkorisnika(korisnik):
    for kek in lista_korisnika:
        if kek['username'] == korisnik['username']:
            return False
    lista_korisnika.append(korisnik)
    return True

def unesikorisnika():
    korisnik = {}
    uloga = "korisnik"
    korisnik['uloga'] = uloga
    ime = input("Unesite ime: ")
    korisnik['ime'] = ime
    prezime = input("Prezime: ")
    korisnik['prezime']  = prezime
    username = input("Username: ")
    korisnik['username']  = username
    password = input("Password: ")
    korisnik['password']  = password
    telefon = input("Telefon: ")
    korisnik['telefon']  = telefon
    email = input('Email: ')
    korisnik['email'] = email
    korisnik['rezervacije'] = []
    return korisnik

def korisnik2str(korisnik):
    s = korisnik['uloga'] + '|' + korisnik ['ime'] + '|' + korisnik ['prezime'] + '|' +  korisnik ['username'] + '|' + korisnik ['password'] + '|'+  korisnik ['telefon'] + '|' +  korisnik ['email']
    if korisnik['uloga'] == "recepcioner":
        s +='|' +  korisnik["IDhotela"]
    elif korisnik['uloga'] == "korisnik":
        rez = ""
        for r in korisnik["rezervacije"]:
            rez += '|' + r
        s += rez
    return s



def snimi(nazivfajla):
    target = open(nazivfajla, "w")
    for korisnik in lista_korisnika:
        target.write(korisnik2str(korisnik) + '\n')
    target.close()

