import matplotlib.pyplot as plt
import numpy as np
from image_transfert import *
import time
from tqdm import tqdm


def mesure_temps(n, method):
    X = [taille for taille in range(2, n, 10)]
    Y = []
    for taille in tqdm(range(2, n, 10)):
        A = np.array([[[(i + j)%255, (i + j)%255, (i + j)%255] for j in range(taille)] for i in range(taille)])
        t1 = time.time()
        modification_tableau_rs(erreur, A, taille, taille, method)
        t2 = time.time()-t1
        Y.append(t2)
    return X, Y


X0, Y0 = mesure_temps(100, decode.polynomes)
X0, Y1 = mesure_temps(100, decode.syndrome)
Y2 = [Y0[i]/Y1[i] for i in range(len(Y1))]
plt.plot(X0,Y2, label="Rapport des Complexités")
plt.xlabel("Coté du tableau (Unités)")
plt.ylabel("Temps d'execution (s)")
plt.legend()
plt.show()
