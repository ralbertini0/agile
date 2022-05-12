from dataclasses import dataclass
from boss import Boss
from filiale import Filiale
from capitale import Capitale
import unittest

#import biblio

#install behave

boss1 = Boss("Bernard Arnault", "LVMH")
filiale1 = Filiale("LVMH", "Louis Vuitton", boss1)
capitale1  = Capitale

class OuterTestClass(unittest.TestCase):

    print("start outer class")

    def setUp(self):

        self.boss1 = Boss("Bernard Arnault", "LVMH")
        self.filiale1 = Filiale("LVMH", "Louis Vuitton", boss1)


    def testIsFiliale(self):
        self.assertEqual(self.filiale1.isFiliale(self.pdg), True)

    class InnerTestClass(unittest.TestCase):
        def setUp(self):
            self.boss1 = Boss("Bernard Arnault", "LVMH")
            self.filiale1 = Filiale("LVMH", "Louis Vuitton", boss1)
        print("start inner class")

        def testIsFiliale(self):
            self.assertEqual(self.filiale1.isFiliale(self.pdg), True)

    def test_inner_test_class(self):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(self.InnerTestClass)
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()

