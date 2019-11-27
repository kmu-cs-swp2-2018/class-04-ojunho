import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        #단어 세개로 증가. g2, g3는 중복된글자가 있는 경우, e,n이 중복적으로 들어있는 경우를 선정.
        self.g1 = Guess('default')
        self.g2 = Guess('assignment')
        self.g3 = Guess('enhance')

        self.list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                     'w', 'x', 'y', 'z']

    def tearDown(self):
        pass


    # 숫자, 공백, 대문자, 를 넣어가면서 assertIn으로 확인.
    def testguess3(self):
        self.assertEqual(self.g3.displayCurrent(), 'e n _ _ n _ e ')
        self.assertFalse(self.g3.finished())

        #1. 공백을 넣어서 확인. >> 오류뜸.
        #self.assertIn(' ', self.list)

        #아무런 조건에도 걸리지 않아서 들어갈 수 있는 소문자 'a'는 self.list에 있기 때문에 됨.
        self.assertIn('a', self.list)

        #self.g3.displayCurrent()는 그대로임.
        self.assertEqual(self.g3.displayCurrent(), 'e n _ _ n _ e ')

        #2. 대문자를 넣어서 확인. >> 오류뜸.
        #self.assertIn('A', self.list)

        #그리고 대문자 'A'는 self.g3.guess('A')를 해서 확인 할때 이 단어에 없기때문에 assertFalse 했을 때 통과 한다.
        self.assertFalse(self.g3.guess('A'))

        #3. 숫자를 넣어서 확인. >> 오류뜸.
        #self.assertIn('1', self.list)




    def testguess2(self):
        self.assertEqual(self.g2.displayCurrent(), '_ _ _ _ _ n _ e n _ ')
        self.assertEqual(self.g2.displayGuessed(), ' e n ')
        self.assertEqual(self.g2.currentStatus, '_____n_en_')
        self.assertEqual(self.g2.guessedChars, {'', 'e', 'n'})
        self.assertFalse(self.g2.finished())

        self.assertTrue(self.g2.guess('a'))
        self.assertEqual(self.g2.displayCurrent(), 'a _ _ _ _ n _ e n _ ')
        self.assertEqual(self.g2.displayGuessed(), ' a e n ')
        self.assertEqual(self.g2.currentStatus, 'a____n_en_')
        self.assertEqual(self.g2.guessedChars, {'', 'a', 'e', 'n'})
        self.assertFalse(self.g2.finished())

        #s가 두번 나오는 단어가 한번에 처리가 잘 되는지 확인.
        self.assertTrue(self.g2.guess('s'))
        self.assertEqual(self.g2.displayCurrent(), 'a s s _ _ n _ e n _ ')
        self.assertEqual(self.g2.displayGuessed(), ' a e n s ')
        self.assertEqual(self.g2.currentStatus, 'ass__n_en_')
        self.assertEqual(self.g2.guessedChars, {'', 'a', 'e', 'n', 's'})
        self.assertFalse(self.g2.finished())

        # 이미 사용했던 단어 s를 넣었을 때를 확인.
        self.assertTrue(self.g2.guess('s'))
        # 37행에서 알 수 있듯이 이미 사용한 's'를 guess해도 True가 나온다. 단어에 있기 때문인 것 같다.
        self.assertEqual(self.g2.displayCurrent(), 'a s s _ _ n _ e n _ ')
        self.assertEqual(self.g2.displayGuessed(), ' a e n s ')
        self.assertEqual(self.g2.currentStatus, 'ass__n_en_')
        self.assertEqual(self.g2.guessedChars, {'', 'a', 'e', 'n', 's'})
        self.assertFalse(self.g2.finished())

        self.g2.guess('i')

        self.g2.guess('g')

        self.g2.guess('m')

        self.g2.guess('t')

        self.assertTrue(self.g2.finished())



    def testguess1(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.assertEqual(self.g1.guessedChars, {'', 'e', 'n'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('a')
        self.assertTrue(self.g1.guess('a'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'e', 'n'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('t')
        self.assertTrue(self.g1.guess('t'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'e', 'n', 't'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('u')
        self.assertTrue(self.g1.guess('u'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'e', 'n', 't', 'u'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('d')
        self.assertTrue(self.g1.guess('d'))
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')
        self.assertEqual(self.g1.currentStatus, 'de_au_t')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'd', 'e', 'n', 't', 'u'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('f')
        self.assertTrue(self.g1.guess('f'))
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u ')
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'd', 'e', 'f', 'n', 't', 'u'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('z')
        self.assertFalse(self.g1.guess('z'))
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u z ')
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'd', 'e', 'f', 'n', 't', 'u', 'z'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('l')
        self.assertTrue(self.g1.guess('l'))
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l n t u z ')
        self.assertEqual(self.g1.currentStatus, 'default')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'd', 'e', 'f', 'l', 'n', 't', 'u', 'z'})
        self.assertTrue(self.g1.finished())


    #def testguessFinished(self):
    #    self.assertEqual(self.g1.finished(), True)

if __name__ == '__main__':
    unittest.main()

