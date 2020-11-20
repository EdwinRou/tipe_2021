from fonctions import *
import time
import random as rd

def liste_alea(N):
    L = []
    for i in range(N):
        l = []
        for i in range(k):
            l.append(rd.randint(0,15))
        L.append(l)
    return L

L = [encrypt(i) for i in liste_alea(1000)]
M = [encrypt_naif(i) for i in liste_alea(1000)]


def mesure_temps_calcul(f,L):
    t1 = time.time()
    for i in L:
        f(i)
    return time.time()-t1

R = mesure_temps_calcul(decrypt, L)
S = mesure_temps_calcul(decrypt_naif, M)

print('RS : ', R)
print('Naïf : ', S)

