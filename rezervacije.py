import dataIO
import hoteliIO

lista_rezervacija = dataIO.load_rezervacija()
lista_hotela = hoteliIO.load_hoteli()


def dodajRezervaciju(rezervacija):
    lista_rezervacija.append(rezervacija)
    return True

def rezervacija2Str(r):
    s = r['IDrezervacija'] + '|' + r['vremekreiranja'] + '|' + r['prijava'] + '|' + r['odjava'] + '|' + r['korisnickoime'] + '|'  + r['status'] + '|' + r['ocenahotela']
    for sob in r["sobe"]:
        s += '|' + sob
    return s

def snimi(nazivfajla):
    target = open(nazivfajla, "w")
    for rez in lista_rezervacija:
        target.write(rezervacija2Str(rez) + '\n')
    target.close()

# DODAVANJE HOTELA ADMINISTRATOR

# def dodaj_hotel(s):
#     lista_hotela.append(s)
#     return True

# # def hotel2str(h):
# #     s = h['id'] + '|' + h ['ime'] + '|' + h['adresa'] + '|' + h['restoran'] + '|' + h['bazen'] + '|' + h['ocena'] + '|' + h['idsobe']
# #     return s
# def snimihotel(nazivfajla):
#     target = open(nazivfajla, 'a')

#     target.close


