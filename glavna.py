import hoteli
import korisnici
import korisniciIO
import data
import dataIO
import hoteliIO
import datetime
import rezervacije
import pretraga_recep


def main():
    while True:
        print('dobrodosli u hotel')
        print('1) prijavite se')
        print('2) registrujte se')
        print('3) kraj programa')
        prvaopcija = input("opcija?")
        if prvaopcija == "1":
            # login >>
            korisnik = login()
            if korisnik == None:
                print("Los unos" + '\n')
                continue

            if korisnik['uloga'] == "korisnik":
                print("ulogovani ste kao : " + korisnik['username'])
                meni_korisnika(korisnik)


            elif korisnik['uloga'] == "recepcioner":
                print("ulogovani ste kao : " + korisnik['uloga'])
                meni_recepcionera(korisnik)
            elif korisnik['uloga'] == "administrator":
                print("ulogovani ste kao : " + korisnik['uloga'])
                meni_administratora(korisnik)

        # registracija >>

        elif prvaopcija == "2":
            korisnik = korisnici.unesikorisnika()
            uspesnododavanje = korisnici.dodajkorisnika(korisnik)
            if uspesnododavanje:
                korisnici.snimi("korisnici.txt")
                print("uspesno ste se registrovali\n")


            else:
                print('Molimo odaberite drugaciji username\n')
        elif prvaopcija == "3":
            break



def login():
    print("prijavite se na sistem" + '\n')
    username = input('korisnicko ime: ')
    password = input('lozinka: ')
    uspesno = korisnici.za_login(username, password)
    return uspesno


def meni_korisnika(korisnik):
    while True:
        print( '\n')
        print('1) Pregled hotela')
        print('2) Pretraga hotela')
        print('3) Prikaz najbolje ocenjenih hotela')
        print('4) Kreiranje rezervacije')
        print('5) Pregled rezervacija')
        print('6) Ocenjivanje hotela')
        print('7) Odjava')

        opcija = input("Opcija? ")

        if opcija == '1':
            print(hoteli.hoteli_heder())
            l_hoteli = hoteli.get_sorted_by_name()
            print_hoteli(l_hoteli)
        elif opcija == '2':
            pretraga(korisnik)
        elif opcija == '3':
            hoteli_prvih_pet = hoteliIO.load_hoteli()
            prvih_pet = hoteli.sortiraj(hoteli_prvih_pet)
            print(hoteli.hoteli_heder)
            print_hoteli(prvih_pet[:5])
        elif opcija == '4':
            dodavanje_rezervacija(korisnik)
        elif opcija == '5':
            izbor_rezervacija(korisnik)
        elif opcija == '6':
            pass
        elif opcija == '7':
            break


def pretraga(korisnik):
    print("odaberite opciju")
    print("1) pretraga po imenu hotela")
    print("2) pretraga po adresi hotela")
    print("3) pretraga po oceni hotela")
    print("4) pretraga-vise kriterijuma")
    print('5) nazad')
    opcija2 = input(">> ")
    if opcija2 == "1":
        po_imenu = input('Ime: ')
        l_students = hoteli.filter_ime(po_imenu)
        print(hoteli.hoteli_heder())
        print_hoteli(l_students)
    elif opcija2 == "2":
        po_adresi = input('adresa: ')
        l_students = hoteli.filter_adresa(po_adresi)
        print(hoteli.hoteli_heder())
        print_hoteli(l_students)
    elif opcija2 == "3":
        po_oceni = input('ocena: ')
        l_students = hoteli.filter_ocena(po_oceni)
        print(hoteli.hoteli_heder())
        print_hoteli(l_students)
    elif opcija2 == "4":
        po_imenu = input('Ime: ')
        po_adresi = input('adresa: ')
        po_oceni = input('ocena: ')
        l_students = hoteli.visekrit_pretraga(po_imenu, po_adresi, po_oceni)
        print(hoteli.hoteli_heder())
        print_hoteli(l_students)
    elif opcija2 == "5":
        meni_korisnika(korisnik)
    else:
        print("unesite odgovarajucu komandu")


def izbor_rezervacija(korisnik):
    print("pregled rezervacija")
    print("1) Pregled rezervacija koje nisu zapocete")
    print("2) Rezervacije u toku")
    print("3) zavrsene rezervacije")
    print("4) Nazad")
    opcija = input('opcija: ')
    if opcija == '1':
        proba = data.pregled_rezervacije(korisnik)
        print_rezervacije(proba)
        meni_korisnika(korisnik)
    elif opcija == '2':
        proba = data.u_toku(korisnik)
        print_rezervacije(proba)
        meni_korisnika(korisnik)
    elif opcija == '3':
        proba = data.nezapocete(korisnik)
        print_rezervacije(proba)
        meni_korisnika(korisnik)
    elif opcija == '4':
        meni_korisnika(korisnik)


def los_Unos_Odabranih_Soba(sobe, odabraneSobeId):
    listaValidnihIdSoba = []
    for s in sobe:
        listaValidnihIdSoba.append(s["IDsoba"])

    ids = odabraneSobeId.split(",")
    for odabraniId in ids:
        if not odabraniId in listaValidnihIdSoba:
            return True
    return False


def los_Unos_Hotela(hoteli, imeHotela):
    for h in hoteli:
        if h["ime"] == imeHotela:
            return False
    return True


def pronadjiSveSobeZaHotel(hoteli, sobe, imeHotela):
    sobeHotelaId = []
    for h in hoteli:
        if h["ime"] == imeHotela:
            sobeHotelaId = h["idsobe"]

    sobeRecnici = []
    for s in sobe:
        if s["IDsoba"] in sobeHotelaId:
            sobeRecnici.append(s)
    return sobeRecnici


def dodavanje_rezervacija(korisnik):
    rezervacija = {}

    lista_Rezervacija = dataIO.load_rezervacija()

    listaIdRezervacija = []
    for rez in lista_Rezervacija:
        listaIdRezervacija.append(int(rez["IDrezervacija"]))

    rezervacija['IDrezervacija'] = str(max(listaIdRezervacija) + 1)

    vreme_rezervacije = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    rezervacija['vremekreiranja'] = vreme_rezervacije

    datum_Prijave = data.provera_datuma_prijave()
    rezervacija['prijava'] = datum_Prijave

    datum_Odjave = data.provera_datuma_odjave(datum_Prijave)
    rezervacija['odjava'] = datum_Odjave

    rezervacija['status'] = "nezapoceta"
    rezervacija['ocenahotela'] = "-1"
    rezervacija["korisnickoime"] = korisnik["username"]

    hoteli = hoteliIO.load_hoteli()
    print_hoteli(hoteli)
    while True:
        imeHotela = input("Unesite ime hotela")
        if los_Unos_Hotela(hoteli, imeHotela):
            print("Molimo vas unesite ispravan naziv hotela")
        else:
            break

    sobe = dataIO.load_soba()

    sobe = pronadjiSveSobeZaHotel(hoteli, sobe, imeHotela)
    print_soba(sobe)

    while True:
        odabraneSobeIds = input("Unesite id-eve soba odvojene zarezom")
        if los_Unos_Odabranih_Soba(sobe, odabraneSobeIds):
            print("Molimo vas unesite ispravne vrednosti id-eva za sobe")
        else:
            break
    rezervacija['sobe'] = odabraneSobeIds.split(",")

    rezervacije.dodajRezervaciju(rezervacija)
    rezervacije.snimi("rezervacije.txt")


# RECEPCIONER >>

def meni_recepcionera(korisnik):
    print("1) Pretraga soba")
    print("2) Pretraga rezervacija")
    print("3) izvestaj")


def azuriranje_hotela(korisnik):
    hoteli = hoteliIO.load_hoteli()
    print_hoteli(hoteli)
    ime_hotela = input("Unesite ime hotela koji zelite da azutirate: ")
    """
    
    100001|Fontana|Nikole Pasica 27 |ne|da|7|200001
    100002|Garden|Primorska 50 |ne|ne|2|200002
    100003|Sheraton|Polgar Andrasa 1|da|da|8|200003
    100004|Pupin|Narodnih heroja |ne|da|9|200004
    100005|Garni|Uspenska 1|da|da|6|200005
    100006|Vila Dama|Backa 14|ne|da|8|200006
    100001|Fontana|Nikole Pasica 27 |ne|da|7|200011
    """
    while True:
        print("1. Dodavanje soba")
        print("2. Dodaj bazen")
        print("3. Dodaj restoran")
        opcija = input("opcija? ")
        if opcija == "1":

            for hotel in hoteli:
                if ime_hotela == hotel["ime"]:
                    broj_soba = data.unos_broja("Unesite koliko soba zelite dodati: ")
                    id_dodate_sobe = dodavanje_soba(broj_soba)
                    for id in id_dodate_sobe:
                        hotel["idsobe"].append(id)
                    break

            target = open('hoteli.txt', 'w')
            for hotel in hoteli:
                sobeIds = ""
                for id in hotel["idsobe"]:
                    sobeIds += "|" + id
                target.write(
                    hotel['id'] + '|' + hotel['ime'] + '|' + hotel['adresa'] + '|' + hotel['restoran'] + '|' + hotel[
                        'bazen'] + '|' + hotel['ocena'] + sobeIds + "\n")
            target.close()

            break
        elif opcija == "2":
            for hotel in hoteli:
                if ime_hotela == hotel["ime"]:
                    if hotel["bazen"].lower() != "da":
                        hotel["bazen"] = "da"
                        print("Uspesno ste dodali bazen")
                    else:
                        print("Bazen vec postoji")
                    break
            target = open('hoteli.txt', 'w')
            for hotel in hoteli:
                sobeIds = ""
                for id in hotel["idsobe"]:
                    sobeIds += "|" + id
                target.write(
                    hotel['id'] + '|' + hotel['ime'] + '|' + hotel['adresa'] + '|' + hotel['restoran'] + '|' + hotel[
                        'bazen'] + '|' + hotel['ocena'] + sobeIds + "\n")
            target.close()
            break
        elif opcija == "3":
            for hotel in hoteli:
                if ime_hotela == hotel["ime"]:
                    if hotel["restoran"].lower() != "da":
                        hotel["restoran"] = "da"
                        print("Uspesno ste dodali restoran")
                    else:
                        print("Bazen vec postoji")
                    break
            target = open('hoteli.txt', 'w')
            for hotel in hoteli:
                sobeIds = ""
                for id in hotel["idsobe"]:
                    sobeIds += "|" + id
                target.write(
                    hotel['id'] + '|' + hotel['ime'] + '|' + hotel['adresa'] + '|' + hotel['restoran'] + '|' + hotel[
                        'bazen'] + '|' + hotel['ocena'] + sobeIds + "\n")
            target.close()
            break
        else:
            print("Neispravan izbor")


def meni_administratora(korisnik):
    while True:
        print("1) Dodavanje novog hotela")
        print("2) Dodavanje novog recepcionera")
        print("3) Azuriranje hotela")
        print("4) Brisanje hotela")
        print("5) Brisanje recepcionera")
        print("6) Pretraga recepcionera")
        print("7) dodati")
        opcija = input('opcija: ')
        if opcija == '1':
            dodavanje_hotela()
        elif opcija == '2':
            dodavanje_recepcionera()
            
        elif opcija == '3':
            azuriranje_hotela(korisnik)
        elif opcija == '4':
            pass
        elif opcija == '5':
            pass
        elif opcija == '6':
            pretraga_admin(korisnik)
            
        elif opcija == '7':
            break
def dodavanje_recepcionera():
    korisnik = {}
    uloga = "recepcioner"
    korisnik['uloga'] = uloga
    ime = input('Unesite ime novog recepcionera: ')
    korisnik["ime"] = ime
    prezime = input ('Prezime novog recepcionera: ')
    korisnik['prezime'] = prezime
    username =input('Username recepcionera: ')
    korisnik['username'] = username
    password = input('Password za recepcionera: ')
    korisnik['password'] = password
    telefon = input('Telfon recepcionera: ')
    korisnik['telefon'] = telefon
    email = input('Email recepcionera: ')
    korisnik['email'] = email
    IDhotela = input("Unesite sifru hotela za koji ce recepcioner biti zaduzen: ")
    korisnik["IDhotela"] = IDhotela
    target = open('korisnici.txt', 'a')
    target.write(korisnik['uloga'] + '|' + korisnik ['ime'] + '|' + korisnik ['prezime'] + '|' +  korisnik ['username'] + '|' + korisnik ['password'] + '|'+  korisnik ['telefon'] + '|' +  korisnik ['email']+'|'+korisnik['IDhotela'])
    target.close()
    return korisnik

def pretraga_admin(korisnik):
    print("odaberite opciju")
    print("1) pretraga recepcionera po imenu")
    print("2) pretraga recepcionera po prezimenu")
    print("3) pretraga recepcionera po korisnickom imenu")
    print("4) pretraga recepcionera po emailu ")
    print("5) prikaz svih recepcionera ")
    print("6) pretraga recepcionera po hotelu u kojem radi ")
    print("7) nazad")
    opcija = input('opcija: ')
    if opcija == '1':
        po_imenu = input('ime: ')
        l_students = pretraga_recep.filter_recepcionera_po_imenu(po_imenu)
        print(hoteli.korisnici_heder())
        print_korisnika(l_students)
        meni_administratora(korisnik)
    elif opcija == '2':
        po_prezimenu = input('prezime: ')
        l_students = pretraga_recep.filter_recepcionera_po_prezimenu(po_prezimenu)
        print(hoteli.korisnici_heder())
        print_korisnika(l_students)
        meni_administratora(korisnik)
    elif opcija == '3':
        po_username = input('Username: ')
        l_students = pretraga_recep.filter_recepcionera_po_username(po_username)
        print(hoteli.korisnici_heder())
        print_korisnika(l_students)
        meni_administratora(korisnik)
    elif opcija == '4':
        po_emailu = input('email: ')
        l_students = pretraga_recep.filter_recepcionera_po_username(po_emailu)
        print(hoteli.korisnici_heder())
        print_korisnika(l_students)
        meni_administratora(korisnik)
    elif opcija == '5':
        l_students = pretraga_recep.filter_recepcionera_po_ulozi()
        print(hoteli.korisnici_heder())
        print_korisnika(l_students)
        meni_administratora(korisnik)
    elif opcija == '6':
        po_imenu = input('Ime: ')
        po_prezimenu = input('prezime: ')
        po_username = input('username: ')
        po_emailu = input('email: ')
        l_students = pretraga_recep.visekrit_pretraga(po_imenu,po_prezimenu,po_username,po_emailu)
        print(hoteli.korisnici_heder())
        print_hoteli(l_students)
        meni_administratora(korisnik)
    elif opcija == '8':
        meni_administratora(korisnik)

def dodavanje_soba(broj_soba_koliko_zeli):
    sobe = dataIO.load_soba()
    id_dodatih_soba = []
    vrednost_id = 200000
    soba = {}
    for i in range(0, broj_soba_koliko_zeli):
        for soba in sobe:
            if vrednost_id < int(soba["IDsoba"]):
                vrednost_id = int(soba["IDsoba"])
        id_dodate = str(vrednost_id + 1)
        id_dodatih_soba.append(id_dodate)
        soba['IDsoba'] = id_dodate
        soba['brojsobe'] = input("Unesi broj sobe: ")
        soba['brojkreveta'] = input("Unesi broj kreveta: ")
        soba['tipsobe'] = input("Unesi tip sobe(apartman/jedna soba): ")
        soba['tv'] = data.provera_da_ne("Da li soba poseduje tv(da/ne): ")
        soba['klima'] = data.provera_da_ne("Da li soba poseduje klimu(da/ne): ")
        soba['cena'] = str(data.unos_broja("Unesi cenu sobe: "))
        print("Uspesno ste dodali sobu")
        target = open('sobe.txt', 'a')
        target.write(soba['IDsoba'] + '|' + soba['brojsobe'] + '|' + soba['brojkreveta'] + '|' + soba['tipsobe'] + '|' +
                     soba['tv'] + '|' + soba['klima'] + '|' + soba['cena'] + '\n')
        target.close()
    return id_dodatih_soba


def dodavanje_hotela():
    hotel = {}
    hoteli = hoteliIO.load_hoteli()

    lista_id_hotela = []
    for hotel in hoteli:
        lista_id_hotela.append(int(hotel["id"]))

    hotel['id'] = str(max(lista_id_hotela) + 1)

    hotel['ime'] = input('Unesite ime hotela: ')

    hotel['adresa'] = input('Unesite adresu hotela: ')

    hotel['restoran'] = data.provera_da_ne('Da li Hotel ima restoran? da/ne ')

    hotel['bazen'] = data.provera_da_ne('Da li hotel ima bazen? da/ne ')

    hotel['ocena'] = '-1'
    broj_soba_koliko_zeli = data.unos_broja("Unesite koliko soba zelite dodati: ")
    id_dodatih_soba = dodavanje_soba(broj_soba_koliko_zeli)
    hotel['soba'] = id_dodatih_soba
    h = '\n' + hotel['id'] + '|' + hotel['ime'] + '|' + hotel['adresa'] + '|' + hotel['restoran'] + '|' + hotel[
        'bazen'] + '|' + hotel['ocena']
    soba_id = ''
    for s in hotel['soba']:
        soba_id += '|' + s
    h += soba_id
    target = open('hoteli.txt', 'a')
    target.write(h)
    print("Uspesno ste dodali hotel")
    target.close()


# funkcije za ispisivanje iz fajla >>

def print_hoteli(l_hoteli):
    for hotel in l_hoteli:
        if hotel != None:
            print(hotel['ime'].rjust(20) + '|' + hotel['adresa'].ljust(25)[:20] + '|' + hotel['restoran'].ljust(10) + '|' + hotel['bazen'].ljust(10) + '|' + hotel['ocena'].ljust(11) + '|'+ hotel['id'])



def print_rezervacije(lista_rezervacija):
    for rezervacija in lista_rezervacija:
        if rezervacija != None:
            print(rezervacija['vremekreiranja'].rjust(10) + '|' + rezervacija['prijava'].ljust(20)[:10] + '|' +
                  rezervacija['odjava'].ljust(8)[:8] + '|' + rezervacija['status'].ljust(8)[:8] + '|' + rezervacija[
                      'ocenahotela'])


def print_soba(lista_soba):
    for soba in lista_soba:
        if soba != None:
            print(soba['IDsoba'].rjust(10) + '|' + soba['brojsobe'].ljust(20)[:10] + '|' + soba['brojkreveta'].ljust(8)[:8] + '|' + soba['tipsobe'].ljust(8)[:8] + '|' + soba['tv'].ljust(8)[:8] + '|' + soba['klima'] + '|' + soba['cena'])

def print_korisnika(l_korisnici):
    for korisnik in l_korisnici:
        if korisnik != None:
            print(korisnik['uloga'].rjust(16) + '|' +  korisnik['ime'].rjust(16) + '|' + korisnik['prezime'].ljust(16) + '|' + korisnik['username'].ljust(12) + '|' + korisnik[ 'telefon'].ljust(12) + '|' +korisnik['email'].ljust(20) + '|' +korisnik['IDhotela'])
if __name__ == "__main__":
    main()
