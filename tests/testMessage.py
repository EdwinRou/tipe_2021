#coding:utf-8
import sys, os
sys.path.append(os.path.realpath(os.path.dirname('src')))
from src.fonctions import k
import unittest

class TestMessage(unittest.TestCase):
    def test_is_message(self):
        m = [i for i in range(k)]
        self.assertEqual(k, len(m))


if __name__ == '__main__':
    unittest.main()
else : 
    print("name of the module:", __name__)