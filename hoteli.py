import hoteliIO

# prikaz svih hotela
def get_sorted_by_name():
    hoteli = hoteliIO.load_hoteli()
    return hoteli

hoteli1 = hoteliIO.load_hoteli()
# sortira pet najboljih
def sortiraj(l):
    
    for i in range(len(l)):
        indeks = i
        for j in range(i+1, len(l)):
            if l[indeks]['ocena']<l[j]['ocena']:
                indeks = j
        temp = l[i]
        l[i] = l[indeks]
        l[indeks]= temp
    return l

def filter_ime (ime):
    hoteli = hoteliIO.load_hoteli()
    ret_val = []
    for hotel in hoteli:
        if ime.lower() in hotel['ime'].lower():
            ret_val.append(hotel)
    return ret_val

def filter_adresa(adresa):
    hoteli = hoteliIO.load_hoteli()
    ret_val = []
    for hotel in hoteli:
        if adresa.lower() in hotel['adresa'].lower():
            ret_val.append(hotel)
    return ret_val

def filter_ocena(ocena):
    hoteli = hoteliIO.load_hoteli()
    ret_val = []
    for hotel in hoteli:
        if ocena in hotel['ocena']:
            ret_val.append(hotel)
    return ret_val

def visekrit_pretraga(ime, adresa, ocena):
    hoteli = hoteliIO.load_hoteli()
    ret_val = []
    for hotel in hoteli:
        if ime.lower() in hotel["ime"].lower():
            ret_val.append(hotel)
        if adresa.lower() in hotel["adresa"].lower():
            ret_val.append(hotel)
        if ocena in hotel["ocena"]:
            ret_val.append(hotel)
    return ret_val


def hoteli_heder():
    return \
        "\n Ime hotela         |Adresa              |restoran   |bazen   |ocena    |ID hotela \n" \
        "---------------------+--------------------+-----------+--------+---------+--------------="

def korisnici_heder():
    return \
        "\n Uloga        |Ime             |Prezime         |Username    |Telefon    |Email           |ID hotela     \n" \
        "----------------+----------------+----------------+------------+------------+-----------------+----------------="

def sobe_heder():
    return \
        "\n IDsoba        |Broj sobe        |Broj kreveta    |Tip sobe    |TV         |Klima        |Cena    \n" \
        "-----------------+-----------------+----------------+------------+-----------+-------------+----------------="

def rezervacije_heder():
    return \
        "\n Vreme kreiranja rezervacije |Datum prijave    |Datum odjave    |Korisnicko ime  |Stanje          |ocena \n" \
        "-----------------------------+-----------------+----------------+----------------+----------------+-------="