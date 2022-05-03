
# citanje iz fajla za SOBE

def line_to_soba(line):
    line_l = line.strip().split('|')
    user = { 'IDsoba':line_l[0], 'brojsobe':line_l[1], 'brojkreveta':line_l[2], 'tipsobe':line_l[3], 'tv':line_l[4],'klima':line_l[5], 'cena':line_l[6]}
    return user


def load_soba():
    f_in = open('sobe.txt', 'r')
    ret_val = []
    for line in f_in.readlines():
        ret_val.append(line_to_soba(line))
    return ret_val

# citanje iz fajla za REZERVACIJE

def line_to_rezervacija(line):
    line_l = line.strip().split('|')
    user = {'IDrezervacija':line_l[0], 'vremekreiranja':line_l[1], 'prijava':line_l[2], 'odjava':line_l[3], 'korisnickoime':line_l[4], 'status':line_l[5],'ocenahotela':line_l[6], 'sobe':line_l[7:]}
    return user


def load_rezervacija():
    f_in = open('rezervacije.txt', 'r')
    ret_val = []
    for line in f_in.readlines():
        ret_val.append(line_to_rezervacija(line))
    return ret_val
# citanje iz fajla za hotele

