from fonctions import *
import decrypt_rs

U = [i for i in range(9)]
U = encrypt(U)
V = erreur(U)
print("U : ", U)
print("V : ", V)
print(decrypt_rs.syndrome(V))
print("X :", X)
#print(H)
