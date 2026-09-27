import unittest
from para8_5 import *

class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2,2),4)

    def test_kwarqs(self):
        self.assertEqual(adder(d=10, c=11), 21)

    def test_mixed(self):
        self.assertEqual(adder(3, a=2), 5)

    def test_wrong_type(self):
        self.assertEqual(adder("5", 10), 15)

if __name__ == "__main__":
    unittest.main()
