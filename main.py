from src.fonctions import erreur, k, G, multiply, add, diveu
from src.decode import polynomes, syndrome
from src.image_transfert import modification_tableau_rs
import matplotlib.image as img
import matplotlib.pyplot as plt


def main():
    B = [1,2,3]
    Q = [3,4]
    R = [5]
    A = add(R, multiply(B,Q))
    print(diveu(A,B))
    
    #A = [i for i in range(9)]
    #B = G.LeftMulColumnVec(A)
    #print(A)
    #C = polynomes(B)
    #print(C)
    #D = erreur(B)
    #E = syndrome(D)
    #print(E)
    #im = img.imread('static/joconde.jpg')
    #height, width, enc = im.shape
    #G_rs = modification_tableau_rs(erreur, im, width, height, polynomes)
    
    #fig = plt.figure()
    #fig.add_subplot(1, 2, 1)
    #plt.imshow(G)
    #plt.title("Sans Reed-Solomon")
    #plt.axis("off")

    #fig.add_subplot(1, 2, 2)
    #plt.imshow(G_rs)
    #plt.title("Avec Reed-Solomon")
    #plt.axis("off")

    #plt.tight_layout()
    #plt.show()


if __name__ == '__main__':
    main()
else :
    print("name of the module :", __name__)
