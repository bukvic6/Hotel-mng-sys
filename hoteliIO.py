def line_to_hotel(line):
    line_l = line.strip().split('|')
    user = {'id':line_l[0], 'ime':line_l[1], 'adresa':line_l[2], 'restoran':line_l[3], 'bazen':line_l[4], 'ocena':line_l[5], 'idsobe': line_l[6:]}
    return user


def load_hoteli():
    f_in = open('hoteli.txt', 'r')
    ret_val = []
    for line in f_in.readlines():
        ret_val.append(line_to_hotel(line))
    return ret_val
    

# citanje iz fajla HOTELI