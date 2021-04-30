from fonctions import *
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
# import time
from tqdm import tqdm

im = img.imread('picasso.jpg')


def convert(tab):  # retourne trois listes correspondant aux composantes RGB
    R, G, B = [], [], []
    # D=[] # la transmission de la dimension de tab est mise sous le tapis
    # D.append(hexa(np.shape(tab)[0])), L.append(hexa(np.shape(tab)[1]))
    for i in range(np.shape(tab)[0]):
        for j in range(np.shape(tab)[1]):
            for k in hexa(tab[i, j, 0]):
                R.append(k)
            for k in hexa(tab[i, j, 1]):
                G.append(k)
            for k in hexa(tab[i, j, 2]):
                B.append(k)
    return R, G, B


def hexa(n): # décomposition hexa de n sous forme [x,y] pour des nb<256
    if n > 255 :
        raise ValueError
    return [n//16, n%16]


def liste_pleine(L):
    M=[]
    for i in range(len(L)):
        for j in L[i]:
            M.append(j)
    return M


def cut(L,q=9):  # décompose L en sous listes de taille q
    n = len(L)
    S = []
    for k in range(n//q):
        S.append(L[k*q:(k+1)*q])
    S.append(L[q*(n//q):]+[0]*(q-(n%q)))
    return S


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

def modification_tableau(f,im): # applique aux pixel du tableau im la fonction f
    A = convert(im)
    R, G, B = cut(A[0]), cut(A[1]), cut(A[2])
    R, G, B = f([encrypt(i) for i in R]), f([encrypt(i) for i in G]), f([encrypt(i) for i in B])
    R, G, B = [decrypt(i) for i in tqdm(R)], [decrypt(i) for i in tqdm(G)], [decrypt(i) for i in tqdm(B)]
    R, G, B = liste_pleine(R), liste_pleine(G), liste_pleine(B)
    R, G, B = reverse_hexa(R), reverse_hexa(G), reverse_hexa(B)
    return convert_l_t(R, G, B)

def id(l: list) -> list : # identité des listes
    return l
G = modification_tableau(id, im) # ne fait aucune modif
plt.imshow(G)
plt.show()
