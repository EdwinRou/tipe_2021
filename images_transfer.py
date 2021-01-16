from fonctions import *
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

# im = img.imread('Oeil.jpg')
im = img.imread('tournesol.jpg')

def convert_t_l(tab): #retourne une liste [shape[0], shape[1], L]
    L = []
    L.append(hexa(np.shape(tab)[0])[0]), L.append(hexa(np.shape(tab)[0])[1]), L.append(hexa(np.shape(tab)[1])[0]),L.append(hexa(np.shape(tab)[1])[1])
    for i in range(np.shape(tab)[0]):
        for j in range(np.shape(tab)[1]):
            for nb in tab[i][j]:
                for s in hexa(nb):
                    L.append(s)
    return L

        
def hexa(n):
    if n > 255 :
        raise ValueError
    return [n//16, n%16]

def cut(L,q):
    n =len(L)
    S = []
    for k in range(n//q):
        S.append(L[k:k+q])
    S.append(L[q*(n//q):]+[0]*(q-(n%q)))
    return S

def liste_pleine(L):
    S = []
    for i in range(len(L)):
        for j in range(len(L[i])):
            S.append(L[i][j])
    return S

def convert_l_t(L):
    S = L[:]
    n = S.pop(0)
    p= S.pop(0)
    if len(S)%3 != 0:
        raise ValueError
    else:
        return np.array(cut(S,3)).reshape(n,p)

def reverse_hexa(L):
    n = len(L)
    S = L[:]
    Q = []
    while len(S)>1:
        a=S.pop(0)
        b=S.pop(0)
        Q.append(a*16+b)
    return Q

#A = convert_t_l(im)
#B = cut(A,9)
#C = [encrypt(i) for i in B]
#D = [decrypt(i) for i in C]
#E = liste_pleine(D)
#F = reverse_hexa(E)
#G = convert_l_t(F)
#plt.imshow(G)
#plt.show()
