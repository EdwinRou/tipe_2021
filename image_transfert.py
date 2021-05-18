from fonctions import *
import random as rd
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import decrypt_rs


im = img.imread('Images/image.jpg')
height, width, enc = im.shape


def hexa(nombre: int) -> list:  # décomposition hexa de n sous forme [x,y] pour des nb<256
    if nombre > 255:
        raise ValueError
    return [nombre // 16, nombre % 16]


def convert(tab, syst=hexa):  # retourne trois listes correspondant aux composantes RGB
    comp_r, comp_g, comp_b = [], [], []
    for ligne_i in range(np.shape(tab)[0]):
        for colonne_j in range(np.shape(tab)[1]):
            for indice in syst(tab[ligne_i, colonne_j, 0]):
                comp_r.append(indice)
            for indice in syst(tab[ligne_i, colonne_j, 1]):
                comp_g.append(indice)
            for indice in syst(tab[ligne_i, colonne_j, 2]):
                comp_b.append(indice)
    return comp_r, comp_g, comp_b


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
    S = L[:]
    Q = []
    while len(S) > 1:
        a = S.pop(0)
        b = S.pop(0)
        Q.append(a*16+b)
    return Q


def convert_l_t(R, G, B, w=width, h=height):
    R_p, G_p, B_p = R[:], G[:], B[:]
    R_p.reverse(), G_p.reverse(), B_p.reverse()
    image = [[[R_p.pop(), G_p.pop(), B_p.pop()]for i in range(w-1)] for j in range(h-1)]
    image = np.array(image)
    return image


def modification_tableau_rs(f, im, w=width, h=height): # applique aux pixel du tableau im la fonction f
    A = convert(im)
    R = map(f, [encrypt(i) for i in cut(A[0])])
    G = map(f, [encrypt(i) for i in cut(A[1])])
    B = map(f, [encrypt(i) for i in cut(A[2])])
    R, G, B = [decrypt_rs.polynomes(i) for i in R], [decrypt_rs.polynomes(i) for i in G], [decrypt_rs.polynomes(i) for i in B]
    R, G, B = reverse_hexa(liste_pleine(R)), reverse_hexa(liste_pleine(G)), reverse_hexa(liste_pleine(B))
    return convert_l_t(R, G, B, w, h)


def modification_tableau(f , im):
    A = convert(im, id_n)
    R, G, B = cut(A[0]), cut(A[1]), cut(A[2])
    R, G, B = [f(i) for i in R], [f(i) for i in G], [f(i) for i in B]
    R, G, B = liste_pleine(R), liste_pleine(G), liste_pleine(B)
    return convert_l_t(R, G, B)


def erreur(l: list,r=16, n=3) -> list:
    taille = len(l)
    for t in range(n):
        rdm = rd.randrange(0,taille)
        l[rdm] = rd.randrange(0,r)
    return l


def main():
    G_rs = modification_tableau_rs(erreur, im)
    G = modification_tableau(lambda liste: erreur(liste, 255), im)
    fig = plt.figure()

    fig.add_subplot(1,2,1)
    plt.imshow(G)
    plt.title("Sans Reed-Solomon")
    plt.axis("off")

    fig.add_subplot(1,2,2)
    plt.imshow(G_rs)
    plt.title("Avec Reed-Solomon")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


#main()
# profiling with snakeviz
