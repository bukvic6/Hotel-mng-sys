import korisniciIO



def filter_recepcionera_po_imenu(ime):
    korisnici = korisniciIO.load_korisnici()
    ret_val = []
    for korisnik in korisnici:
        if ime in korisnik['ime']:
            ret_val.append(korisnik)
    return ret_val

def filter_recepcionera_po_prezimenu(prezime):
    korisnici = korisniciIO.load_korisnici()
    ret_val = []
    for korisnik in korisnici:
        if prezime in korisnik['prezime']:
            ret_val.append(korisnik)
    return ret_val

def filter_recepcionera_po_username(username):
    korisnici = korisniciIO.load_korisnici()
    ret_val = []
    for korisnik in korisnici:
        if username in korisnik['username']:
            ret_val.append(korisnik)
    return ret_val
def filter_recepcionera_po_ulozi():
    korisnici = korisniciIO.load_korisnici()
    ret_val = []
    for korisnik in korisnici:
        if korisnik['uloga'] == 'recepcioner':
            ret_val.append(korisnik)
    return ret_val

def visekrit_pretraga(ime, prezime, username, email):
    korisnici = korisniciIO.load_korisnici()
    ret_val = []
    for korisnik in korisnici:
        if ime.lower() in korisnik["ime"].lower():
            ret_val.append(korisnik)
        if prezime.lower() in korisnik["prezime"].lower():
            ret_val.append(korisnik)
        if username.lower() in korisnik["username"].lower():
            ret_val.append(korisnik)
        if email.lower() in korisnik["email"].lower():
            ret_val.append(korisnik)
    return ret_val