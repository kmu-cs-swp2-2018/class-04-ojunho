import unittest

from hangman import Hangman
from guess import Guess


class TestHangman(unittest.TestCase):

    def setUp(self):
        self.h1 = Hangman() #6
        self.g1 = Guess("default")

    def tearDown(self):
        pass

    def testdecrease(self):
        self.assertEqual(self.h1.remainingLives, 6)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 5)


if __name__ == '__main__':
    unittest.main()
