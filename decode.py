from fonctions import *


def syndrome(message):
    assert (n-k) % 2 == 0  # MDS
    s = H.LeftMulColumnVec(message)
    if sont_egale(s, [0]*(n-k)):
        return message
    S_ext = pfmat.GenericMatrix((l_1, l_1+1), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
    for i in range(l_1):
        ligne = []
        for j in range(l_1+1):
            ligne.append(s[i+j])
        S_ext.SetRow(i, ligne)
        u = S_ext.LUP()[1]  # décomposition en matrices triangulaires pour extraire un élément non trivial du noyau
        """
        récupération du noyau grâce au pivot de Gauss
        """
        b = [X[1]]  # on fixe un élément pour obtenir un systeme de Cauchy
        taille = l_1 + 1
        for i in range(1, taille):
            a = 0
            for j in range(1, len(b) + 1):
                a = F.Add(a, F.Multiply(u[taille - i - 1, taille - j], b[-j]))
            if a == 0:
                b = [a] + b
            else:
                a = F.Divide(a, u[taille - i - 1, taille - i - 1])
                b = [a] + b
    indice = []
    b.reverse()
    for i in range(0, 16):  # on test pour chaque élément non nul du corps
        evaluation_q1 = 0
        for l in range(l_1+1):  # pour chaque monome
            e = evaluation_q1
            evaluation_q1 = F.Add(e, F.Multiply(b[l], puissance(X[i], l_1-l)))
        if evaluation_q1 == 0:
            indice.append(i-1)
    t = len(indice)
    H_ext = pfmat.GenericMatrix((t, t), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
    for m in range(t):
        ligne = []
        for l in range(t):
            ligne.append(puissance(X[indice[l]+1], m+1))
        H_ext.SetRow(m, ligne)
    S_sol = [s[i] for i in range(t)]
    I = H_ext.Solve(S_sol)
    E = [0]*15
    for i in range(len(S_sol)):
        E[indice[i]] = I[i]
    C = [F.Add(message[i], E[i]) for i in range(15)]
    return G_inverse.LeftMulColumnVec(C[:9])

def polynomes(message):
    """
    définition de M à partir du message reçu
    """
    m = pfmat.GenericMatrix((n, l_0 + l_1 + 2), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
    for indice in range(1, n+1):
        ligne = []
        for j in range(l_0 + 1):
            ligne.append(puissance(X[indice], j))
        for k in range(l_1 + 1):
            ligne.append(F.Multiply(message[indice-1], puissance(X[indice], k)))
        m.SetRow(indice-1, ligne)
    u = m.LUP()[1]  # décomposition en matrices triangulaires pour extraire un élément non trivial du noyau
    """
    récupération du noyau grâce au pivot de Gauss
    """
    q = [X[1]] # on fixe un élément pour obtenir un systeme de Cauchy
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
    q_1 = q[l_0 + 1:] # définition de Q1
    q_0 = q[:(len(q) - (l_1 + 1))] # définition de Q0
    return div_euclid(q_0, q_1)[0]  # le message initialement envoyé