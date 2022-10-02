import sys
sys.path.append("..")
from src.fonctions import deg
import unittest
import random as rd

class Test_deg(unittest.TestCase):
    X = [rd.randint(0,15) for i in range(10)]
    
    def test_is_int(self):
        self.assertEqual(type(deg(self.X)), int)
        
    def test_deg(self):
        self.assertEqual(2,deg([1,2,3]))
        