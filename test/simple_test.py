import sys
sys.path.append("..")
from src.fonctions import simple
import unittest
import random as rd

class Test_simple(unittest.TestCase):
    X = [rd.randint(0,15) for i in range(10)]
    Y = X+[0]
    def test_is_first_monome_null(self):
        if len(self.Y)!=1:
            self.assertNotEqual(simple(self.Y)[-1], 0)
    
    def test_correction(self):
        self.assertEqual(simple(self.Y),self.X)
    