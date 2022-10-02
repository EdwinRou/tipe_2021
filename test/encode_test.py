import sys
sys.path.append("..")
from src.fonctions import encode, diveu, add, multiply
import unittest
import random as rd

class Test_encode(unittest.TestCase):
    u = [rd.randint(0,15) for i in range(9)]
    e = encode(u)
    
    def test_len_out(self):
        self.assertEqual(len(self.e), 15)
        
    def test_est_dans_le_coprs(self):
        for i in self.e:
            self.assertIn(i, [j for j in range(16)])
    
    def test_diveuclid(self):
        A,B = [9,5],[13, 22, 2]
        Q,R = diveu(A,B)
        self.assertEqual(A, add(multiply(B,Q),R))
    
