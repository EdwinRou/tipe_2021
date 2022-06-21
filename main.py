from src.fonctions import k, G
from src.decode import polynomes, syndrome

def main():
    message = [i for i in range(k)]
    print(G.LeftMulColumnVec(message))

if __name__ == '__main__':
    main()
else :
    print("run.py is not the main file")
