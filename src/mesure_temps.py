from image_transfert import *
import time
from tqdm import tqdm


def mesure_temps(n, method):
    x = [taille for taille in range(2, n, 10)]
    y = []
    for taille in tqdm(range(2, n, 10)):
        A = np.array([[[(i + j) % 255, (i + j) % 255, (i + j) % 255] for j in range(taille)] for i in range(taille)])
        t1 = time.time()
        modification_tableau_rs(erreur, A, taille, taille, method)
        t2 = time.time()-t1
        y.append(t2)
    return x, y


X0, Y1 = mesure_temps(100, decode.syndrome)
plt.plot(X0, Y1, label="Rapport des Complexités")
plt.xlabel("Coté du tableau (Unités)")
plt.ylabel("Temps d'execution (s)")
plt.legend()
plt.show()
