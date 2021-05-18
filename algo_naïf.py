from fonctions import *


def encrypt_naif(l):
    return l*3  # principe des tiroirs


def decrypt_naif(l):
    assert len(l) % 3 == 0
    d = []
    c = [1]*3  # nombre d'éléments en commun entre les trois parties du message
    for indice in range(3):
        d.append(l[k * indice:k * (indice + 1)])  # on découpe l en trois parties
    for ind_i in range(len(d)-2):
        for ind_j in range(ind_i+1, len(d)-1):
            if ind_j < len(d) and sont_egale(d[ind_i], d[ind_j]):  # on les compares deux à deux
                d.pop(ind_j)
                c[ind_i] += c.pop(ind_j)
    imax = c.index(max(c))
    return d[imax]
