from fonctions import *
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

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
        S.append(L[k:k+q])
    S.append(L[q*(n//q):]+[0]*(q-(n%q)))
    return S


def reverse_hexa(L):
    n = len(L)
    S = L[:]
    Q = []
    while len(S)>1:
        a=S.pop(0)
        b=S.pop(0)
        Q.append(b*16+a)
    return Q


def convert_l_t(L,n=256,p=256):
    S = L[:]
    if len(S)%3 != 0:
        raise ValueError
    else:
        return np.array(cut(S,3)).reshape(n,p)


A = convert(im)
print(A[0][:10])
B = cut(A[0])
print('nb d\'envoi pour R :', len(B))
C = [encrypt(i) for i in B]
D = [decrypt(i) for i in C]
D=liste_pleine(D)
R = reverse_hexa(D)
print(len(R))
'''E = liste_pleine(D)
F = reverse_hexa(E)
G = convert_l_t(F)
#plt.imshow(G)
plt.show()
'''
