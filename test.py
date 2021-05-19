from fonctions import *
import decrypt_rs
import time

U = [i for i in range(9)]
U = encrypt(U)
V = erreur(U)
print(decrypt_rs.syndrome(V))

