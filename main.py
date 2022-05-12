from dataclasses import dataclass
from boss import Boss
from filiale import Filiale
import unittest

#import biblio

#install behave

boss1 = Boss("Bernard Arnault", "LVMH")
filiale1 = Filiale("LVMH", "Louis Vuitton", boss1)

class FilialeTest(unittest.TestCase):

    def setUp(self):

        self.boss1 = Boss("Bernard Arnault", "LVMH")
        self.filiale1 = Filiale("LVMH", "Louis Vuitton", boss1)

    def testIsFiliale(self):
        self.assertEqual(self.filiale1.isFiliale(boss1), True)

if __name__ == '__main__':
    unittest.main()

