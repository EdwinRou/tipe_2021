from fonctions import *
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import time
from tqdm import tqdm

#im = img.imread('Oeil.jpg')
im = img.imread('picasso.jpg')

def convert(tab): #retourne une liste dimension, tab
    R,G,B = [],[],[]
    #D=[] #la transmission de la dimension de tab est mise sous le tapis
    #D.append(hexa(np.shape(tab)[0])), L.append(hexa(np.shape(tab)[1]))
    for i in range(np.shape(tab)[0]):
        for j in range(np.shape(tab)[1]):
            for k in hexa(tab[i, j, 0]):
                R.append(k)
            for k in hexa(tab[i, j, 1]):
                G.append(k)
            for k in hexa(tab[i, j, 2]):
                B.append(k)
    return R,G,B


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


def cut(L,q=9): #décompose L en sous listes de taille q
    n =len(L)
    S = []
    for k in range(n//q):
        S.append(L[k*q:(k+1)*q])
    S.append(L[q*(n//q):]+[0]*(q-(n%q)))
    return S


def reverse_hexa(L):
    n = len(L)
    S = L[:]
    Q = []
    while len(S)>1:
        a=S.pop(0)
        b=S.pop(0)
        Q.append(a*16+b)
    return Q


def convert_l_t(R, G, B,n=256,p=256):
    R_p, G_p, B_p = R[:], G[:], B[:]
    image = []
    for j in range(p):
        for i in range(n):
            image.append([R.pop(0),G.pop(0), B.pop(0)])
    image.reshape(n,p)
    return image


A = convert(im)
print("Les 9 premiers elements de la composante Rouge (hexa) : \n", A[0][:9])
B = cut(A[0])
print('nombre d\'envoi pour la composante Rouge :\n', len(B))
C = [encrypt(i) for i in B]
print("Premier élément encrypté : \n", C[0])
D = [decrypt(i) for i in C]
print("Premier élément décrypté :\n", D[0])
D=liste_pleine(D)
R = reverse_hexa(D)
print(R[:9])
print("nombre d\'éléments reçu :\n ",len(R))
print(R[-9:])
#G = convert_l_t(R,R,R)
#plt.imshow(G)
#plt.show()

