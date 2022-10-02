"""
Import des bibliothèques relatives au coprs F16
"""
import pyfinite.ffield as pffield
import pyfinite.genericmatrix as pfmat
import random as rd


"""
Définition des paramètres du cadre d'étude :
"""
q = 2 ** 4  # nombre d'éléments de F16 => 16
n = q - 1  # en python on compte à partir de 0
F = pffield.FField(4)  # F est le coprs F16
a = 2  # élément primitif ie X
k = 9  # taille du message envoyé choisi de sorte que l'on autorise 3 erreurs)
nombreerreur = (n - k) // 2
l_0 = n - 1 - nombreerreur  # degré d'un polynome Q0
l_1 = n - k - nombreerreur  # degré d'un polynome Q1
    
def puissance(x, puiss)->int:
    """retourne x à la puissance puiss dans le corps

    Args:
        x (int): élément du corps
        puiss (int): nombre entier

    Returns:
        int: x^puiss
    """
    c = 1
    for compteur in range(puiss):
        c = F.Multiply(c, x)
    return c


def deg(polynome)->int:
    """retourne le degré du polynome

    Args:
        polynome (list): ploynome du corps

    Returns:
        int: degré du polynome
    """
    polynome = simple(polynome)
    if polynome == [0]:
        return -1  # Si le polynome est le polynome nul, on pose que son degré est -1
    else:
        return len(polynome)-1  # Retourne la valeur de la puissance de X après laquelle
        # tous les coefficients sont nuls


def simple(poly: list) -> list:
    """retire les 0 inutiles en tête du polynome

    Args:
        poly (list): polynome dont le surplus de 0 est à enlever

    Returns:
        list: polynome sans 0 en tête
    """
    while len(poly) > 1:  # Tant que le polynome n'est pas une constante
        if poly[-1] == 0:
            poly.pop()  # On le retire le terme de plus haut degré s'il est nul
        else:
            return poly
    return poly

def add(X : list,Y : list) -> list:
    assert len(X) != 0 and len(Y) != 0
    X,Y = simple(X), simple(Y)
    M, m = max(deg(X), deg(Y)), min(deg(X), deg(Y))
    M+=1
    m+=1
    r =[F.Add(X[k], Y[k]) for k in range(m)]
    if deg(X) < deg(Y): #ie deg(Y) is greater
        return r + [Y[k] for k in range(m, deg(Y)+1)]
    else:
        return r + [X[k] for k in range(m, deg(X)+1)]
        
def multiply(X,Y):
    X, Y = simple(X), simple(Y)
    Somme = []
    for s in range(deg(X)+deg(Y)+1):
        monome = 0
        for k in range(s+1):
            try:
                monome = F.Add(F.Multiply(X[k], Y[s-k]),monome)
            except IndexError:
                pass
        Somme.append(monome)
    return Somme

def diveu(Pa : list, Pb: list) -> list :
    """
    retourne la division euclidienne du polynome Pa par le polynome Pb

    Args:
        Pa (list): dividende
        Pb (list): diviseur

    Raises:
        ZeroDivisionError: pas de division par 0

    Returns:
        list: Quotient,Reste
    """
    poly_a, poly_b = Pa.copy(), Pb.copy()
    da, db = deg(poly_a), deg(poly_b)
    if db == -1:  # On ne divise pas par 0 !
        raise ZeroDivisionError
    elif db > da:  # La division d'un polynome par un polynome de degré supérieur est nulle
        return [0], poly_a
    else:
        Q = [0]
        R = poly_a
        while deg(R) >= deg(poly_b):
            Q = add(Q,[0]*(deg(R)-deg(poly_b)) + [F.Divide(R[-1],poly_b[-1])])
            R = add(R,multiply(Q,poly_b))
        return(simple(Q),simple(R))
            
def adn(x, y):  # definition de la fonction addition pour le calcul matriciel
    return F.Add(x, y)


def multn(x, y):  # definition de la fonction multiplication pour le calcul matriciel
    return F.Multiply(x, y)


def divn(x, y):  # definition de la fonction division pour le calcul matriciel
    if x == 0:
        return 0
    else:
        return F.Divide(x, y)


"""
Définition des éléments algébriques
"""

X = [0]  # Liste des Xi
for i in range(2, n + 2):
    X.append(puissance(a, i - 2))

G = pfmat.GenericMatrix((n, k), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
for i in range(1, n + 1):
    ligne = []
    for j in range(0, k):
        ligne.append(puissance(X[i], j))
    G.SetRow(i - 1, ligne)

G_tronquee = pfmat.GenericMatrix((k, k), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
for i in range(1, k + 1):
    ligne = []
    for j in range(0, k):
        ligne.append(puissance(X[i], j))
    G_tronquee.SetRow(i - 1, ligne)

G_inverse = G_tronquee.Inverse()

H = pfmat.GenericMatrix((n - k, n), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
for i in range(n - k):
    ligne = []
    for j in range(n):
        ligne.append(puissance(X[j + 1], i + 1))
    H.SetRow(i, ligne)

K = pfmat.GenericMatrix((l_1, n), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
for i in range(l_1):
    ligne = []
    for j in range(n):
        ligne.append(puissance(X[j+1], i + 1))
    K.SetRow(i, ligne)

"""
définition des fonctions qui opèrent sur les listes
"""


def id_l(l: list) -> list:  # identité des listes
    return l


def id_n(n) -> list:  # utile pour convert sans système hexa
    return [n]


def sont_egale(L: list, M: list) -> bool:  # test l'égalité de deux listes
    if len(M) != len(L):
        return False
    else:
        for i in range(len(L)):
            if L[i] != M[i]:
                return False
    return True


"""
Définition des fonctions de Reed-Solomon
"""


def encode(u):
    c = G.LeftMulColumnVec(u)
    return c


def erreur(l: list, r=16, n=3) -> list:
    li = l.copy()
    taille = len(li)
    for t in range(n):
        rdm = rd.randrange(0, taille)
        li[rdm] = rd.randrange(0, r)
    return li
