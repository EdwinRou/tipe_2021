import matplotlib.pyplot as plt
import numpy as np
from image_transfert import *
import time
from tqdm import tqdm


def mesure_temps(n):
    X = [taille for taille in range(2, n, 10)]
    Y = []
    for taille in tqdm(range(2, n, 10)):
        A = np.array([[[i + j, i + j, i + j] for j in range(taille)] for i in range(taille)])
        t1 = time.time()
        modification_tableau_rs(erreur, A, taille, taille)
        t2 = time.time()-t1
        Y.append(t2)
    return X, Y


X0, Y0 = mesure_temps(100)
plt.plot(X0, Y0, label="R-S Polynômes")
# plt.plot(X0, [i for i in X0], label="x")
plt.xlabel("Coté du tableau (Unités)")
plt.ylabel("Temps d'execution (s)")
plt.legend()
plt.show()
