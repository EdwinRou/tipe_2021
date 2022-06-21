#coding:utf-8
from json import load
import sys, os
sys.path.append(os.path.realpath(os.path.dirname('src'))) # import src folder relative path
from src.fonctions import k, G
from src.decode import polynomes
import unittest

class TestMessage(unittest.TestCase):
    def test_is_message(self):
        m = [i for i in range(k)]
        m = polynomes(G.LeftMulColumnVec(m))
        self.assertEqual(k, len(m))
        for i in range(k):
            self.assertEqual(i, m[i])
        


if __name__ == '__main__':
    unittest.main()
else : 
    print("name of the module:", __name__)