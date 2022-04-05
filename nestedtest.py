from dataclasses import dataclass
from Boss import Boss
from Filiale import Filiale
import unittest

#import biblio

#install behave

boss1 = Boss("Bernard Arnault", "LVMH")
filiale1 = Filiale("LVMH", "Louis Vuitton")

class OuterTestClass(unittest.TestCase):

    print("start outer class")

    def setUp(self):
        self.filiale2 = Filiale("LVMH", "Louis Vuitton")
        self.boss1 = Boss("Bernard Arnault", "LVMH")

    def testIsFiliale(self):
        self.assertEqual(self.filiale2.isFiliale(boss1), True)

    class InnerTestClass(unittest.TestCase):

        print("start inner class")

        def testIsFiliale(self):
            self.assertEqual(self.filiale2.isFiliale(boss1), True)

    def test_inner_test_class(self):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(self.InnerTestClass)
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()

