import pyfinite.ffield as pffield
import pyfinite.genericmatrix as pfmat
from random import randint

p = 4
q = 2 ** p
n = q - 1
F = pffield.FField(p)
a = 2
k = 9
t = (n - k) // 2
l_0 = n - 1 - t
l_1 = n - k - t
nombreerreur=3


def puissance(x, puiss):  # Définition de la puissance dans le corps F16
    c = 1
    for compteur in range(puiss):
        c = F.Multiply(c, x)
    return c


def deg(polynome):  # retourn le degré du polynome
    if simple(polynome) == [0]:
        return -1  # Si le polynome est le polynome nul, on pose que son degré est -1
    else:
        return len(simple(polynome)) - 1  # Retourne la valeur de la puissance de X après laquelle
        # tous les coefficients sont nuls


def simple(poly: list) -> list:
    while len(poly) > 1:  # Tant que le polynome n'est pas une constante
        if poly[-1] == 0:
            poly.pop()  # On le retire le terme de plus haut degré s'il est nul
        else:
            return poly
    return poly


def diveu(poly_a: list, poly_b: list):  # division euclidienne de a par b
    if deg(poly_b) == 0:  # On ne divise pas par 0 !
        return []
    elif deg(poly_b) > deg(poly_a):  # La division d'un polynome par un polynome de degré supérieur est nulle
        return [0], poly_a
    else:
        b = [0] * (deg(poly_a) - deg(poly_b) + 1)  # Création du polynôme quotient dont
        # le degré maximal est deg Pa - deg Pb
        while deg(poly_a) >= deg(poly_b):  # Condition sur le reste dans la DE
            coefficient = F.Divide(poly_a[-1], poly_b[-1])
            c = [0] * (deg(poly_a) - deg(poly_b)) + simple(poly_b)
            # Crée un polynôme égale à Pb multiplié par X à la puissance deg Pa - deg Pb
            b[deg(poly_a) - deg(poly_b)] = coefficient  # Ajoute au quotient X à la puissance deg P - deg Q
            for index in range(len(c)):
                c[index] = F.Multiply(c[index], coefficient)
            for index in range(len(poly_a)):
                poly_a[index] = F.Add(poly_a[index], c[index])
            simple(poly_a)
        return simple(b), simple(poly_a)  # Simple b est le quotient tandis que #simple(poly_a) est le reste


def adn(x, y):  # definition de la fonction addition pour le calcul matriciel
    return F.Add(x, y)


def multn(x, y):  # definition de la fonction multiplication pour le calcul matriciel
    return F.Multiply(x, y)


def divn(x, y):  # definition de la fonction division pour le calcul matriciel
    if x == 0:
        return 0
    else:
        return F.Divide(x, y)


X = [0]  # Liste des Xi
for i in range(2, n + 2):
    X.append(puissance(a, i - 2))

G = pfmat.GenericMatrix((n, k), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
for i in range(1, n + 1):
    ligne = []
    for j in range(0, k):
        ligne.append(puissance(X[i], j))
    G.SetRow(i - 1, ligne)

H = pfmat.GenericMatrix((n - k, n), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
for i in range(n - k):
    ligne = []
    for j in range(n):
        ligne.append(puissance(X[j + 1], i + 1))
    H.SetRow(i, ligne)


def encrypt(u):
    c = G.LeftMulColumnVec(u)
    return c


def decrypt(message):
    m = pfmat.GenericMatrix((n, l_0 + l_1 + 2), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
    for indice in range(1, n+1):
        ligne = []
        for j in range(l_0 + 1):
            ligne.append(puissance(X[indice], j))
        for k in range(l_1 + 1):
            ligne.append(F.Multiply(message[indice-1], puissance(X[indice], k)))
        m.SetRow(indice-1, ligne)

    u = m.LUP()[1]

    q = [X[1]]
    taille = l_0 + l_1 + 2
    for i in range(1, taille):
        a = 0
        for j in range(1, len(q) + 1):
            a = F.Add(a, F.Multiply(u[taille - i - 1, taille - j], q[-j]))
        if a == 0:
            q = [a] + q
        else:
            a = F.Divide(a, u[taille - i - 1, taille - i - 1])
            q = [a] + q

    q_1 = q[l_0 + 1:]
    q_0 = q[:(len(q) - (l_1 + 1))]
    return diveu(q_0, q_1)[0]

def sont_egale(L,M): # test l'égalité de deux listes
    if len(M) != len(L):
        return False
    else:
        for i in range(len(L)):
             if L[i] != M[i]:
                 return False
    return True

def encrypt_naif(L):
    return L*(2*nombreerreur + 1) # principe des tiroirs

def decrypt_naif(L):
    n = len(L)
    D = []
    c = [1]*(2*nombreerreur+1)
    for i in range(2*nombreerreur+1):
        D.append(L[k*i:k*(i+1)])
    for i in range(len(D)-2):
        for j in range(i+1, len(D)-1):
            if j<len(D) and sont_egale(D[i],D[j]):
                D.pop(j)
                c[i]+=c.pop(j)
    imax = c.index(max(c))
    return D[imax]


def erreur(L):
    for i in range(nombreerreur):
        position=randint(0,len(L)-1)
        erreur=randint(0,16)
        L[position]=erreur
    return L
