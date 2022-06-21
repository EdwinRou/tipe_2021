from src.fonctions import erreur, k, G, erreur
from src.decode import polynomes, syndrome
from src.image_transfert import modification_tableau_rs
import matplotlib.image as img
import matplotlib.pyplot as plt


def main():
    im = img.imread('static/joconde.jpg')
    height, width, enc = im.shape
    G_rs = modification_tableau_rs(erreur, im, width, height, polynomes)
    
    fig = plt.figure()
    fig.add_subplot(1, 2, 1)
    plt.imshow(G)
    plt.title("Sans Reed-Solomon")
    plt.axis("off")

    fig.add_subplot(1, 2, 2)
    plt.imshow(G_rs)
    plt.title("Avec Reed-Solomon")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
else :
    print("run.py is not the main file")
