from fonctions import *
import random as rd
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
# import time
from tqdm import tqdm

im = img.imread('image.jpg')


def convert(tab):  # retourne trois listes correspondant aux composantes RGB
    comp_r, comp_g, comp_b = [], [], []
    # D=[] # la transmission de la dimension de tab est mise sous le tapis
    # D.append(hexa(np.shape(tab)[0])), L.append(hexa(np.shape(tab)[1]))
    for ligne_i in range(np.shape(tab)[0]):
        for colonne_j in range(np.shape(tab)[1]):
            for indice in hexa(tab[ligne_i, colonne_j, 0]):
                comp_r.append(indice)
            for indice in hexa(tab[ligne_i, colonne_j, 1]):
                comp_g.append(indice)
            for indice in hexa(tab[ligne_i, colonne_j, 2]):
                comp_b.append(indice)
    return comp_r, comp_g, comp_b

def hexa(nombre: int) -> list:  # décomposition hexa de n sous forme [x,y] pour des nb<256
    if nombre > 255:
        raise ValueError
    return [nombre // 16, nombre % 16]

def liste_pleine(liste: list) -> list:
    m = liste.copy()
    if type(m[0]) != list:
        return m
    else:
        res =[]
        for o in range(len(m)):
            for t in range(len(m[o])):
                res.append(m[o][t])
        return liste_pleine(res)

def cut(liste, taille=9):  # décompose L en sous listes de taille q
    taille_liste = len(liste)
    s = []
    for k in range(taille_liste // taille):
        s.append(liste[k * taille:(k + 1) * taille])
    s.append(liste[taille * (taille_liste // taille):] + [0] * (taille - (taille_liste % taille)))
    return s

def reverse_hexa(L):
    n = len(L)
    S = L[:]
    Q = []
    while len(S) > 1:
        a = S.pop(0)
        b = S.pop(0)
        Q.append(a*16+b)
    return Q

def convert_l_t(R, G, B, n=5, p=5):
    R_p, G_p, B_p = R[:], G[:], B[:]
    image = []
    for j in range(p):
        l = []
        for i in range(n):
            l.append([R_p.pop(0),G_p.pop(0), B_p.pop(0)])
        image.append(l)
    image = np.array(image)
    return image

def modification_tableau_rs(f,im): # applique aux pixel du tableau im la fonction f
    A = convert(im)
    R, G, B = cut(A[0]), cut(A[1]), cut(A[2])
    R, G, B = f([encrypt(i) for i in R]), f([encrypt(i) for i in G]), f([encrypt(i) for i in B])
    R, G, B = [decrypt(i) for i in tqdm(R)], [decrypt(i) for i in tqdm(G)], [decrypt(i) for i in tqdm(B)]
    R, G, B = liste_pleine(R), liste_pleine(G), liste_pleine(B)
    R, G, B = reverse_hexa(R), reverse_hexa(G), reverse_hexa(B)
    return convert_l_t(R, G, B)

def modification_tableau(f , im):
    A = convert(im)
    R, G, B = f(cut(A[0])), f(cut(A[1])), f(cut(A[2]))
    R, G, B = liste_pleine(R), liste_pleine(G), liste_pleine(B)
    return convert_l_t(R, G, B)

def erreur(l: list, n=3) -> list:
    for t in range(n):
        l[t]=rd.randrange(0,16)
    return l

def main():

    G = modification_tableau_rs(erreur, im)  # ne fait aucune modif
    # G = modification_tableau(erreur, im)
    plt.imshow(G)
    plt.show()

main()
