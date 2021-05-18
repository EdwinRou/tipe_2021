from fonctions import *


def encrypt_naif(L):
    return L*3 # principe des tiroirs


def decrypt_naif(L):
    n = len(L)
    D = []
    c = [1]*(3) # nombre d'éléments en commun entre les trois parties du message
    for i in range(3):
        D.append(L[k*i:k*(i+1)])# on découpe L en trois parties
    for i in range(len(D)-2):
        for j in range(i+1, len(D)-1):
            if j<len(D) and sont_egale(D[i],D[j]):# on les compares deux à deux
                D.pop(j)
                c[i]+=c.pop(j)
    imax = c.index(max(c))
    return D[imax]
