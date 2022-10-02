import sys
sys.path.append("..")
from src.fonctions import puissance
import unittest
import random as rd

class Test_puissance(unittest.TestCase):
    x=rd.randint(0,15)
    n=rd.randint(0,10000)
    
    def test_correction(self):
        self.assertEqual(puissance(7,3), 1)
        
    def test_est_dans_le_coprs(self):
        self.assertIn(puissance(self.x,0),[i for i in range(16)])
        
