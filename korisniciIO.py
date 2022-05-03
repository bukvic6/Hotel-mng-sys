

def line_to_korisnik(line):
    line_l = line.strip().split('|')
    user = {'uloga':line_l[0], 'ime':line_l[1], 'prezime':line_l[2], 'username':line_l[3], 'password':line_l[4], 'telefon':line_l[5], 'email':line_l[6]}
    if user['uloga'] == "recepcioner":
        user["IDhotela"] = line_l[7]
    if user['uloga'] == "korisnik":
        user["rezervacije"] = line_l[7:]
    return user


def load_korisnici():
    f_in = open('korisnici.txt', 'r')
    ret_val = []
    for line in f_in.readlines():
        ret_val.append(line_to_korisnik(line))
    return ret_val









