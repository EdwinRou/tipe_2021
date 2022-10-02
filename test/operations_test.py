import sys
sys.path.append("..")
from src.fonctions import simple, F, deg, multiply, add, diveu
import unittest
import random as rd


class Test_operations(unittest.TestCase):
        
    def test_add(self):
        X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(add(X,X), [0 for _ in range(16)])
        self.assertEqual(add([9,4,10],[3]),[10,4,10])

    def test_multiply(self):
        X, Y = [1, 7], [3]
        self.assertEqual([3,9], multiply(X,Y))
        
    def test_diveu(self):
        db = rd.randint(4,7)
        B,Q,R = [rd.randint(0,15) for _ in range(db)], [rd.randint(0,15) for _ in range(db-1)],[rd.randint(0,15) for _ in range(db-3)]
        A = add(R,multiply(B,Q))
        q,r = diveu(A,B)
        self.assertEqual(q, Q)
        self.assertEqual(r, R)