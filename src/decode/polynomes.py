import sys
sys.path.append("..")
from src.fonctions import pfmat, n, l_0, l_1, adn, multn, divn, puissance, X, F, diveu

def polynomes(message : list)->list:
    """decode message using polynomial method

    Args:
        message (list): message to decode

    Returns:
        list: message decoded
    """
    #définition de M à partir du message reçu
    m = pfmat.GenericMatrix((n, l_0 + l_1 + 2), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
    for indice in range(1, n+1):
        ligne = []
        for j in range(l_0 + 1):
            ligne.append(puissance(X[indice], j))
        for k in range(l_1 + 1):
            ligne.append(F.Multiply(message[indice-1], puissance(X[indice], k)))
        m.SetRow(indice-1, ligne)
    u = m.LUP()[1]  # décomposition en matrices triangulaires pour extraire un élément non trivial du noyau
    #récupération du noyau grâce au pivot de Gauss
    q = [X[1]]  # on fixe un élément pour obtenir un systeme de Cauchy
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
    q_1 = q[l_0 + 1:]  # définition de Q1
    q_0 = q[:(len(q) - (l_1 + 1))]  # définition de Q0
    return div_euclid(q_0, q_1)[0]  # le message initialement envoyé
